#!/usr/bin/python
# create new project by cocos-console
# compile, deploy project and run
# perpose: for autotest cocos2d-console command.
# now support: mac- mac/ios/android
# will add: window-android,linux-android

import os
import subprocess
import sys
import json
import time
import socket
import threading
import smtplib
from email.mime.text import MIMEText
from os.path import join, getsize

# default console_param.
console_param = '[console run]'
# get param from commit.
if 'payload' in os.environ:
    payload_str = os.environ['payload']
    payload = json.loads(payload_str)
    if 'console' in payload:
        console_param = payload['console']
console_param = console_param[1:len(console_param)-1]
print('console_param:',console_param)

console_param_arr = console_param.split(' ')

# enum command type
class ENUM_PARAM:
    new = 0
    compile = 1
    deploy = 2
    run = 3

# partition different level
LEVEL_COCOS = {
    ENUM_PARAM.new : 1,
    ENUM_PARAM.compile : 2,
    ENUM_PARAM.deploy : 4,
    ENUM_PARAM.run : 8
}

# level's cocos command
COCOS_CMD = {
    ENUM_PARAM.new:'new',
    ENUM_PARAM.compile:'compile',
    ENUM_PARAM.deploy:'deploy',
    ENUM_PARAM.run:'run'
}

# set cocos_param for run different command
cocos_param = 0
for level in LEVEL_COCOS:
    if console_param_arr.count(COCOS_CMD[level]):
        cocos_param = cocos_param + LEVEL_COCOS[level]
if cocos_param < LEVEL_COCOS[ENUM_PARAM.new]:
    cocos_param = LEVEL_COCOS[ENUM_PARAM.new]
print('cocos_param:', cocos_param)
