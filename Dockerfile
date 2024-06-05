FROM python:3.10

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt && \
    mkdir logs


COPY . .

ENTRYPOINT ["python", "main.py"]

CMD ["-c", "JPY", "-i", "3s"]