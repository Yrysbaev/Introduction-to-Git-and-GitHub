#!/usr/bin/env python3

import psutil

def check_cpu_usage(percent):

<<<<<<< HEAD
    usage = psutil.cpu_percent(1)
    pring("DEBUG: usage:{}".format(usage))
=======
    usage = psutil.cpu_percent()

>>>>>>> origin/Main
    return usage < percent

if not check_cpu_usage(75):

    print("ERROR! CPU is overloaded")

else:


    print("Everything ok")
<<<<<<< HEAD
=======


>>>>>>> origin/Main
