import sys,base64

f=open(sys.argv[1],"rt")
enc=f.read()
f.close()
cont=base64.b64decode(enc)
f=open(sys.argv[2],"wb")
f.write(cont)
f.close()