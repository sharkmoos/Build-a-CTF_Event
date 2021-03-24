#!/bin/bash
gcc /home/manager/source.c -o runme 
chown manager /home/manager/runmme 
sudo -u intern python3 /home/intern/create_db.py
sudo -u intern python3 /home/intern/main.py
