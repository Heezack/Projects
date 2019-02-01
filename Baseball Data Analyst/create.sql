-- ----------------------------
-- Create People table
-- ----------------------------
drop table if exists People CASCADE;
create table People (
  playerID varchar(255),
  birthDay date DEFAULT NULL,
  birthCountry varchar(255) DEFAULT NULL,
  birthState varchar(255) DEFAULT NULL,
  birthCity varchar(255) DEFAULT NULL,
  deathDay date DEFAULT NULL,
  nameFirst varchar(255) DEFAULT NULL,
  nameLast varchar(255) DEFAULT NULL,
  nameGiven varchar(255) DEFAULT NULL,
  weight integer DEFAULT NULL,
  height integer DEFAULT NULL,
  bats varchar(255) DEFAULT NULL,
  throws varchar(255) DEFAULT NULL,
  debut date DEFAULT NULL,
  finalGame date DEFAULT NULL,

  constraint people_pkey primary key (playerID)
);

-- ----------------------------
--  Table structure for Teams
-- ----------------------------
DROP TABLE IF EXISTS Teams cascade;
CREATE TABLE Teams (
  year integer DEFAULT NULL,
  lgID varchar(255) DEFAULT NULL,
  teamID varchar(255) DEFAULT NULL,
  divID varchar(255) DEFAULT NULL,
  Rank integer DEFAULT NULL,
  G integer DEFAULT NULL,
  Ghome varchar(255) DEFAULT NULL,
  W integer DEFAULT NULL,
  L integer DEFAULT NULL,
  DivWin varchar(255) DEFAULT NULL,
  WCWin varchar(255) DEFAULT NULL,
  LgWin varchar(255) DEFAULT NULL,
  WSWin varchar(255) DEFAULT NULL,
  R integer DEFAULT NULL,
  AB integer DEFAULT NULL,
  H integer DEFAULT NULL,
  "2B" integer DEFAULT NULL,
  "3B" integer DEFAULT NULL,
  HR integer DEFAULT NULL,
  BB integer DEFAULT NULL,
  SO integer DEFAULT NULL,
  SB integer DEFAULT NULL,
  CS integer DEFAULT NULL,
  HBP varchar(255) DEFAULT NULL,
  SF varchar(255) DEFAULT NULL,
  RA integer DEFAULT NULL,
  ER integer DEFAULT NULL,
  ERA float DEFAULT NULL,
  CG integer DEFAULT NULL,
  SHO integer DEFAULT NULL,
  SV integer DEFAULT NULL,
  IPouts integer DEFAULT NULL,
  HA integer DEFAULT NULL,
  HRA integer DEFAULT NULL,
  BBA integer DEFAULT NULL,
  SOA integer DEFAULT NULL,
  E integer DEFAULT NULL,
  DP varchar(255) DEFAULT NULL,
  FP float DEFAULT NULL,
  name varchar(255) DEFAULT NULL,
  park varchar(255) DEFAULT NULL,
  attendance varchar(255) DEFAULT NULL,
  BPF integer DEFAULT NULL,
  PPF integer DEFAULT NULL,
  teamIDBR varchar(255) DEFAULT NULL,
  teamIDretro varchar(255) DEFAULT NULL,
    
  constraint team_pkey primary key (teamID, year)
); 

drop table if exists Appearances cascade;
create table Appearances (
    year integer,
    teamID varchar(255),
    lgID varchar(255) DEFAULT NULL,
    playerID varchar(255),
    G_all integer DEFAULT NULL,
    GS varchar(255) DEFAULT NULL,
    G_batting integer DEFAULT NULL,
    G_defense integer DEFAULT NULL,
    G_p integer DEFAULT NULL,
    G_c integer DEFAULT NULL,
    G_1b integer DEFAULT NULL,
    G_2b integer DEFAULT NULL,
    G_3b integer DEFAULT NULL,
    G_ss integer DEFAULT NULL,
    G_lf integer DEFAULT NULL,
    G_cf integer DEFAULT NULL,
    G_rf integer DEFAULT NULL,
    G_of integer DEFAULT NULL,
    G_dh varchar(255) DEFAULT NULL,
    G_ph varchar(255) DEFAULT NULL,
    G_pr varchar(255) DEFAULT NULL,
    
    constraint appearances_pkey primary key (year, teamID, playerID),
    constraint People_fk foreign key (playerID) references People(playerID),
    constraint Teams_fk foreign key (year, teamID) references Teams(year, teamID)
);

