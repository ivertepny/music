FROM python:3.13

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY ./backend /app

CMD ["gunicorn", "shop.wsgi:application", "--bind", "0.0.0.0:8000"]
