# Intro session

A simple introduction to the basics of Python + attempting to build our own database and seeing some of the challenges.

## Getting your python env started:

1) Install python 3.10 or 3.11
2) Install pip for your python environment
3) Install venv using pip ```python3.10 -m pip install venv```
4) To create a venv ```python3.10 -m venv my_venv```
5) Enter the venv ```source my_venv/bin/activate```
6) Install dependencies (I have tornado here but unused) ```pip install -r requirements.txt```
7) Now your terminal is setup for python development! I highly recommend configuring your .bashrc or .zshrc to display both your venv and git branch

## Getting setup with pycharm
1) Scroll down for the community version https://www.jetbrains.com/pycharm/download/
2) Either import or create a new project. Select your python virtual environment
3) Configure your run configurations to run the main.py file, or use the defaults

## Environment stuff for next week
1) Install docker
2) Create a docker container running postgres. https://www.docker.com/blog/how-to-use-the-postgres-docker-official-image/
3) Install psql (postgres client)
4) Install a gui db client (https://tableplus.com/blog/2018/10/dbeaver-postico-vs-tableplus.html). I use tableplus, but the free version sucks.
5) Connect to your docker db using psql. Run ```create database test```
6) Together we will make a simple schema/data and populate it.