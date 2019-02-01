create or replace function leagueAlert() returns trigger as
$$
begin
	if new.lgID not in ('AA','AL','NA','PL','NL','UA','FL') then 
		raise exception 'Invalid lgID.';
	else return new;
	end if;
end;
$$
language plpgsql;

drop trigger if exists printLeagueAlert on Teams;
create trigger printLeagueAlert after insert on Teams
for each row
execute procedure leagueAlert();

--trigger test
delete from Teams where year in (3,4);
insert into Teams(year, teamID, lgID) values
(3,11111,'NNA');
delete from Teams where year in (3,4)；

create or replace function finalGameAlert() returns trigger as
$$
begin
	if new.deathDay is not null then 
		raise notice 'Please remember to update %''s final game.', new.playerID;
	return new;
	end if;
end;
$$
language plpgsql;

drop trigger if exists printFGAlert on People;
create trigger printFGAlert after insert on People
for each row
execute procedure finalGameAlert();

--trigger test
delete from People where playerID in ('person3');
insert into People(playerID, deathDay) values
('person3','1990-10-03');
delete from People where playerID in ('person3')