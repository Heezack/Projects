drop function if exists numPlayerAwardsbySchool;
create or replace function numPlayerAwardsbySchool(input_schoolID varchar) returns integer as
$$
    declare 
        numBySchool integer default 0; 
    begin
    select count(*) from (
    select distinct ap.playerid, ap.yearid, ap.awardid from AwardsPlayers ap
        where $1 in (select uc.schoolid from
            (select distinct c.playerid, c.schoolid from CollegePlaying c) as uc
            where uc.playerid = ap.playerid)) as award_by_school
        into numBySchool; 
        return numBySchool;
    end;
$$ language plpgsql;

drop table if exists NumAwardsbySchool;
create table NumAwardsbySchool as
select schoolid, numPlayerAwardsbySchool(schoolid) as count from Schools s
order by count desc;
 ALTER TABLE NumAwardsbySchool ADD PRIMARY KEY (schoolid);
-- \copy numawardsbyschool to '/home/yerong/Documents/533-project/numawardsbyschool.csv' delimiters',' csv header