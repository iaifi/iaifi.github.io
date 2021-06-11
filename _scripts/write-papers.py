import yaml,os

products = os.listdir("../_data/products/")
products.sort(reverse=True)

for thrust in ['T','E','A']:
    print 'main thrust = ', thrust, '\n'
    for status in ['submitted','published']:
        print 'papers', status, '\n'
        print '\\begin{itemize}'
        print ' '
        for filename in products:
            if not filename.endswith(".yml"): continue
            ymlfile = open("../_data/products/" + filename)
            parsed = yaml.load(ymlfile, Loader=yaml.BaseLoader)
            if not (parsed['iaifi-thrust'][0] == thrust): continue
            if not (parsed['type'] == 'paper'): continue
            published = False
            if ('doi' in parsed) and (len(parsed['doi'].strip()) > 0): published = True
            if ('alt-url' in parsed) and (len(parsed['alt-url'].strip()) > 0): published = True
            if status == 'submitted' and published: continue
            if status == 'published' and not published: continue

            paper = '\\item '
            paper += parsed['authors'].replace('.','.\\ ')
            paper += ', \\textit{'
            paper += parsed['title'] + '}, '
            if parsed['journal']: paper += parsed['journal'] + '. '
            if parsed['arxiv']: paper += '\\href{https://arxiv.org/abs/' + parsed['arxiv'] + '}{[arXiv:' + parsed['arxiv'] + ']} '
            if parsed['code']: paper += ' \\href{' + parsed['code'] + '}{[code]} '
            print paper
            print ' '
        print '\\end{itemize}'
        print ' '
