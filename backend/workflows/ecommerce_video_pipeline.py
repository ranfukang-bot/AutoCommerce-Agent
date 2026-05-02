from typing import Dict, Any

from backend.agents.product_insight_agent import ProductInsightAgent
from backend.agents.viral_script_agent import ViralScriptAnalysisAgent
from backend.agents.video_prompt_agent import VideoPromptAgent
from backend.agents.quality_review_agent import QualityReviewAgent
from backend.agents.report_agent import ReportAgent


class EcommerceVideoPipeline:
    def __init__(self):
        self.agents = [
            ProductInsightAgent(),
            ViralScriptAnalysisAgent(),
            VideoPromptAgent(),
            QualityReviewAgent(),
            ReportAgent(),
        ]

    def run(self, product: Dict[str, Any]) -> Dict[str, Any]:
        context: Dict[str, Any] = {"product": product}
        for agent in self.agents:
            context = agent.run(context)
        return context
