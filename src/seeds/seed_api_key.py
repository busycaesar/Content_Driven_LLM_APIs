from models import UserAPIKey, db

sample_user_api_key_table_data = [
    UserAPIKey("1234", 1)
]

def seed_user_api_key_table():
    if db.session.query(UserAPIKey).first():
        return
    
    db.session.add_all(sample_user_api_key_table_data)
    db.session.commit()