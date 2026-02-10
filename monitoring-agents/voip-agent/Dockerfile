FROM python:3.9-slim
WORKDIR /app
COPY voip_exporter.yml /app/voip_exporter.yml
EXPOSE 9700
CMD ["sh", "-c", "python -m http.server 9700"]
