import os

for filename in os.listdir("."):
    if not filename.endswith(".yml"): continue
    f = open(filename, 'r')
    data = f.readlines()
    #print data
    for i in range(0,len(data)):
        if not data[i].startswith('photo:'): continue
        data[i] = 'photo: images/small-photo-%s.jpg' % (filename.split('.yml')[0])
        #print data[i]
    f = open(filename, 'w')
    f.writelines(data)
