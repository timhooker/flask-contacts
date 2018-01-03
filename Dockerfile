FROM python:3.6-jessie
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN npm install
RUN npm run build
ENTRYPOINT ["sh", "./entrypoint.sh"]

CMD ["python", "app.py"]