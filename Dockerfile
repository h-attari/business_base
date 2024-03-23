FROM python:3.9-alpine

WORKDIR /business_base

COPY ./requirements.txt /business_base/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /business_base/requirements.txt

COPY ./app /business_base/app

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
