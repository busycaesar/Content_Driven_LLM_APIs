from langchain.schema import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter, CharacterTextSplitter

class TextSplitterAdaptor:

    @staticmethod
    def split_content(
        content, 
        chunk_size=None, 
        chunk_overlap=None, 
        separator=None
    ):
        if not separator and (not chunk_size or not chunk_overlap):
            raise ValueError("Either separator or chunk size and chunk overlap should be provided.")

        # Convert the text into Document type.
        content = Document(page_content=content)

        if separator:
            text_splitter = CharacterTextSplitter(
                separator=separator,
                is_separator_regex=False
            )
        else:
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=chunk_size,
                chunk_overlap=chunk_overlap
            )

        # Use the text splitter to split the content into chunks.
        return text_splitter.split_documents([content])