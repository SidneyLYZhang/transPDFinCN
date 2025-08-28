from typing import Optional

class ProperNoun :
    def __init__(self, text: str) -> None:
        self._text = text
    
    def prompt(self, custom_prompt: Optional[str] = None) -> str:
        if custom_prompt :
            return custom_prompt.format(self._text)
        else :
            return "setting prompt"