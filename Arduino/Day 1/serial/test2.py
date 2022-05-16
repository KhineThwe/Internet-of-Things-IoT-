try:
 from flask import Flask
 from flask_restful import Resource,Api
 from flask_restful import reqparse
 from flask import request
 import time
 import datetime
 import json
 import Adafruit_DHT
 print("All modules loaded")
except Exception as e:
 print("Error:{}".format(e))
app=Flask(__name__)
api=Api(app)

pin=4
sensor=Adafruit_DHT.DHT11

class Temperature(Resource)
  def __init__(self):
      pass
  def get(self):
      print("checking Temperature")
      humidity,temperature=Adafruit_DHT.read_retry(sensor,pin)
      if humidity is not None and temperature is not None:
          return{
              'Temperature':temperature,
              'humidity':humidity
          }
api.add_resource(Temperature,"/")
if __name__ == "__main__":
    app.run(host='0.0.0.0')