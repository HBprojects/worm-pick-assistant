#!/usr/bin/python3

# How to do digital zoom using the "ScalerCrop" control.

import time
import libcamera
from picamera2 import Picamera2
from picamera2.encoders import H264Encoder
from picamera2 import Picamera2, Preview


preview_resolution = (1280, 960)  # 4:3 aspect ratio
picam2 = Picamera2()
config = picam2.create_video_configuration(main={"size": (1332,990)}, controls={"FrameDurationLimits": (16666,16666)})
                                           
picam2.configure(config)

encoder = H264Encoder(framerate=60)
filname = "video60.h264"

#picam2.set_controls({"Framerate": 60})
picam2.start_preview(Preview.QTGL)
picam2.start_recording(encoder=encoder,output=filname)
time.sleep(20)
picam2.stop_recording()
picam2.stop()