-- ----------------------------
--  Table structure for Batting
-- ----------------------------
drop table if exists Batting;
create table Batting (
  playerID varchar(255) DEFAULT NULL,
  year integer DEFAULT NULL,
  stint integer DEFAULT NULL,
  teamID varchar(255) DEFAULT NULL,
  lgID varchar(255) DEFAULT NULL,
  G integer DEFAULT NULL,
  AB integer DEFAULT NULL,
  R integer DEFAULT NULL,
  H integer DEFAULT NULL,
  "2B" integer DEFAULT NULL,
  "3B" integer DEFAULT NULL,
  HR integer DEFAULT NULL,
  RBI integer DEFAULT NULL,
  SB integer DEFAULT NULL,
  CS integer DEFAULT NULL,
  BB integer DEFAULT NULL,
  SO integer DEFAULT NULL,
  IBB varchar(255) DEFAULT NULL,
  HBP varchar(255) DEFAULT NULL,
  SH varchar(255) DEFAULT NULL,
  SF varchar(255) DEFAULT NULL,
  GIDP varchar(255) DEFAULT NULL,
  
  constraint batting_pkey primary key (playerID, year, stint)
);


-- ----------------------------
--  Table structure for Schools
-- ----------------------------
DROP TABLE IF EXISTS Schools CASCADE;
CREATE TABLE Schools (
  schoolID varchar(255) DEFAULT NULL,
  name_full varchar(255) DEFAULT NULL,
  city varchar(255) DEFAULT NULL,
  state varchar(255) DEFAULT NULL,
  country varchar(255) DEFAULT NULL,
  
  constraint Schools_pkey primary key (schoolID)
);


-- ----------------------------
--  Table structure for CollegePlaying
-- ----------------------------
DROP TABLE IF EXISTS CollegePlaying;
CREATE TABLE CollegePlaying (
  playerID varchar(255),
  schoolID varchar(255),
  yearID integer,
  
  constraint CollegePlaying_pkey primary key (playerID, schoolID, yearID),
  constraint CollegePlaying_fkey_playerID foreign key (playerID) references people(playerID)
--  constraint CollegePlaying_fkey_schoolID foreign key (schoolID) references schools(schoolID)
);

-- ---------------------------- 
--  Table structure for Managers 
-- ---------------------------- 
DROP TABLE IF EXISTS Managers cascade; 
CREATE TABLE Managers ( 
  playerID varchar(255) DEFAULT NULL, 
  yearID integer DEFAULT NULL, 
  teamID varchar(255) DEFAULT NULL, 
  lgID varchar(255) DEFAULT NULL, 
  inseason integer DEFAULT NULL, 
  G integer DEFAULT NULL, 
  W integer DEFAULT NULL, 
  L integer DEFAULT NULL, 
  rank integer DEFAULT NULL, 
  plyrMgr varchar(255) DEFAULT NULL,
  
  constraint Managers_pkey primary key (playerID, yearID, teamID, lgID, inseason),
  constraint Managers_fkey_playerID foreign key (playerID) references People(playerID),
  constraint Teams_fk foreign key (yearID, teamID) references Teams(year, teamID)

);

-- ----------------------------
--  Table structure for AwardsManagers
-- ----------------------------
DROP TABLE IF EXISTS AwardsManagers;
CREATE TABLE AwardsManagers (
  playerID varchar(255) DEFAULT NULL,
  awardID varchar(255) DEFAULT NULL,
  yearID integer DEFAULT NULL,
  lgID varchar(255) DEFAULT NULL,
  tie varchar(255) DEFAULT NULL,
  notes varchar(255) DEFAULT NULL,
  
  constraint AwardsManagers_pkey primary key (playerID, awardID, yearID, lgID),
  constraint AwardsManagers_fkey foreign key (playerID) references People(playerID)
);


-- ----------------------------
--  Table structure for AwardsPlayers
-- ----------------------------
DROP TABLE IF EXISTS AwardsPlayers cascade;
CREATE TABLE AwardsPlayers (
  playerID varchar(255) DEFAULT NULL,
  awardID varchar(255) DEFAULT NULL,
  yearID integer DEFAULT NULL,
  lgID varchar(255) DEFAULT NULL,
  tie varchar(255) DEFAULT NULL,
  notes varchar(255) DEFAULT NULL
);

-- ----------------------------
--  Table structure for Salaries
-- ----------------------------
DROP TABLE IF EXISTS Salaries cascade;
CREATE TABLE Salaries (
  year integer DEFAULT NULL,
  teamID varchar(255) DEFAULT NULL,
  lgID varchar(255) DEFAULT NULL,
  playerID varchar(255) DEFAULT NULL,
  salary integer DEFAULT NULL,
  
  constraint Salaries_pkey primary key (year, teamID, playerID),
  constraint People_fk foreign key (playerID) references People(playerID),  
  constraint Teams_fk foreign key (year, teamID) references Teams(year, teamID)
);

