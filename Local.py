# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 2019 

@author: mlgkschm (Ken Schmahl)
"""

from copy import copy
import json as js
from os.path import basename
from os.path import dirname
from os import getcwd
# The next module comes from pywin32: 'pip install pywin32'
import win32gui as gui

#############################################################################
#############################################################################
# Windows constants
# (cannot find these in win32com, though it is said they are there
xlTop = -4160
xlCenter = -4108
xlAbove = 0
xlContinuous = 1
xlEdgeBottom = 9
xlEdgeLeft = 7
xlEdgeRight = 10
xlEdgeTop = 8
xlInsideHorizontal = 12
xlInsideVertical = 11

##############################################################################
##############################################################################
# useful functions
def defined(var):
    return(var != None)

##############################################################################
def atoi(text):
    return int(text) if text.isdigit() else text

##############################################################################
def deepcopy(obj):
  return(
    js.loads(js.dumps(obj))
  )

#############################################################################
def mkType(t_name='C'):  # Make a type to be used as a dict
    return(type(t_name, (object,), {}))

##############################################################################
def readFile(fname):
    #print('Filename',fname)
    with open(fname, 'r') as f:
        s = f.read()
    return(s)

#############################################################################
def getFilename(filter=None):
  cwd = getcwd()
  #print('CWD: ',cwd); exit(1)

  if not defined(filter):
    filter = 'All: *.*\0*.*\0'

  boxDialog = gui.GetOpenFileNameW(None,None,filter,None,1,None,1024,cwd)
  #print('DialogBox output: ',boxDialog)
  file = list(boxDialog)[0]
  filename = basename(file)
  pathname = dirname(file)
  #print('%s\%s'%(pathname,filename))

  return((pathname, filename))

##############################################################################
# A generic object
# C = type('C', (object,), {})
class Parms(object):  # Called Parms, short for "Parameters"
    def copy(self):  # make it easy to make copies of this object
        return(copy(self))

##############################################################################