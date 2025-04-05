class ConfigVars:
    # Default values.
    class DEFAULT:
        CHUNK_SIZE = 1000
        CHUNK_OVERLAP = 250
        PROMPT_TEMPLATE = """
        This is the prompt template
        """;
        LLM_ID = 1
        RELEVANT_CHUNKS_REQUIRED = 3