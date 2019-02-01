drop table if exists Years2Award;

create table Years2Award as
select * from 
    (select uniqueDebut.playerID, uniqueDebut.first-extract(year from p.debut)::int as difference from
        People p,
        (select uniqueID.playerID, first from 
            (select distinct playerID from
            AwardsPlayers) as uniqueID,
            (select ap.playerID, min(ap.yearID) as first from
            AwardsPlayers ap
            group by ap.playerID) firstAwardyear
        where firstAwardyear.playerID = uniqueID.playerID) as uniqueDebut
    where p.playerID = uniqueDebut.playerID) as player
where difference <= 30 and difference >=0; -- \copy Years2Award to '/home/yerong/Documents/533-project/Years2Award.csv' delimiters',' csv header
