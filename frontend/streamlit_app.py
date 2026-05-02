import json
from pathlib import Path
import sys

import streamlit as st

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.workflows.ecommerce_video_pipeline import EcommerceVideoPipeline


st.set_page_config(
    page_title="AutoCommerce-Agent",
    page_icon="🎬",
    layout="wide"
)

st.title("AutoCommerce-Agent")
st.caption("Agentic workflow for cross-border e-commerce short video production.")

with st.sidebar:
    st.header("Product Input")
    product_name = st.text_input("Product Name", "Oversized Graphic T-Shirt")
    category = st.text_input("Category", "T-Shirt")
    target_market = st.selectbox("Target Market", ["Indonesia", "Philippines", "Thailand", "Vietnam", "Global"])
    model_preference = st.selectbox("Preferred Video Model", ["VEO", "Seedance", "WAN"])
    price_positioning = st.text_input("Price Positioning", "affordable daily wear")
    selling_points_text = st.text_area(
        "Selling Points",
        "oversized fit\nsoft cotton fabric\nstreetwear graphic print"
    )
    notes = st.text_area("Notes", "Use realistic model movement and avoid exaggerated interaction.")

run_btn = st.button("Generate Production Plan", type="primary")

if run_btn:
    product = {
        "product_name": product_name,
        "category": category,
        "target_market": target_market,
        "selling_points": [x.strip() for x in selling_points_text.splitlines() if x.strip()],
        "model_preference": model_preference,
        "price_positioning": price_positioning,
        "notes": notes,
    }

    pipeline = EcommerceVideoPipeline()
    result = pipeline.run(product)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Product Insight")
        st.json(result["product_insight"])

        st.subheader("Viral Script")
        st.json(result["viral_script"])

    with col2:
        st.subheader("Model Recommendation")
        st.json(result["video_prompts"]["model_recommendation"])

        st.subheader("Risk Profile")
        st.write(result["video_prompts"]["risk_profile"])

    st.subheader("VEO Prompt")
    st.code(result["video_prompts"]["veo_prompt"], language="text")

    st.subheader("Seedance Prompt")
    st.code(result["video_prompts"]["seedance_prompt"], language="text")

    st.subheader("WAN Prompt")
    st.code(result["video_prompts"]["wan_prompt"], language="text")

    st.subheader("Quality Review Scorecard")
    st.table(result["quality_review"]["scorecard"])

    st.subheader("Report")
    st.json(result["report"])

    st.download_button(
        "Download JSON Result",
        data=json.dumps(result, ensure_ascii=False, indent=2),
        file_name="autocommerce_agent_output.json",
        mime="application/json"
    )
else:
    st.info("Fill in product information in the sidebar, then click Generate Production Plan.")
