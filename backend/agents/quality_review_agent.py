from typing import Dict, Any
from .base_agent import BaseAgent


class QualityReviewAgent(BaseAgent):
    name = "Quality Review Agent"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        result = {
            "scorecard": [
                {"dimension": "Product Consistency", "weight": 25, "standard": "Product shape, color, print, and key features remain stable."},
                {"dimension": "Motion Naturalness", "weight": 20, "standard": "Human movement or product movement looks realistic and controlled."},
                {"dimension": "Commercial Clarity", "weight": 20, "standard": "Viewer can understand what is being sold within 3 seconds."},
                {"dimension": "Visual Quality", "weight": 15, "standard": "Lighting, composition, texture, and overall polish are suitable for ads."},
                {"dimension": "Platform Safety", "weight": 10, "standard": "No risky text, misleading claims, or sensitive visual elements."},
                {"dimension": "Conversion Potential", "weight": 10, "standard": "Video has clear desire trigger, usage scenario, and purchase motivation."}
            ],
            "pass_threshold": 80,
            "revision_rules": [
                "If product consistency score is below 18/25, regenerate instead of minor editing.",
                "If the first 3 seconds are unclear, rewrite the hook and opening shot.",
                "If motion distortion exceeds 2 seconds in a 15-second video, mark as not ready for delivery.",
                "If product value is not visible, replace lifestyle shot with close-up proof shot."
            ]
        }

        context["quality_review"] = result
        return context
