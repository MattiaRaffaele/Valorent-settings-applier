from asyncore import read
import time

print("The destination for your file")
dst = input()

print("\nI'll replace \ with /...")

replaced_text = dst.replace("\\" , "/")

fh = open ('Data/dst.txt' , 'w+')
fh.write(replaced_text)


time.sleep(1)
print ("\n\nblip blop done!")


fh.close



print('Press ENTER to exit')
input()
quit()