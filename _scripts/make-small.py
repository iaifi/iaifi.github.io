# run this in the images directory
import os

for filename in os.listdir("."):
    
    # get filename without suffix
    filestem = filename[:-4]

    # check that file begins with photo
    if not filestem.startswith('photo'): continue

    # check that small version does not already exist
    newfilename = "small-" + filestem + ".jpg"
    if os.path.exists(newfilename): continue

    # run shrinking command
    print "Converting " + filename + " to " + newfilename
    cmd = 'sips -Z 300 --out small-%s.jpg %s' % (filename[:-4],filename)
    os.system(cmd)


# special fixes
# os.system('sips -c 200 200 small-photo-georgios-valogiannis.jpg')
# os.system('sips -c 190 200 small-photo-rumen-dangovski.jpg')
# os.system('sips -c 200 200 small-photo-dimitra-pefkou.jpg')
# os.system('sips -c 200 200 small-photo-cristiano-fanelli.jpg')
