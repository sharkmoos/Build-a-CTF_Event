FROM ubuntu:latest

RUN apt update && apt install -y python3 sqlite3 python3-pip sudo openssh-client 

RUN useradd -rm -d /home/intern -s /bin/bash -u 3232 intern \
    && echo 'intern:my_wifes_birthday' | chpasswd \
    && useradd -rm -d /home/manager -s /bin/bash -u 3233 manager \
    && echo 'manager:s3cret_passw0rd' | chpasswd \
    && echo 'root:date_of_birth' | chpasswd \

RUN pip3 install flask gunicorn requests pycryptodome cryptography flask_sqlalchemy PyJWT

COPY templates/ /home/flask/templates/
COPY static/ /home/flask/static/

COPY admin/ home/flask/admin/

copy source.c runme research.txt managerflag.txt /home/manager/
COPY main.py create_db.py runapp.sh /home/flask/
COPY rootflag.txt /home/root

RUN chmod +x /home/flask/runapp.sh  \
    && ./home/flask/create_db.py \
    && chown manager /home/manager/runme \
    && chown manager /usr/bin/cp \
    && sudo -u manager chmod +s /usr/bin/cp \
    && chmod +s /home/manager/runme \
    && chmod 400 /home/manager/managerflag.txt \
    && RUN chmod 400 /home/root/rootflag.txt

EXPOSE 5000

ENTRYPOINT ["./home/flask/runapp.sh"]
