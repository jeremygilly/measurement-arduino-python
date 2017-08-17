# measurement-arduino-python
A replacement for the National Instruments datalogger and Signal Express with laptop. It uses an Arduino with Python for graphing instead.

# System requirements
1. Arduino IDE. Can be found at https://www.arduino.cc/en/Main/Software
  I recommend the offline version for better stability.
  This file also requires the Statistic library to be installed. It may already be installed with Arduino, but if not, further information (and the download link from GitHub) can be found here: https://playground.arduino.cc/Main/Statistics

2. Python 2.7.13. Can be found at https://www.python.org/downloads/release/python-2713/
  Why Python 2? It is backwards compatible with a bunch of operating systems (including Windows XP). 
  Dependencies: import sys, serial, argparse, numpy, sleep, deque, itertools, matplotlib, datetime.
  Most of these should already be included. If not, they are pretty easy to install.
  
# Output
The data is output to the same folder the python file is saved in. I recommend Desktop. 
It is a .txt file labelled with the first reading taken.
