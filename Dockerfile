FROM python:3-alpine
RUN mkdir /app
ADD app.py /app/
ENTRYPOINT ["/app/app.py"]
