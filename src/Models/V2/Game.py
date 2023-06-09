#region Imports
from Base import ModelBase;
from dataclasses import dataclass
#endregion Imports

@dataclass
class Game(ModelBase):
    id: str = None;
    sport: str = None;
    league: str = None;
    start_date: str = None;
    away_team: str = None;
    home_team: str = None;
    is_live: bool = None;
    is_popular: bool = None;
    tournament: str = None;
    status: str = None;