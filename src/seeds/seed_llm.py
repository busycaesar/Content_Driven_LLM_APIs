from models import LLM, db

sample_llm_table_data = [
    LLM(name="qwen2.5:3b")
]

def seed_llm_table():
    if db.session.query(LLM).first():
        return
    
    db.session.bulk_save_objects(sample_llm_table_data)
    db.session.commit()