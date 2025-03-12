from pydantic import BaseModel
from typing import Dict, Any, List

class StatsResponse(BaseModel):
    user_count: int
    item_count: int
    active_users_last_day: int
    active_users_last_week: int
    active_users_last_month: int
    system_health: Dict[str, Any]
    recent_activities: List[Dict[str, Any]]
