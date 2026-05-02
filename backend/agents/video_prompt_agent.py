from typing import Dict, Any, List
from .base_agent import BaseAgent


class VideoPromptAgent(BaseAgent):
    name = "Video Prompt Agent"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        product = context["product"]
        script = context["viral_script"]
        category = product.get("category", "")

        risk = self._risk_profile(category)

        result = {
            "model_recommendation": self._recommend_model(product),
            "risk_profile": risk,
            "veo_prompt": self._build_veo_prompt(product, script),
            "seedance_prompt": self._build_seedance_prompt(product, script),
            "wan_prompt": self._build_wan_prompt(product, script),
            "cover_image_prompt": self._build_cover_prompt(product),
        }

        context["video_prompts"] = result
        return context

    def _recommend_model(self, product: Dict[str, Any]) -> Dict[str, str]:
        preferred = product.get("model_preference", "VEO")
        category = product.get("category", "").lower()
        if "shirt" in category or "fashion" in category:
            return {
                "primary": preferred,
                "reason": "Fashion and outfit display are suitable for light motion, model posing, fabric detail, and lifestyle scenes."
            }
        return {
            "primary": preferred,
            "reason": "Use controlled product display scenes. Avoid complex assembly, tearing, pouring, or precise hand interactions."
        }

    def _risk_profile(self, category: str) -> List[str]:
        category_lower = category.lower()
        if "shirt" in category_lower:
            return [
                "print deformation during body movement",
                "hand/finger distortion when adjusting clothes",
                "unrealistic fabric fold if motion is too large"
            ]
        return [
            "object deformation under complex interaction",
            "inconsistent scale between hand and product",
            "unclear product identity if shot changes too fast"
        ]

    def _build_veo_prompt(self, product: Dict[str, Any], script: Dict[str, Any]) -> str:
        return f"""
Vertical 9:16 TikTok commercial video. Product: {product.get('product_name')}.
Category: {product.get('category')}. Target market: {product.get('target_market')}.
Scene: realistic lifestyle environment, clean background, natural lighting.
Action: light, controlled movement that clearly shows the product. Avoid complex hand-object interaction.
Visual focus: {", ".join(product.get("selling_points", []))}.
Structure: 0-3s strong hook, 3-8s product value demonstration, 8-15s lifestyle close-up and purchase impulse.
Camera: stable handheld feel, smooth push-in, clear close-up details.
Style: realistic, high-quality commercial, no distorted text, no extra logos, no watermark.
""".strip()

    def _build_seedance_prompt(self, product: Dict[str, Any], script: Dict[str, Any]) -> str:
        return f"""
9:16 short product video for TikTok. Show {product.get('product_name')} in a realistic scene.
Fast opening shot, strong product focus, clear benefit demonstration.
Use medium shot and close-up shot alternation. Keep movement simple and natural.
Emphasize: {", ".join(product.get("selling_points", []))}.
Commercial style, realistic human motion, clean composition, no visual glitches, no extra text.
""".strip()

    def _build_wan_prompt(self, product: Dict[str, Any], script: Dict[str, Any]) -> str:
        return f"""
A realistic vertical short video, product showcase of {product.get('product_name')}.
Simple camera movement, stable product shape, no fast cuts, no complex interaction.
Highlight the product's most visible feature. High clarity, clean lighting, commercial product video style.
""".strip()

    def _build_cover_prompt(self, product: Dict[str, Any]) -> str:
        return f"""
A high-impact TikTok e-commerce cover image for {product.get('product_name')}.
Large product hero shot, premium lighting, clean background, bold visual contrast,
clear selling point layout, modern commercial design, sharp details, high conversion style.
""".strip()
