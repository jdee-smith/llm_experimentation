FROM ubuntu:latest
COPY --link . .
RUN apt-get update && apt-get install -y \
    python3 \
    pip
RUN pip install -r requirements.txt
RUN mkdir /db && chmod -R a+rwx /db
ENV PYTHONUNBUFFERED=1
RUN useradd -m -u 1000 user
USER user
EXPOSE 8501
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD [ "curl", "--fail", "http://localhost:8501/_stcore/health" ]