# First stage
FROM python:3.11 as builder
COPY --link . .
RUN apt-get update
RUN apt-get install -y python3 pip
RUN pip install -r requirements.txt

# Second stage
FROM python:3.11-slim
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder ./src ./src
ENV PYTHONUNBUFFERED=1
RUN useradd -m -u 1000 user
USER user
CMD ["python3", "/src/app.py"]