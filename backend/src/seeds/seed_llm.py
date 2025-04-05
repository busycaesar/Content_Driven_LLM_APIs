from models import LLM, db

sample_llm_table_data = [
    LLM(name="gemini-1.5-flash")
]

def seed_llm_table():
    if db.session.query(LLM).first():
        return
    
    db.session.bulk_save_objects(sample_llm_table_data)
    db.session.commit()