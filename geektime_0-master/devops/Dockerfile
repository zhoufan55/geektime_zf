FROM hub.ceshiren.com/ceba/tech/devops/ceba-base-image-dev:v2

COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3","geektime_0/platform/server.py", "--port=5000"]
