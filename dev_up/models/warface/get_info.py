import enum
import typing as ty
from pydantic import BaseModel, Field


class WarfaceGetInfoTypeEnum(enum.Enum):
    STATISTICS = "statistics"
    ACHIEVEMENTS = "achievements"
    PVP = "pvp"
    PVE = "pve"


class WarfaceGetInfoStatisticsResponse(BaseModel):
    nickname: str
    server: str
    player_type: str = Field(default_factory=str, alias="playerType")
    skills: ty.List[int]
    pvp: int
    pve: int
    pvp_kd: float = Field(default_factory=float, alias="pvpKd")
    pve_kd: float = Field(default_factory=float, alias="pveKd")
    rang_name: str = Field(default_factory=str, alias="rangName")
    rang_lvl: int = Field(default_factory=int, alias="rangLvl")
    experience: int
    next_rang_experience: int = Field(default_factory=int, alias="nextRangExperience")
    longest_match_time: int = Field(default_factory=int, alias="longestMatchTime")
    total_matches_time: int = Field(default_factory=int, alias="totalMatchesTime")
    in_game_time: int = Field(default_factory=int, alias="inGameTime")
    execution_time: int = Field(default_factory=int, alias="executionTime")


class WarfaceGetInfoPVPResponseTotal(BaseModel):
    kills: int
    shoots: int
    hits: int
    killed_by_mines: int = Field(default_factory=int, alias="killedByMines")
    killed_in_close: int = Field(default_factory=int, alias="killedInClose")
    suicides: int
    deads: int
    kd: float
    kd_0_0_0_1: int
    kd_0_0_1: int
    kd_0_1: int 
    matches_played: int = Field(default_factory=int, alias="matchesPlayed")
    wins: int
    losses: int
    draws: int
    win_percent: float = Field(default_factory=float, alias="winPercent")
    match_exceptions: int = Field(default_factory=int, alias="matchExceptions")
    stopped_matches: int = Field(default_factory=int, alias="stoppedMatches")
    in_game_time: int = Field(default_factory=int, alias="inGameTime")


class WarfaceGetInfoPVPResponseByClass(BaseModel):
    shoots: int
    hits: int
    accuracy: float
    headshots: int
    headshots_in_close: int = Field(default_factory=int, alias="inGameTime")
    in_game_time: int = Field(default_factory=int, alias="inGameTime")


class WarfaceGetInfoPVPResponse(BaseModel):
    total: WarfaceGetInfoPVPResponseTotal
    stormtrooper: WarfaceGetInfoPVPResponseByClass
    medic: WarfaceGetInfoPVPResponseByClass
    sed: WarfaceGetInfoPVPResponseByClass
    engineer: WarfaceGetInfoPVPResponseByClass
    sniper: WarfaceGetInfoPVPResponseByClass
    execution_time: int = Field(default_factory=int, alias="executionTime")


class WarfaceGetInfoPVEResponseTotal(BaseModel):
    kills: int
    shoots: int
    hits: int
    killed_by_mines: int = Field(default_factory=int, alias="killedByMines")
    killed_in_close: int = Field(default_factory=int, alias="killedInClose")
    suicides: int
    deads: int
    kd: float
    kd_0_0_1: int
    kd_0_1: int
    kd_1: int 
    missions_played: int = Field(default_factory=int, alias="missionsPlayed")
    completed_missions: int = Field(default_factory=int, alias="completedMissions")
    losed_missions: int = Field(default_factory=int, alias="losedMissions")
    win_percent: float = Field(default_factory=float, alias="winPercent")
    signs_used: float = Field(default_factory=float, alias="signsUsed")
    match_exceptions: int = Field(default_factory=int, alias="matchExceptions")
    stopped_missions: int = Field(default_factory=int, alias="stoppedMissions")
    in_game_time: int = Field(default_factory=int, alias="inGameTime")


class WarfaceGetInfoPVEResponseByClass(BaseModel):
    shoots: int
    hits: int
    accuracy: float
    headshots: int
    headshots_in_close: int = Field(default_factory=int, alias="inGameTime")
    in_game_time: int = Field(default_factory=int, alias="inGameTime")


class WarfaceGetInfoPVEResponse(BaseModel):
    total: WarfaceGetInfoPVEResponseTotal
    stormtrooper: WarfaceGetInfoPVEResponseByClass
    medic: WarfaceGetInfoPVEResponseByClass
    sed: WarfaceGetInfoPVEResponseByClass
    engineer: WarfaceGetInfoPVEResponseByClass
    sniper: WarfaceGetInfoPVEResponseByClass
    execution_time: int = Field(default_factory=int, alias="executionTime")


class WarfaceGetInfoAchievementsResponseItem(BaseModel):
    img: str
    name: str
    description: str
    completed: bool
    date: int


class WarfaceGetInfoAchievementsResponse(BaseModel):
    count: int
    completed_count: int = Field(default_factory=int, alias="completedCount")
    marks: ty.List[WarfaceGetInfoAchievementsResponseItem]
    badges: ty.List[WarfaceGetInfoAchievementsResponseItem]
    stripes: ty.List[WarfaceGetInfoAchievementsResponseItem]
    execution_time: int = Field(default_factory=int, alias="executionTime")


class WarfaceGetInfo(BaseModel):
    response: ty.Union[WarfaceGetInfoStatisticsResponse, WarfaceGetInfoPVPResponse, WarfaceGetInfoPVEResponse, WarfaceGetInfoAchievementsResponse]
