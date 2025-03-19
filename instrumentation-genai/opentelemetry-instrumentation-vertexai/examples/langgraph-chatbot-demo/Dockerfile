FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim AS build
RUN apt update && apt install -y git curl
WORKDIR /build
ARG GIT_REF
#ENV SCRIPT_URL="https://raw.githubusercontent.com/aabmass/opentelemetry-python-contrib/${GIT_REF?must be set to a git commit}/instrumentation-genai/opentelemetry-instrumentation-vertexai/examples/langgraph-chatbot-demo/run_streamlit.py"
#ENV SCRIPT_URL="https://raw.githubusercontent.com/aabmass/opentelemetry-python-contrib/refs/heads/vertex-langgraph/instrumentation-genai/opentelemetry-instrumentation-vertexai/examples/langgraph-chatbot-demo/run_streamlit.py"
#ENV SCRIPT_URL="run_streamlit.py"
# Creates the virtualenv
#RUN curl -LO "${SCRIPT_URL}" && curl -LO "${SCRIPT_URL}.lock"
COPY . .
RUN VIRTUAL_ENV=./venv uv sync --active --frozen --script run_streamlit.py
RUN VIRTUAL_ENV=./venv uv pip install "google-cloud-alloydb-connector[pg8000]" opentelemetry-instrumentation-sqlalchemy
COPY src /build/
COPY *.py /build/

FROM python:3.13-slim
WORKDIR /build
COPY --from=build /build/ .
ENV PATH="/build/venv/bin:$PATH"
ENTRYPOINT ["python", "run_streamlit_local.py"]
