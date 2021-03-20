#!/bin/bash
sudo -u manager chmod o+s /usr/bin/find
sudo -u intern python3 /home/intern/create_db.py
sudo -u intern python3 /home/intern/main.py
