
# back.py
# (c) 2019 fieldcloud SAS. all rights reserved
# VERSION:
# DATE: 14/10/2020
# AUTHOR: mds@fieldcloud.com,mnayebare@fieldcloud.com
# back-end api file for the website

from flask import Flask
from flask import Flask,request, json, jsonify
from flask_cors import CORS
import requests
import smtplib, ssl
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])
def index():
    return("ivory coast iot-training api") 
    
#send sms
@app.route("/sms/", methods=['GET'])
def post_data_from_provider():
    resp = requests.post('https://textbelt.com/text', {
    'phone': '+250782330752',
    'message': 'Hello world',
    'key': 'textbelt',
    
    })
    return jsonify("status")

#send email 
@app.route("/email", methods=['POST'])
def sendEmail():
    data = request.get_json()
    temp = data['data']['temp'] 
    s = smtplib.SMTP('smtp.gmail.com', 587)   
    s.starttls()   
    s.login("iotivorycoast@gmail.com", "p@#!iVvfNg3pTRh4ts")

    msg = MIMEMultipart()
    msg['From']="iotivorycoast@gmail.com"
    msg['To']=data['data']['email']
    msg['Subject']="Alerte de capteur "
    message= "La température a atteint le bon seuil de " + str(temp)  +  "degrés" 
    msg.attach(MIMEText(message, 'plain'))
    if  s.send_message(msg) is None:
         return(jsonify({'Error':'Error sending'}), 400) 
    else:
        return(jsonify({'Success':'Email sent'}), 200) 
    s.quit() 

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
