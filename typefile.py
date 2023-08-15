import pyautogui as ag
import time,sys,base64

f=open(sys.argv[1],"rb")
content=f.read()
f.close()
if len(sys.argv)>2:
    content=(base64.b64encode(content)).decode('utf-8')
time.sleep(5)
ag.write(content)