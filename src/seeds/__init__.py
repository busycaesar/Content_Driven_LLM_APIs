from .seed_llm import seed_llm_table
from .seed_user import seed_user_table
from .seed_api_key import seed_user_api_key_table

def seed_all_tables():
    seed_llm_table()
    seed_user_table()
    seed_user_api_key_table()