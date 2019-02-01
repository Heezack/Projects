drop table if exists RaiseOnAward;
create table RaiseOnAward as
select  uniqueFirst.first, uniqueFirst.playerID, updated_salary, old_salary, (updated_salary-old_salary)/old_salary*100  as "increase in %" from
    (select uniqueID.playerID, first from 
        (select distinct playerID from
        AwardsPlayers) as uniqueID,
        (select ap.playerID, min(ap.yearID) as first from
        AwardsPlayers ap
        group by ap.playerID) firstAwardyear
    where firstAwardyear.playerID = uniqueID.playerID) as uniqueFirst,
    (select uniqueFirstAward.playerID, avg(s.salary) as updated_salary from
        Salaries s,
        (select uniqueID.playerID, first from 
            (select distinct playerID from
            AwardsPlayers) as uniqueID,
            (select ap.playerID, min(ap.yearID) as first from
            AwardsPlayers ap
            group by ap.playerID) firstAwardyear
        where firstAwardyear.playerID = uniqueID.playerID) as uniqueFirstAward
    where s.playerID = uniqueFirstAward.playerID and s.year >= uniqueFirstAward.first group by uniqueFirstAward.playerID) as new
    left join (select uniqueFirstAward.playerID, avg(s.salary) as old_salary from
        Salaries s,
        (select uniqueID.playerID, first from 
            (select distinct playerID from
            AwardsPlayers) as uniqueID,
            (select ap.playerID, min(ap.yearID) as first from
            AwardsPlayers ap
            group by ap.playerID) firstAwardyear
        where firstAwardyear.playerID = uniqueID.playerID) as uniqueFirstAward
    where s.playerID = uniqueFirstAward.playerID and s.year < uniqueFirstAward.first group by uniqueFirstAward.playerID) as old
on new.playerID = old.playerID
where uniqueFirst.playerID = new.playerID 
and (old_salary is not null) and (updated_salary is not null)
order by uniqueFirst.first;
ALTER TABLE RaiseOnAward ADD PRIMARY KEY (playerID); -- \copy RaiseOnAward to '/home/yerong/Documents/533-project/RaiseOnAward.csv' delimiters',' csv header 
