from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    name: str = "BaseAgent"

    @abstractmethod
    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        raise NotImplementedError
