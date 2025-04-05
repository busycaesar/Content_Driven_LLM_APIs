from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from utils import EnvVars

class LLMAdaptor:

    @staticmethod
    def generate_response(
        prompt,
        relevant_chunk_of_data,
        prompt_template,
        llm
    ):
        if not prompt or not relevant_chunk_of_data:
            raise ValueError("Prompt and Relevant Chunk of Data are not provided.")
        
        prompt_template = PromptTemplate(
            input_variables=[
                "prompt_template",
                "prompt",
                "relevant_chunk_of_data"
            ],
            template= """
            {prompt_template}

            Content: {relevant_chunk_of_data}

            User's Question: {prompt}
            """
        )

        if not EnvVars.GEMINI_API_KEYS: return

        llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=EnvVars.GEMINI_API_KEYS)

        # Chain the template and instance
        chain = prompt_template | llm

        # Invoke the chain by passing the input variables of prompt
        response = chain.invoke({
            "prompt_template":prompt_template,
            "prompt":prompt,
            "relevant_chunk_of_data": relevant_chunk_of_data
        })

        # Return the response
        return response.content