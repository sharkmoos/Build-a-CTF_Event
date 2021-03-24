#!/bin/bash
gcc /home/manager/source.c -o /home/manager/runme 
chown manager /home/manager/runmme 
sudo -u manager chmod +s /home/manager/runme 
sudo -u intern python3 /home/intern/create_db.py
sudo -u intern python3 /home/intern/main.py
