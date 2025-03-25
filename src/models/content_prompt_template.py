from .db import db
from sqlalchemy import Column, Integer, Text, DateTime, String
from sqlalchemy.sql import func
from utils import ErrorMessages

class ContentPromptTemplate(db.Model):
    __tablename__ = "content_prompt_template"

    id = Column(Integer, primary_key=True, autoincrement=True)
    collection_id = Column(String(32), nullable=False,unique=True)
    prompt_template = Column(Text, nullable=False)
    created_on = Column(DateTime, nullable=False, default=func.now())
    modified_on = Column(DateTime, onupdate=func.now())

    def __init__(self, collection_id, prompt_template=None):
        if not collection_id:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["collection_id"],
                    "Model layer error."
                )
            )

        self.collection_id = collection_id
        self.prompt_template = prompt_template

    def _verify_prompt_template(self):
        if not self.prompt_template:
            raise ValueError(
                ErrorMessages.MISSING_DATA(
                    ["prompt_template"],
                    "Model layer error."
                )
            )

    # Store a new prompt template using the collection id.
    def add(self):
        self._verify_prompt_template()

        try:
            db.session.add(self)
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"adding the prompt template for the user content's. {str(e)}."
            ))

    # Update the stored prompt template using the collection id.
    def update(self):
        self._verify_prompt_template()

        try:
            db.session.commit()

        except Exception as e:
            db.session.rollback()
            raise ValueError(ErrorMessages.EXCEPTION(
                f"updating the prompt template for the user content's. {str(e)}."
            ))

    # Get the prompt template using the collection id.
    def get_prompt_template(self):
        data = db.session.query(ContentPromptTemplate).filter_by(collection_id=self.collection_id).first()

        self.prompt_template = data.prompt_template

        if not self.prompt_template:
            raise ValueError(ErrorMessages.NOT_FOUND("Prompt template with collection id."))
        
        return self.prompt_template