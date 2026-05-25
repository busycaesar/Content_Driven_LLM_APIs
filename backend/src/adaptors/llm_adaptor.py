from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from utils import EnvVars, ErrorMessages

class LLMAdaptor:
    def __init__(self, model_name):
        self.prompt_template = self._get_prompt_template()
        self.llm = self._get_model(model_name)

        if not self.llm:
            raise ValueError(ErrorMessages.NOT_FOUND("LLM through Model Name."))

    def _get_prompt_template(self):
        return PromptTemplate(
            input_variables=[
                "prompt_template",
                "prompt",
                "relevant_chunk_of_data"
            ],
            template= """
            {prompt_template}

            Relevant Content: {relevant_chunk_of_data}

            User's Question: {prompt}
            """
        )

    def _google_model(self, model_name):
        if not EnvVars.GEMINI_API_KEYS:
            raise ValueError(ErrorMessages.MISSING_DATA(["GEMINI_API_KEYS"]))

        return ChatGoogleGenerativeAI(
            model=model_name,
            google_api_key=EnvVars.GEMINI_API_KEYS
        )

    def _get_model(self, model_name):
        if model_name == "gemini-1.5-flash":
            return self._google_model(model_name)

        return

    def generate_response(
        self,
        prompt,
        relevant_chunk_of_data,
        prompt_template_text,
    ):
        if not prompt or not relevant_chunk_of_data or not prompt_template_text:
            raise ValueError(ErrorMessages.MISSING_DATA(["prompt", "relevant_chunk_of_data", "prompt_template_text"]))

        # Chain the template and instance
        chain = self.prompt_template | self.llm

        # Invoke the chain by passing the input variables of prompt
        response = chain.invoke({
            "prompt_template":prompt_template_text,
            "prompt":prompt,
            "relevant_chunk_of_data": relevant_chunk_of_data
        })

        # Return the response
        return response.content