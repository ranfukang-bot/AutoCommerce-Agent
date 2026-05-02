from typing import Dict, Any
from .base_agent import BaseAgent


class ViralScriptAnalysisAgent(BaseAgent):
    name = "Viral Script Analysis Agent"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        product = context["product"]
        insight = context["product_insight"]

        hook = self._build_hook(product, insight)
        result = {
            "hook": hook,
            "structure": [
                {
                    "time": "0-3s",
                    "goal": "Stop scrolling",
                    "content": hook,
                    "camera": "close-up or strong visual contrast"
                },
                {
                    "time": "3-8s",
                    "goal": "Show product value",
                    "content": "Demonstrate the most visible selling point with natural movement.",
                    "camera": "medium shot, stable motion, clear product focus"
                },
                {
                    "time": "8-15s",
                    "goal": "Build purchase impulse",
                    "content": "Show usage scenario, texture, fit, or result; end with simple call-to-action.",
                    "camera": "detail shot + lifestyle shot"
                }
            ],
            "conversion_triggers": [
                "visual proof within 3 seconds",
                "simple benefit statement",
                "clear product close-up",
                "realistic lifestyle context"
            ],
            "avoid": [
                "too much text",
                "complex hand-object interaction",
                "unclear product identity",
                "slow opening"
            ]
        }

        context["viral_script"] = result
        return context

    def _build_hook(self, product: Dict[str, Any], insight: Dict[str, Any]) -> str:
        name = product.get("product_name", "this product")
        category = product.get("category", "product")
        market = product.get("target_market", "market")
        return f"Make {name} instantly understandable for {market} viewers with a strong visual opening."
