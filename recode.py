import os
from time import sleep
kosher_extensions="MP4,mp4,mkv,MKV,avi,AVI,ts,TS,mov,MOV".split(",")
paths = [input("type or paste folder path you wish to recode videos from: "), #paths[0]
         input("also recode files in subfolders? (y/n): ")+"/", #paths[1]
         input("type or paste output files path: ")] #paths[2]

i=0
for path in paths:
    if path[-1] == "/":
        sleep(1)
    elif path[-1]==" ":
        paths[i]=paths[i][:-1]
    else:
        paths[i]=paths[i]+"/"
    i+=1
def recode(file,infile):
    go=0
    if "/" in file:
        filename=(file.rsplit("/",1))[1]
    else:
        filename=file
    extension = (filename.rsplit(".",1))[1]
    for ext in kosher_extensions:
        if ext==extension:
            go=1
    if not extension=="mkv":
        filename =filename.rstrip(extension)+"mkv"
    p=0
    while(os.path.exists(paths[2]+filename)):
        filename = filename[:len(filename)-4] +str(p)+filename[-4:]
        p+=1
    if(go):
        print("recoding "+file+" to "+filename)
        os.system("ffmpeg -loglevel quiet -x265-params log-level=quiet -hide_banner  -i \""+infile+"\" -map 0:a? -map 0:s? -map 0:v? -c:v libx265 -preset slow -crf 30  \""+paths[2]+filename+"\"")
for filefolder in os.listdir(paths[0][:-1]):
    if os.path.isfile(paths[0]+filefolder):
        recode(filefolder)
    elif paths[1]=="y/" and os.path.isdir(paths[0]+filefolder):
        print("sub1")
        for subfile in os.listdir(paths[0]+filefolder):
            infile=paths[0]+filefolder+"/"+subfile
            if os.path.isfile(paths[0]+filefolder+"/"+subfile):
                recode(subfile,infile)
            elif os.path.isdir(paths[0]+filefolder+"/"+subfile):
                print("sub2")
                for sub2file in os.listdir(paths[0]+filefolder+"/"+subfile):
                    infile=paths[0]+filefolder+"/"+subfile+"/"+sub2file
                    recode(sub2file,infile)
