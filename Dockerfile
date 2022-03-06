# Using Python Slim-Buster
FROM kyyex/kyy-userbot:buster
#━━━━━ Userbot Telegram ━━━━━
#━━━━━ By Flicks-Userbot ━━━━━

RUN git clone -b Flicks-Userbot https://github.com/fjgaming212/Flicks-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

RUN curl -sL https://deb.nodesource.com/setup_16.x | bash -
RUN apt-get install -y nodejs
RUN apt-get update && apt-get upgrade -y
RUN apt-get install ffmpeg -y

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/fjgaming212/Flicks-Userbot/Flicks-Userbot/requirements.txt

EXPOSE 80 443

# Finalization
CMD ["python3", "-m", "userbot"]
