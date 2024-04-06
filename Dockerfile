# First stage
FROM python:3.11 as builder
COPY --link . .
RUN apt-get update && apt-get install -y \
    python3 \
    pip
RUN pip install -r requirements.txt

# Second stage
FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder ./src ./src
ENV PYTHONUNBUFFERED=1
RUN useradd -m -u 1000 user
USER user
EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "--fail", "http://localhost:8501/_stcore/health" ]
ENTRYPOINT [ "python3", "-m", "streamlit", "run", "/src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0" ]