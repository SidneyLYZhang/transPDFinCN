from dotenv import load_dotenv

class Config :
    __all__ = ["forllm_client"]
    _normal = {
        "temperature": 0.5,
        "max_tokens": 16800,
        "top_p": 0.65,
    }
    def __init__(self) -> None:
        self.__config = load_dotenv()
    
    def _get(self, key: str) -> str:
        if key in self.__config :
            return self.__config[key]
        else :
            return Config._normal[key]

    def forllm_client(self) -> dict:
        return {
            "api_key": self.__config["API_KEY"],
            "base_url": self.__config["BASE_URL"],
        }