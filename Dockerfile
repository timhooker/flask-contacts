FROM python:3.6-jessie
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -
RUN apt-get install -y nodejs
RUN curl -o- -L https://yarnpkg.com/install.sh | bash
ENTRYPOINT ["sh", "./entrypoint.sh"]