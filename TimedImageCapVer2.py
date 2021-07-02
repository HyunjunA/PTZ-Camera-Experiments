# encoding: UTF-8

# This code takes Infrared images.

import cv2 #sudo apt-get install python-opencv
import numpy as py
import os
import sys
import time
from datetime import datetime as dt
try:
    import picamera
    from picamera.array import PiRGBArray
except:
    sys.exit(0)

from Focuser import Focuser
from AutoFocus import AutoFocus
import curses
import pathlib



camera = picamera.PiCamera()

camera.resolution = (2500,1900)


mp=camera._camera.control.params[65536+5]
mp.value =10
camera._camera.control.params[65536+5]=mp

# Gets or sets the auto-white-balance gains of the camera.

# When queried, this attribute returns a tuple of values representing
# the `(red, blue)` balance of the camera. The `red` and `blue` values
# are returned :class:`~fractions.Fraction` instances. The values will
# be between 0.0 and 8.0.

# When set, this attribute adjusts the camera's auto-white-balance gains.
# The property can be specified as a single value in which case both red
# and blue gains will be adjusted equally, or as a `(red, blue)` tuple.
# Values can be specified as an :ref:`int <typesnumeric>`, :ref:`float
# <typesnumeric>` or :class:`~fractions.Fraction` and each gain must be
# between 0.0 and 8.0.  Typical values for the gains are between 0.9 and
# 1.9.  The property can be set while recordings or previews are in
# progress.



focuser = Focuser(1)


datetime_object = dt.now()
datetime_object=datetime_object.isoformat()
datetime_object = datetime_object.replace(":",".")
# pathlib.Path.cwd() == /home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/
# pathlib.Path.cwd() == /home/pi (by cron job)

# Take original image
camera.capture("/home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/Image_Original/image{}.jpg".format(datetime_object))
# camera.capture(str(pathlib.Path.cwd())+"/image{}.jpg".format(datetime_object))


# Open IR cut
focuser.set(Focuser.OPT_IRCUT,focuser.get(Focuser.OPT_IRCUT)^0x0001)

datetime_object = dt.now()
datetime_object=datetime_object.isoformat()
datetime_object = datetime_object.replace(":",".")

# Take IR image
camera.capture("/home/pi/Documents/PTZ-Camera-Controller/PTZ_IMX477_Controller/pyCode/Image_IR/image_IR{}.jpg".format(datetime_object))
# camera.capture(str(pathlib.Path.cwd())+"/image_IR{}.jpg".format(datetime_object))

# Close IR cut
focuser.set(Focuser.OPT_IRCUT,focuser.get(Focuser.OPT_IRCUT)^0x0001)
