print("The destination for your file")
dst = input()
fh = open ('Data/dst.txt' , 'w')
fh.write(dst)
fh.close

print('Press ENTER to exit')
input()
quit()