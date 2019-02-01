create or replace function rank_salary() returns void as
$$
declare

begin
    
    drop table if exists archive;
    create table archive as(
        select t.teamID, round(AVG(t.rank),1) as avgRank, round(AVG(s.salary),2) as avgSalary
		from teams as t join salaries as s
        on t.teamID=s.teamID and t.year > 2010 and s.year > 2010
        group by t.teamID);


end;
$$
language plpgsql;

select rank_salary ();
select * from archive ORDER by teamid