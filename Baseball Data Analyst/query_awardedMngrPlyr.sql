#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 00:44:37 2018

@author: zehe
"""

create or replace function awarded_mngr_plr() returns void as
$$
declare

begin
    drop table if exists awarded_m_p;
    create table awarded_m_p (
        awardSeqID serial not null primary key,
        managerID varchar(255) default null,
        cnt int default 0
    );
	
	drop table if exists awardedMngrTeam;
    create table awardedMngrTeam as 
        select am.playerID, am.awardID, am.yearID, am.lgID, m.teamID from awardsManagers as am, managers as m
        where am.playerID=m.playerID
            and am.yearID=m.yearID
            and am.lgID=m.lgID;

	drop table if exists awardedPlyrTeam;
    create table awardedPlyrTeam as
        select ap.playerID, ap.awardID, ap.yearID, ap.lgID, a.teamID from awardsPlayers as ap, appearances as a
        where ap.playerID=a.playerID
            and ap.yearID=a.year
            and ap.lgID=a.lgID;
			
    insert into awarded_m_p(managerID, cnt)
        select amt.playerID, count(*) from awardedMngrTeam AS amt, awardedPlyrTeam as apt
        where amt.teamID=apt.teamID
            and amt.lgID=apt.lgID
            and apt.yearID - amt.yearID >= 0
            and apt.yearID - amt.yearID <= 3
		group by amt.playerID, amt.yearID;
end;
$$
language plpgsql;

select awarded_mngr_plr();
select * from awarded_m_p order by cnt;
select count(distinct (playerID, yearID)) from awardsManagers