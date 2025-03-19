# /// script
# requires-python = ">=3.13"
# dependencies = [
#  "google-cloud-alloydb-connector>=1.7.0",
#  "langgraph-chatbot-demo",
# ]
#
# [tool.uv.sources]
# langgraph-chatbot-demo = { git = "https://github.com/aabmass/opentelemetry-python-contrib.git", subdirectory = "instrumentation-genai/opentelemetry-instrumentation-vertexai/examples/langgraph-chatbot-demo", branch = "vertex-langgraph" }
#
# ///

from langgraph_chatbot_demo.run_streamlit import run_streamlit

run_streamlit()
