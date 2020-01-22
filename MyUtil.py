import sys
import time
class MyUtil:
    @staticmethod
    def write_log(file,line,func,content):
        str_content=file+" "+str(line)+" "+func+" "+time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))+" "+content+" "+"\n"
        #if (sys.platform=="win32"):
        #    f=open("d:\\log.txt","a+")
        #else:
        f=open("/root/backlog.txt", "a+")
        f.write(str_content)
        f.close()

