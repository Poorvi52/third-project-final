import os
import shutil
import time

def main():
    path= "E:/Win10/Desktop/fornopurpose/no.jpg"
    days= 30
    seconds=time.time()-(days*24*60*60)
    if os.path.exists(path):
        os.remove(path)
main()