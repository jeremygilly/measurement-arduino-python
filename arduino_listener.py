"""
ldr.py
Display analog data from Arduino using Python (matplotlib)
Author: Mahesh Venkitachalam
Website: electronut.in
"""

import sys, serial, argparse
import numpy as np
from time import sleep
from collections import deque
import itertools

import matplotlib.pyplot as plt 
import matplotlib.animation as animation
import datetime
output = "none"
count = 0
    
# plot class
class AnalogPlot:
  # constr
  def __init__(self, strPort, maxLen):
      # open serial port
      self.ser = serial.Serial(strPort, 9600)

      self.ax = deque([0.0]*maxLen)
      self.ay = deque([0.0]*maxLen)
      self.maxLen = maxLen

      global output_file
      output_file.write('yyyy-mm-dd hh:mm:ss' + ', ' + 'output' + '\n')

      

  # add to buffer
  def addToBuf(self, buf, val):
      if len(buf) < self.maxLen:
          buf.append(val)
          # print ('adding')
      else:
          buf.pop()
          buf.appendleft(val)
          # print ('appending right')

  # add data
  def add(self, data):
      assert(len(data) == 1)
      
      self.addToBuf(self.ax, data[0])
      global output 
      output = str(data[0])
      # self.outputFile(self, data[0])
      # self.addToBuf(self.ay, data[1])

  # update plot
  def update(self, frameNum, a0, a1):
      try:
          line = self.ser.readline()
          print(line)
          data = [float(val) for val in line.split()]
          # print data
          if(len(data) == 1):
              self.add(data)
              print(data)
              a0.set_data(range(self.maxLen), self.ax)
              now = str(datetime.datetime.now())
              global output_file
              output_file.write(now + ', ' + output + '\n')
      except KeyboardInterrupt:
          print('exiting')
      
      return a0

  # clean up
  def close(self):
      # close serial
      self.ser.flush()
      self.ser.close()    

# main() function
def main():
  now = datetime.datetime.now()
  write_to_file_path = str(now) + ".txt"
  global output_file
  output_file = open(write_to_file_path, "w+")
  
      
  
  # create parser
  parser = argparse.ArgumentParser(description="LDR serial")
  # add expected arguments
  parser.add_argument('--port', dest='port', required=True)

  # parse args
  args = parser.parse_args()
  
  #strPort = '/dev/tty.usbserial-A7006Yqh'
  strPort = args.port

  print('reading from serial port %s...' % strPort)

  # plot parameters
  analogPlot = AnalogPlot(strPort, 100)

  print('plotting data...')

  # set up animation
  fig = plt.figure()
  ax = plt.axes(xlim=(0, 100), ylim=(0, 400))
  a0, = ax.plot([], [])
  a1, = ax.plot([], [])
  plt.ylabel('Response (mV)')
  plt.xlabel('Samples')
  anim = animation.FuncAnimation(fig, analogPlot.update, 
                                 fargs=(a0, a1), 
                                 interval=5)
  
  # show plot
  plt.show()
  
  # clean up
  analogPlot.close()

  print('exiting.')
  

# call main
if __name__ == '__main__':
  main()