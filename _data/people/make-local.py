import yaml, os

for filename in os.listdir("."):
    if not filename.endswith(".yml"): continue
    #print filename
    person = filename.split('.yml')[0]
    ymlfile = open(filename)
    parsed = yaml.load(ymlfile, Loader=yaml.FullLoader)
    #print parsed['photo']
    photo = parsed['photo']
    if not photo.startswith('http'): continue
    print photo
    cmd = 'wget -O ../../images/photo-%s.%s %s' % (person,photo[-3:],photo)
    print cmd
    os.system(cmd)
