FROM python:3-alpine
RUN mkdir /app
ADD app.py /app/
CMD ["sh","-c","python3 /app/app.py"]
