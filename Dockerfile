FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
#COPY requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip3 install uvicorn
RUN pip3 install fastapi
RUN pip3 install fastapi_sqlalchemy
RUN pip3 install python-dotenv
RUN pip3 install psycopg2
RUN pip3 install alembic
RUN pip3 install python-multipart
RUN pip3 install "passlib[bcrypt]"
RUN pip3 install pyjwt
#RUN pip3 install -r requirements.txt
COPY . /app
EXPOSE 8001