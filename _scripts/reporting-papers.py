#### IAIFI Reporting Script

# importing modules
import yaml,os

# importing products
products = os.listdir("../_data/products/")
products.sort(reverse=True)

# main loop
for thrust in ['T','E','A']:
  for status in ['submitted','published']:
    
    # creating TeX file
    filename = 'papers_'+thrust+'_'+status+'.tex'
    print('Writing: ' + filename)
    outputfile = open('reporting/'+filename,"w")
    
    # writing preamble
    outputfile.write('\\begin{itemize}\n')

    # go through all files and extract relevant info

    for filename in products:

      # open product files
      if not filename.endswith(".yml"): continue
      ymlfile = open("../_data/products/" + filename)
      parsed = yaml.load(ymlfile, Loader=yaml.BaseLoader)

      # check if correct thrust and product type
      if not (parsed['iaifi-thrust'][0] == thrust): continue
      if not (parsed['type'] == 'paper'): continue

      # check if submitted or published
      published = False
      if ('doi' in parsed) and (len(parsed['doi'].strip()) > 0): published = True
      if ('alt-url' in parsed) and (len(parsed['alt-url'].strip()) > 0): published = True
      if status == 'submitted' and published: continue
      if status == 'published' and not published: continue

      # good to go!  Now starting writing...
      paper = '\\item '
      paper += parsed['authors'].replace('.','.\\ ')
      paper += ', \\textit{'
      paper += parsed['title'] + '}, '
      if parsed['journal']: paper += parsed['journal'] + '. '
      if parsed['arxiv']: paper += '\\href{https://arxiv.org/abs/' + parsed['arxiv'] + '}{[arXiv:' + parsed['arxiv'] + ']} '
      if parsed['code']: paper += ' \\href{' + parsed['code'] + '}{[code]} '
      outputfile.write(paper+'\n')
      
    # writing postamble
    outputfile.write('\\end{itemize}')
