# -*- coding: utf-8 -*-
"""
Created on Fri Apr 26 2019 

@author: mlgkschm (Ken Schmahl)
"""

from copy import copy
import json as js
import re
from os.path import basename
from os.path import dirname
from os import getcwd
from getopt import getopt, GetoptError
from sys import exit,stderr,stdout
from platform import system

# The next module comes from pywin32: 'pip install pywin32'
if 'Windows' in system():
  import win32gui as gui

VERSION = "v1.2" # 7/21/2023

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

#############################################################################
#############################################################################
# useful functions
def defined(var):
    return(var != None)

#############################################################################
def atoi(text):
    return int(text) if text.isdigit() else text

#############################################################################
def deepcopy(obj):
  return(
    js.loads(js.dumps(obj))
  )

#############################################################################
def mkType(t_name='C'):  # Make a type to be used as a dict
    return(type(t_name, (object,), {}))

#############################################################################
def readFile(fname):
    #print('Filename',fname)
    with open(fname, 'r') as f:
        s = f.read()
    return(s)

##############################################################################
def readlnFile(fname):
    #print('Filename',fname)
    with open(fname, 'r') as f:
        s = f.readlines()
    return(s)

#############################################################################
def getFilename_old(filter=None):
  cwd = getcwd()
  #print('CWD: ',cwd); exit(1)

  if not defined(filter):
    filter = 'All: *.*\0*.*\0'

  try:
    boxDialog = gui.GetOpenFileNameW(None,None,filter,None,1,None,1024,cwd)
  except:
    print('Filename selection aborted')
    exit(1)
  #
  #print('DialogBox output: ',boxDialog)
  file = list(boxDialog)[0]
  filename = basename(file)
  pathname = dirname(file)
  #print('%s\%s'%(pathname,filename))

  return((pathname, filename))

#############################################################################
def getFilename(filter=None):
  cwd = getcwd()
  #print('CWD: ',cwd); exit(1)

  if not defined(filter):
    filter = 'All: *.*\0*.*\0' # Default filename filter
  elif type(filter) == type(list()): # If filter is list form...
    f = ""
    for t in filter:
      f = "\0".join([f,"\0".join(t)])
    filter = f + "\0"
  #print("filter:",filter); exit(1)
  
  try:
    boxDialog = gui.GetOpenFileNameW(None,None,filter,None,1,None,1024,cwd)
  except:
    print('Filename selection aborted')
    exit(1)
  #
  #print('DialogBox output: ',boxDialog)
  file = list(boxDialog)[0]
  filename = basename(file)
  pathname = dirname(file)
  #print('%s\%s'%(pathname,filename))

  return((pathname, filename))

#############################################################################
# A generic object
# C = type('C', (object,), {})
class Struct(object):  # 
  def copy(self):      # make it easy to make copies of this object
    return(copy(self))

class Parms(Struct):   # Called Parms, short for "Parameters"
  None

#############################################################################
def isNumber(s):
  try:
    float(s)
    return True
  except ValueError:
    return False

#############################################################################
def isHex(val, lbits=None): # does string 'val' have a hex value?
  if type(val) != type(''):
    return(None) # return 'None' if not a string
  elif defined(lbits):
    pattern = '^0x[0-9a-fA-F]{%d}$'%lbits
  else:
    pattern = '^0x[0-9a-fA-F_]+$'
  m = re.search(pattern, val)
  return(defined(m)) # return 'True' or 'False'

#############################################################################
def getOpts(args, options=None):
  opts={}
  if not defined(options):
    print('**Error: missing \'options\' keyword')
    print('** getOpts needs a list of options')
    exit(1)

  try:
    optlist, args = getopt(args, options+'h')
    # print('optlist',str(optlist),'\nargs',str(args));exit(1)
  except GetoptError as err:
    print('Error:',err,'\n', file=stderr)
    # showHelp();exit(1)
    raise Exception('showHelp')
  #
  if '-h' in [x[0] for x in optlist]:
    # showHelp();exit(0)
    raise Exception('showHelp')
  #
  return({x[0]:x[1] for x in optlist})

#############################################################################
def sprint(*args, end='', **kwargs):
  sio = io.StringIO()
  print(*args, **kwargs, end=end, file=sio)
  return sio.getvalue()
    
#############################################################################
