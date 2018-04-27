# PineAppleTeamWebSci
https://github.com/marteo2/PineAppleTeamWebSci

Spring 2018 Web Science project repo

The application we propose to create is a website that allows a user to track and observe trends in BTC prices in various markets. The website will show updated BTC prices in comparable markets as well as showing a history of price changes in each market through a graphical/visual aid such as a line graph. 


Bug Track server Link: <http://test.worldpara.com>


# Installation

#### Prerequisite
1. Make sure you have python 3.6 or higher
2. Install pip3 (use pip --version to make sure the version of pip)
3. Install MongoDB 3.4 or higher
4. Make sure crontab is working

##### If you want to use virtual environment
Install virtualenv via pip

    pip install virtualenv
    cd PineAppleTeamWebSci

To begin using the virtual environment, it needs to be activated:

    source virtualEnv/bin/activate

If you are done working in the virtual environment for the moment, you can deactivate it:

    deactivate

#### Dependency

     pip install -r requirements.txt
Use this command to install all required packages

# Run

    python manage.py runserver 127.0.0.1:8000
The server will run on http://127.0.0.1:8000/btcdata

## Pull Data
    python manage.py crontab add
Add data collection service to your server

    python manage.py crontab remove // remove the service
## API

    http://127.0.0.1:8000/api/start_time/end_start

##### Example

    http://www.worldpara.com:9000/api/1524693338584/1524693858584
Both should be timestamp

## Send Email

    python manage.py send_email
This command will send email to all user in Email Collections
