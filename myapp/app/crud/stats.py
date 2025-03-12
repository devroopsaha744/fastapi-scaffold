from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.models.user import User
from app.models.item import Item
from app.services.health import check_all_services

def get_system_stats(db: Session):
    now = datetime.utcnow()
    day_ago = now - timedelta(days=1)
    week_ago = now - timedelta(weeks=1)
    month_ago = now - timedelta(days=30)
    user_count = db.query(func.count(User.id)).scalar()
    item_count = db.query(func.count(Item.id)).scalar()
    active_day = db.query(func.count(User.id)).filter(User.updated_at >= day_ago).scalar()
    active_week = db.query(func.count(User.id)).filter(User.updated_at >= week_ago).scalar()
    active_month = db.query(func.count(User.id)).filter(User.updated_at >= month_ago).scalar()
    system_health = check_all_services()
    recent_activities = [{'type': 'user_created', 'timestamp': now.isoformat(), 'details': 'Sample activity'}]
    return {'user_count': user_count, 'item_count': item_count, 'active_users_last_day': active_day, 'active_users_last_week': active_week, 'active_users_last_month': active_month, 'system_health': system_health, 'recent_activities': recent_activities}
