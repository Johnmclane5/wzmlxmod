FROM itsherchoice/wzmlxmod:latest
WORKDIR /usr/src/app
COPY . .
CMD ["bash", "start.sh"]
