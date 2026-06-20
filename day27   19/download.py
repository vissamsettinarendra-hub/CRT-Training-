#real tome example :downloading

import threading
import time
def downloading_file(file):
    print("downloding",file)
    time.sleep(3)
    print(file,"finished")
files = ["movies.mp4","songs.mp3","image.jpg"]
threads = []
for f in files:
    t = threading.Thread(target=downloading_file,args=(f,)) 
    threads.append(t)
    t.start()   
for t in threads:
    t.join()
print("all downloads finished")   