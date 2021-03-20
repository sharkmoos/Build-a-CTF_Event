#!/bin/bash
sudo -u manager chmod o+s /usr/bin/cp
sudo -u intern python3 /home/intern/create_db.py
sudo -u intern python3 /home/intern/main.py
