from typing import Dict, Any
from datetime import datetime
from .base_agent import BaseAgent


class ReportAgent(BaseAgent):
    name = "Report Agent"

    def run(self, context: Dict[str, Any]) -> Dict[str, Any]:
        product = context["product"]
        prompts = context["video_prompts"]

        result = {
            "generated_at": datetime.now().isoformat(timespec="seconds"),
            "project_summary": f"Generated a complete short-video production plan for {product.get('product_name')}.",
            "recommended_model": prompts["model_recommendation"],
            "estimated_workflow": [
                "Collect product image and basic selling points",
                "Generate script and 3-part storyboard",
                "Generate video prompt with selected model",
                "Review output using quality scorecard",
                "Record failure reasons and reusable template"
            ],
            "cost_control_suggestions": [
                "Use low-cost model for first-round visual testing.",
                "Use premium model only after script and product angle are confirmed.",
                "Reuse stable prompts by category to reduce trial-and-error.",
                "Avoid complex interaction scenes unless required by the product."
            ],
            "team_management_notes": [
                "Assign one person to collect product information.",
                "Assign one person to generate and test prompts.",
                "Assign one person to review video output and record quality issues.",
                "Review reusable templates weekly."
            ]
        }

        context["report"] = result
        return context
