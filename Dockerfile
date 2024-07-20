FROM python:3.10-slim

WORKDIR /app

COPY . /app

EXPOSE 8000  

RUN pip install --trusted-host pypi.python.org -r requirements.txt

# CMD ["python3", "main.py"]

CMD ["gunicorn", "-c", "gunicorn_conf.py", "main:app"]