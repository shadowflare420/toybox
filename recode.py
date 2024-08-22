#requires ffmpeg, python3.?+
#this is set up for linux, if you want to use this on windows you will probably have to make some changes like replacing all the / with \\

#os mostly for using ffmpeg and file checks
import os
#sleep because i couldn't think of anything else to put in that spot and too lazy to rewrite properly
from time import sleep

#extensions that are allowed to be used, entered as one string then split because lazy
kosher_extensions="MP4,mp4,mkv,MKV,avi,AVI,ts,TS,mov,MOV".split(",")

#get user input, then re-assign them because i'm lazy and decided after the fact that having to type y in the middle is incredibly annoying
paths = [input("type or paste folder path you wish to recode videos from: "), #paths[0]
         input("type or paste output folder path: "),#paths[2]
         input("also recode files in subfolders? (y/n): ")] #paths[1] 

temp1=paths[1]
temp2=paths[2]
paths[1]=temp2
paths[2]=temp1

i=0

#ensure every path has a / at the end
for path in paths:
    if path[-1] == "/":
        sleep(0.01)
    elif path[-1]==" ":
        paths[i]=paths[i][:-1]
    else:
        paths[i]=paths[i]+"/"
    i+=1


#define how to encode
def recode(file,infile):
    go=0
#seperate the file name from rest of path, if somehow present
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
    #better than requiring a user prompt every 2 seconds
    while(os.path.exists(paths[2]+filename)):
        filename = filename[:len(filename)-4] +str(p)+filename[-4:]
        p+=1
             
    #idk why i did it this way, but it works well enough to leave alone         
    if(go):
        print("recoding "+file+" to "+filename)
        #this isn't confusing at all 
        os.system("ffmpeg -loglevel quiet -hide_banner  -i \""+infile+"\" -map 0:a? -map 0:s? -map 0:v? -c:v libx265 -preset slow -crf 30  \""+paths[2]+filename+"\"")


#a incredibly inneficient way to write code that loops through a folder and 2 subfolder levels then calls a function when a file is hit
for filefolder in os.listdir(paths[0][:-1]):
    infile=paths[0]+filefolder
    if os.path.isfile(paths[0]+filefolder):
        recode(filefolder,infile)
    elif paths[1]=="y/" and os.path.isdir(paths[0]+filefolder):
        print("sub1")
        for subfile in os.listdir(paths[0]+filefolder):
            infile=paths[0]+filefolder+"/"+subfile
            if os.path.isfile(paths[0]+filefolder+"/"+subfile):
                recode(subfile,infile)
            elif os.path.isdir(paths[0]+filefolder+"/"+subfile):
                print("sub2")
                #ah yes, my naming is flawless  
                for sub2file in os.listdir(paths[0]+filefolder+"/"+subfile):
                    infile=paths[0]+filefolder+"/"+subfile+"/"+sub2file
                    recode(sub2file,infile)
