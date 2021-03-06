# measurement-arduino-python
A replacement for the National Instruments datalogger and Signal Express with laptop. It uses an Arduino with Python for graphing instead. The following instructions are for Windows only. However, every command has its analog with Mac (also tested), and likely Linux.

# System requirements
1. Arduino IDE. Can be found at https://www.arduino.cc/en/Main/Software  
  I recommend the offline version for better stability.   
  This file also requires the Statistic library to be installed. It may already be installed with Arduino, but if not, further information (and the download link from GitHub) can be found here: https://playground.arduino.cc/Main/Statistics<br />

2. Python 2.7.13. Can be found at https://www.python.org/downloads/release/python-2713/  
  Why Python 2? It is backwards compatible with a bunch of operating systems (including Windows XP).  
  Dependencies: import sys, serial, argparse, numpy, sleep, deque, itertools, matplotlib, datetime.  
  Most of these should already be included. If not, they are pretty easy to install.  
  a) To install serial, download pyserial from: https://pypi.python.org/pypi/pyserial/2.7 - I recommend pyserial 2.7 (for compatibility with Windows XP).  
  b) You may need to change the file path, similar to here: https://www.youtube.com/watch?v=byBW30oIRPU or use the setx PATH command (https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command).  
  c) You may want to install pip (usually pre-installed, but may require a change in file path) and wheel ('pip install wheel' into command prompt).  
  d) Use pip to install wheel file. I found this to be helpful: https://www.webucator.com/blog/2015/03/installing-the-windows-64-bit-version-of-pygame/  
  e) Install numpy: <code>pip install numpy</code>
  f) Install matplotlib: <code>pip install matplotlib</code>
  
# Use
0. Connect sensor as shown in the following diagram (note the resistor is the sensor).
![alt text](https://github.com/jeremygilly/measurement-arduino-python/blob/master/GaN%20Circuit%20layout.png)
1. Connect Arduino, turn on device, and run program.<br />
2. Identify the USB port connected to the Arduino through the command line<br />
Windows: <code>mode</code><br />
Mac: <code>ls /dev/tty.*</code><br />
Find the correct port.<br />
In command line when calling the python program, first navigate to the folder where the program is using <code>cd</code><br />
Then, use: <code>python arduino_listener.py --port [your chosen port]</code><br />
A chosen port on Mac OS X may be /dev/tty.usbmodem1411<br />
A chosen port on Windows XP may be COM9, e.g. <code>python arduino_listener.py --port COM9</code><br />
You may need to install/update hardware peripheral drivers for this to work. You can find further information here: https://www.arduino.cc/en/Guide/ArduinoUno#toc2
  
# Output
The data is output to the same folder the python file is saved in. I recommend saving to the Desktop. <br />
It is a .txt file labelled with the first reading taken.<br />
