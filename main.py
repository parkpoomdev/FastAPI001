import string
from fastapi import FastAPI, Request
from pydantic import BaseModel

app = FastAPI()

class Msg(BaseModel):
    msg: str

@app.get("/")
async def root():
    return {"message": "Hello World. Welcome to FastAPI!"}

@app.get("/path")
async def demo_get():
    return {"message": "This is /path endpoint, use a post request to transform the text to uppercase"}

# 1
# get accelerometer data time_stamp, x, y, z
# curl 'http://127.0.0.1:8000/accelerometer/12sdf/2.1/2.2/2.33'
@app.get("/accelerometer/{time_stamp}/{x}/{y}/{z}")
async def get_accelerometer(time_stamp: str, x: float, y: float, z: float):
    return {"Accelerometer": f"timestamp - {time_stamp} x-> {x} y-> {y} z-> {z} "}

# 2
# get barometer data time_stamp, br
# curl 'http://127.0.0.1:8000/barometer/12-23-2323.1123/0.111'
@app.get("/barometer/{time_stamp}/{br}")
async def get_barometer(time_stamp: str, br: float):
    return {"barometer": f"timestamp - {time_stamp} br-> {br}"}

# 3
# get Gyroscope data time_stamp,x ,y ,z
# curl 'http://127.0.0.1:8000/gyroscope/12-23-23223/0.111/0.12/3.4'
# curl 'http://127.0.0.1:8000/gyroscope/?timestamp=06/01/18 00:11:00&gyroX=3.1&gyroY=3.2&gyroZ=3.3'
@app.get("/gyroscope/{time_stamp}/{gyroX}/{gyroY}/{gyroZ}")
async def get_gyroscope(time_stamp: str, gyroX: float, gyroY: float, gyroZ: float):
    return {"gyroscope": f"timestamp - {time_stamp} gyroX-> {gyroX} gyroY-> {gyroY} gyroZ-> {gyroZ}" }

# 4
# curl 'http://127.0.0.1:8000/HeartRateSensor/09-23-19T11%3A41%3A27/98'
# https://community.smartbear.com/t5/ReadyAPI-Questions/Colon-is-being-sent-as-ascii-3A-in-HTTP-Request/td-p/191305
@app.get("/HeartRateSensor/{time_stamp}/{hrm}")
async def get_HeartRateSensor(time_stamp: str, hrm: float):
    return {"HeartRateSensor": f"timestamp - {time_stamp} hrm-> {hrm}" }

# 5
# curl 'http://127.0.0.1:8000/OrientationSensor/09-23-19T11%3A41%3A27/0.2/0.2/0.3/0.4'
@app.get("/OrientationSensor/{time_stamp}/{OrientationSensor1}/{OrientationSensor2}/{OrientationSensor3}/{OrientationSensor4}")
async def get_OrientationSensor(time_stamp: str, OrientationSensor1: float, OrientationSensor2: float, OrientationSensor3: float, OrientationSensor4: float):
    return {"OrientationSensor": f"timestamp - {time_stamp} OrientationSensor1-> {OrientationSensor1} OrientationSensor2-> {OrientationSensor2} OrientationSensor3-> {OrientationSensor3} OrientationSensor4-> {OrientationSensor4}" }

@app.post("/path")
async def demo_post(inp: Msg):
    return {"message": inp.msg.upper()}

@app.get("/path/{path_id}")
async def demo_get_path_id(path_id: int):
    return {"message": f"This is /path/{path_id} endpoint, use post request to retrieve result"}