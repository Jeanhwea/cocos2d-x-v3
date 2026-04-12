#!/usr/bin/python
# check crash of cppemptytest
# install/open/uninstall apk
# perpose: for emptytest.
# now support: android
# will add: autotest-win7

import os
import sys
import json
import time
import socket
import platform
import threading
import codecs
import re
import paramiko

payload = {}
#get payload from os env
if 'payload' in os.environ:
    payload_str = os.environ['payload']
    #parse to json obj
    payload = json.loads(payload_str)
print('payload:',payload)
pr_num = 6326
#get pull number
if 'number' in payload:
    pr_num = payload['number']
print('pr_num:' + str(pr_num))
run_app_time = 5
if 'RUN_APP_TIME' in os.environ:
    run_app_time = os.environ['RUN_APP_TIME']
print('run_app_time:', run_app_time)

test_name = ['cpp_empty_test']
if 'TESTS_NAME' in os.environ:
    temp_var = os.environ['TESTS_NAME']
    test_name = temp_var.split(', ')
package_name = ['org.cocos2dx.cpp_empty_test']
if 'PACKAGE_NAME' in os.environ:
    temp_var = os.environ['PACKAGE_NAME']
    package_name = temp_var.split(', ')
activity_name = ['org.cocos2dx.cpp_empty_test.AppActivity']
if 'ACTIVITY_NAME' in os.environ:
    temp_var = os.environ['ACTIVITY_NAME']
    activity_name = temp_var.split(', ')
gIdx = 0
if 'TEST_INDEX' in os.environ:
    gIdx = os.environ('TEST_INDEX')

current_platform = platform.system()
print('current platform is:', current_platform)
