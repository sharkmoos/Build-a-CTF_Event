FROM ubuntu:latest

RUN apt update && apt install -y python3 sqlite3 python3-pip sudo openssh-client 

RUN useradd -rm -d /home/intern -s /bin/bash -u 3232 intern \
    && echo 'intern:my_wifes_birthday' | chpasswd \
    && useradd -rm -d /home/manager -s /bin/bash -u 3233 manager \
    && echo 'manager:s3cret_passw0rd' | chpasswd \
    && echo 'root:date_of_birth' | chpasswd 

RUN pip3 install flask gunicorn requests pycryptodome cryptography flask_sqlalchemy PyJWT

COPY templates/ /home/intern/templates/
COPY static/ /home/intern/static/

COPY source.c runme research.txt user.txt /home/manager/
COPY main.py create_db.py runapp.sh /home/intern/
COPY root.txt /root/root.txt

RUN chmod +x /home/intern/runapp.sh  \
    && chown manager /home/manager/runme \
    && chown manager /usr/bin/find \
    && sudo -u manager chmod +s /usr/bin/find \
    && chmod +s /home/manager/runme \
    && chmod 400 /home/manager/user.txt \
    && chmod 400 /root/root.txt

EXPOSE 5000

ENTRYPOINT ["./home/intern/runapp.sh"]
