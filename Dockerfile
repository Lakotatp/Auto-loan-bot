FROM langflowai/langflow:latest
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 7860
CMD ```
