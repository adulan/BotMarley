FROM python:3.11.4-alpine3.17

LABEL org.opencontainers.image.source=https://github.com/adulan/BotMarley
LABEL org.opencontainers.image.description="BotMarley Docker Image"
LABEL org.opencontainers.image.licenses=MIT

WORKDIR /usr/src/app
RUN chmod -R 775 /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python3", "./src/ride_natty_ride.py" ]