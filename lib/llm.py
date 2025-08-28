from openai import OpenAI
from lib.config import Config

class LLM :
    def __init__(self, api_key: str) -> None:
        self._config = Config()
        self._client = OpenAI(**self._config.forllm_client())
