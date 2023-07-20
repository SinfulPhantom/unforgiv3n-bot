FROM python:3.10
WORKDIR /unforgiv3n-bot
COPY requirements.txt /unforgiv3n-bot/
RUN pip install -r requirements.txt
COPY . /unforgiv3n-bot
CMD python main.py