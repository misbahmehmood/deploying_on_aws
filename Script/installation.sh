#!/usr/bin/env bash
 
sudo apt update -y
 
sudo apt install python3 -y
 
sudo apt install python3-pip -y
 
sudo apt install python3-venv -y
 
python3 -m venv venv
 
source ~/.bashrc
 
source /var/lib/jenkins/workspace/flask_project/venv/bin/activate
 
cd /var/lib/jenkins/workspace/flask_project
 
pip3 install -r requirements.txt
 
pytest --cov ./application
 
python3 app.py