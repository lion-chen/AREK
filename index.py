# -*-coding:utf-8-*-

import os
import sys


def get_resources(path):
    resources = []
    for root, dirs, files in os.walk(os.path.join(path, "r")):
        if files:
            resources += files


def reverse_apk():
    os.system('apktool.bat d %s -o %s' % (apk_path, reversed_apk_path))


if __name__ == '__main__':
    args = sys.argv
    apk_path = args[1]
    reversed_apk_path = os.path.dirname(apk_path) + '/reversed/'
    reverse_apk()
