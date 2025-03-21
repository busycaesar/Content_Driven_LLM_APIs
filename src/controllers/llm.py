from services import LLMService

class LLMController:
    @staticmethod
    async def get_all_llms():
        return await LLMService.get_all_llms()