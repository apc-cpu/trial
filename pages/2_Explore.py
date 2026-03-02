import streamlit as st
from utils.io import load_weather
from charts.charts import (chart_dashboard, chart_interactive_seasonal_heatmap)

st.set_page_config(page_title="Explore", layout="wide")
df = load_weather()

st.title("Interactive Exploratory View")
st.write("Use interaction to validate and extend the story—focus on one weather type, then zoom into a time window.")
st.altair_chart(chart_dashboard(df), use_container_width=True)


st.markdown("**Guided prompts:**")
st.write("Q: Filter to one weather type (e.g., `sun`, `rain`)—does the temperature distribution shift? A: Yes, temperature distrbution can shift across weather types")
st.write("Q: Brush a specific year—do extremes cluster in particular periods? A: Extreme highs are usually clustered in summer months for metrics such as sun or fog.")
st.write("Q: Compare histogram shape across weather types—what changes most: center, spread, or tails? A: Spread does not change that much (except for snow). However, I would say center probably changes the most across different metrics.")




st.title("Seasonal Temperature Patterns")
st.write("Hover over the heatmap to highlight a specific day across all years.")
st.altair_chart(chart_interactive_seasonal_heatmap(df), use_container_width=True)
