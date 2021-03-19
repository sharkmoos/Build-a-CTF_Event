FROM ubuntu:latest

RUN apt update && apt install -y python3 sqlite3 python3-pip sudo openssh-client

RUN useradd -rm -d /home/flask -s /bin/bash -u 3232 flask \
    && echo 'flask:login' | chpasswd 

RUN pip3 install flask gunicorn requests pycryptodome cryptography flask_sqlalchemy PyJWT

COPY templates/ /home/flask/templates/

COPY static/ /home/flask/static/

COPY main.py create_db.py runapp.sh /home/flask/

RUN chmod +x /home/flask/runapp.sh 

EXPOSE 5000

ENTRYPOINT ["./home/flask/runapp.sh"]