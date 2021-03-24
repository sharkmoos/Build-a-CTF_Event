FROM ubuntu:latest

RUN apt update && apt install -y python3 sqlite3 python3-pip sudo openssh-client --no-install-recommeds

RUN useradd -rm -d /home/intern -s /bin/bash -u 3232 intern \
    && echo 'intern:my_wifes_birthday' | chpasswd \
    && groupadd rootish \
    && useradd -rm -d /home/manager -s /bin/bash -u 3233 -G rootish manager  \
    && echo 'manager:s3cret_passw0rd' | chpasswd \
    && echo 'root:3esr34534rfsawtw' | chpasswd 

RUN pip3 install flask gunicorn requests pycryptodome cryptography flask_sqlalchemy PyJWT

COPY templates/ /home/intern/templates/
COPY static/ /home/intern/static/

COPY source.c research.txt user.txt /home/manager/
COPY main.py create_db.py runapp.sh /home/intern/
COPY root.txt /root/root.txt

RUN chmod +x /home/intern/runapp.sh  \
    && gcc /home/manager/source.c -o runme \
    && chown manager /home/manager/runmme \
    && chown manager /usr/bin/cp \
    && sudo -u manager chmod +s /usr/bin/cp \
    && chmod +s /home/manager/runme \
    && chmod 644 /etc/shadow \
    && chgrp rootish /etc/shadow \
    && chmod 400 /home/manager/user.txt \
    && chmod 400 /root/root.txt 

EXPOSE 5000

ENTRYPOINT ["./home/intern/runapp.sh"]
