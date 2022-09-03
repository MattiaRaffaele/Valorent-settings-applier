from multiprocessing.connection import wait
import shutil
import time

print("Press ENTER to start")
input()

src = "GameUserSettings.ini"

print("Getting AppData directory...")#debug
dst = open("Data/dst.txt" , "r")


print("\nPasting in ...")
time.sleep(1)
shutil.copy2(src , dst.read())


dst.close()

print("\nFile pasted")
print("\n\nFile copied press ENTER to exit, have fun :)")
input()
print ("Closing...")
quit()