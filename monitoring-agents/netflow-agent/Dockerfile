FROM python:3.9-slim
WORKDIR /app
COPY collector.conf /app/collector.conf
# placeholder: install real collector (nfdump/nfcollector) in production
EXPOSE 9600/udp
CMD ["sh", "-c", "python -m http.server 9600"] 
