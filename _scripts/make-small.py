# run this in the images directory
import os

for filename in os.listdir("."):
    if not filename.startswith('photo'): continue
    cmd = 'sips -Z 300 --out small-%s.jpg %s' % (filename[:-4],filename)
    print cmd
    os.system(cmd)

# speical fixes
os.system('sips -c 200 200 small-photo-georgios-valogiannis.jpg')
os.system('sips -c 190 200 small-photo-rumen-dangovski.jpg')
os.system('sips -c 200 200 small-photo-dimitra-pefkou.jpg')
os.system('sips -c 200 200 small-photo-cristiano-fanelli.jpg')
