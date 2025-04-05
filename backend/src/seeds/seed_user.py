from models import User, db

sample_user_table_data = [
    User("Dev", "dev@shahtech.info")
]

def seed_user_table():
    if db.session.query(User).first():
        return
    
    db.session.add_all(sample_user_table_data)
    db.session.commit()