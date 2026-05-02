from typing import Dict, Any, List
from .base_agent import BaseAgent


class ProductInsightAgent(BaseAgent):
    name = "Product Insight Agent"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        product = context["product"]
        selling_points: List[str] = product.get("selling_points", [])
        category = product.get("category", "general product")
        market = product.get("target_market", "global market")

        pain_points = self._infer_pain_points(category)
        angles = self._suggest_angles(category, selling_points)

        result = {
            "product_name": product.get("product_name"),
            "category": category,
            "target_market": market,
            "core_selling_points": selling_points,
            "consumer_pain_points": pain_points,
            "localized_strategy": [
                f"Use simple, direct benefit-driven language for {market}.",
                "Show product usage within the first 3 seconds.",
                "Avoid over-explaining; prioritize visual proof and fast rhythm."
            ],
            "recommended_video_angles": angles
        }

        context["product_insight"] = result
        return context

    def _infer_pain_points(self, category: str) -> List[str]:
        category_lower = category.lower()
        if "shirt" in category_lower or "t-shirt" in category_lower:
            return [
                "ordinary outfits look boring",
                "fabric may feel uncomfortable in hot weather",
                "buyers worry about fit and print quality"
            ]
        if "motor" in category_lower or "oil" in category_lower:
            return [
                "engine wear and poor protection",
                "fear of fake or low-quality oil",
                "lack of trust in performance claims"
            ]
        return [
            "unclear product value",
            "lack of trust before purchase",
            "need to see real usage effect quickly"
        ]

    def _suggest_angles(self, category: str, selling_points: List[str]) -> List[str]:
        base = [
            "problem-solution demonstration",
            "before-after comparison",
            "fast TikTok-style product showcase"
        ]
        if selling_points:
            base.append(f"highlight: {selling_points[0]}")
        return base
