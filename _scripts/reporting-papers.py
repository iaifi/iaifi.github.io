#### IAIFI Reporting Script

# importing modules
import yaml,os

# importing products
products = os.listdir("../_data/products/")
products.sort(reverse=True)

outputfiledictionary = {}
outputcountdictionary = {}

# Creating all of the output files
for thrust in ['T','E','A']:
  for status in ['submitted','published']:
    for year in ['2020','2021','2022','2023','2024']:
      for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:

        # creating TeX file
        datename = year + "-" + month
        outputfilename = 'papers_'+thrust+'_'+status+'_'+datename+'.tex'
        outputfile = open('reporting/'+outputfilename,"w")
        outputcount = 0
        
        outputfiledictionary.update({outputfilename : outputfile})
        outputcountdictionary.update({outputfilename : outputcount})
        print(outputfilename)
        
        # writing preamble
        outputfile.write('\\begin{itemize}\n')

for filename in products:

  # open product files
  if not filename.endswith(".yml"): continue
  ymlfile = open("../_data/products/" + filename)
  parsed = yaml.load(ymlfile, Loader=yaml.BaseLoader)

  # skip if not paper
  if not (parsed['type'] == 'paper'): continue

  # figure out which file to put things in
  thrust = parsed['iaifi-thrust'][0]
  submitteddate = filename[0:7]
  publisheddate = ''
  if ('publication-date' in parsed): publisheddate = parsed['publication-date'][0:7]
  
  # first do submitted
  status = 'submitted'
  outputfilename = 'papers_'+thrust+'_'+status+'_'+submitteddate+'.tex'
  outputfile = outputfiledictionary[outputfilename]
  print(filename + ' : ' + outputfilename)
  outputcountdictionary[outputfilename] += 1

  # Write to file
  paper = '\\item '
  paper += parsed['authors'].replace('.','.\\ ')
  paper += ', \\textit{'
  paper += parsed['title'] + '}, '
  if parsed['journal']: paper += parsed['journal'] + '. '
  if parsed['arxiv']: paper += '\\href{https://arxiv.org/abs/' + parsed['arxiv'] + '}{[arXiv:' + parsed['arxiv'] + ']} '
  if parsed['code']: paper += ' \\href{' + parsed['code'] + '}{[code]} '
  outputfile.write(paper+'\n')

  # then do published, if available
  if publisheddate == '': continue
  status = 'published'
  outputfilename = 'papers_'+thrust+'_'+status+'_'+publisheddate+'.tex'
  outputfile = outputfiledictionary[outputfilename]
  print(filename + ' : ' + outputfilename)
  outputcountdictionary[outputfilename] += 1
  
  # Write to file
  paper = '\\item '
  paper += parsed['authors'].replace('.','.\\ ')
  paper += ', \\textit{'
  paper += parsed['title'] + '}, '
  if parsed['journal']: paper += parsed['journal'] + '. '
  if parsed['arxiv']: paper += '\\href{https://arxiv.org/abs/' + parsed['arxiv'] + '}{[arXiv:' + parsed['arxiv'] + ']} '
  if parsed['code']: paper += ' \\href{' + parsed['code'] + '}{[code]} '
  outputfile.write(paper+'\n')

# Closing all of the output files
for thrust in ['T','E','A']:
  for status in ['submitted','published']:
    for year in ['2020','2021','2022','2023','2024']:
      for month in ['01','02','03','04','05','06','07','08','09','10','11','12']:

        datename = year + "-" + month
        outputfilename = 'papers_'+thrust+'_'+status+'_'+datename+'.tex'
        outputfile = outputfiledictionary[outputfilename]
        outputcount = outputcountdictionary[outputfilename]

        # writing postamble
        outputfile.write('\\end{itemize}')

        # remove empty files
        if outputcount == 0: os.remove('reporting/'+outputfilename)

        print(outputfilename + ' : ' + str(outputcount))
        


