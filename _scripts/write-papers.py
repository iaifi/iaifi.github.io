import yaml,os

products = os.listdir("../_data/products/")
products.sort(reverse=True)

for filename in products:
    if not filename.endswith(".yml"): continue
    #print filename
    #continue
    ymlfile = open("../_data/products/" + filename)
    parsed = yaml.load(ymlfile, Loader=yaml.BaseLoader)
    if not (parsed['type'] == 'paper'): continue
    paper = '\\item '
    paper += parsed['authors'].replace('.','.\\ ')
    paper += ', \\textit{'
    paper += parsed['title'] + '}, '
    if parsed['journal']: paper += parsed['journal'] + '. '
    if parsed['arxiv']: paper += '[arXiv:' + parsed['arxiv'] + '] '
    if parsed['code']: paper += ' [code: ' + parsed['code'] + ']'
    print paper
    print ' '
