# run this in the images directory 
import os

for filename in os.listdir("."):
    if not filename.startswith('photo'): continue
    cmd = 'sips -Z 300 --out small-%s.jpg %s' % (filename[:-4],filename)
    print cmd
    os.system(cmd)
