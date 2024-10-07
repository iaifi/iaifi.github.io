#### IAIFI Reporting Script

# importing modules
import yaml,os,pybtex.database

def iaifi_quarter(month):
  if month in ['10','11','12']: return 'Q1'
  if month in ['01','02','03']: return 'Q2'
  if month in ['04','05','06']: return 'Q3'
  if month in ['07','08','09']: return 'Q4'
  raise Exception("Quarter not defined for:" + month)

def iaifi_year(year,month):
  if month in ['10','11','12']:
    if year == '2019': return 'Y0'
    if year == '2020': return 'Y1'
    if year == '2021': return 'Y2'
    if year == '2022': return 'Y3'
    if year == '2023': return 'Y4'
    if year == '2024': return 'Y5'
  else:
    if year == '2020': return 'Y0'
    if year == '2021': return 'Y1'
    if year == '2022': return 'Y2'
    if year == '2023': return 'Y3'
    if year == '2024': return 'Y4'
    if year == '2025': return 'Y5'

  raise Exception("Year not defined for:" + year + "_" + month)

def iaifi_year_quarter(year,month):
  return iaifi_year(year,month) + "_" + iaifi_quarter(month)


# importing products
products = os.listdir("../_data/products/")
products.sort(reverse=True)

# Creating bibtex files/strings
output_bibtex_file = open('reporting/iaifi_bibliography.bib',"w")
output_thrust_keys_string_dictionary = {}
for thrust in ['T','E','A','F']:
  output_string = '\\cite{'
  output_thrust_keys_string_dictionary.update({thrust : output_string})

# Creating all of the output files
outputfiledictionary = {}
outputcountdictionary = {}
for thrust in ['T','E','A','F']:
  for status in ['submitted','published']:
    for year in ['Y0','Y1','Y2','Y3','Y4','Y5']:
      for quarter in ['Q1','Q2','Q3','Q4']:

        # creating TeX file
        datename = year + "_" + quarter
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

  # If present, pull out bibtex entry
  if ('bib-tex' in parsed):
    bibtex_string = parsed['bib-tex']
    output_bibtex_file.write(bibtex_string+'\n')
    this_key = next(iter(pybtex.database.parse_string(bibtex_string,"bibtex").entries))
    this_thrust = parsed['iaifi-thrust'][0]
    output_thrust_keys_string_dictionary[this_thrust] += this_key+','


  # figure out which file to put things in
  thrust = parsed['iaifi-thrust'][0]
  submitteddate = iaifi_year_quarter(filename[0:4],filename[5:7])
  publisheddate = ''
  if ('publication-date' in parsed and not parsed['publication-date'] == ''):
    publisheddate = iaifi_year_quarter(parsed['publication-date'][0:4],parsed['publication-date'][5:7])
  
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
for thrust in ['T','E','A','F']:
  for status in ['submitted','published']:
    for year in ['Y0','Y1','Y2','Y3','Y4','Y5']:
      for quarter in ['Q1','Q2','Q3','Q4']:

        datename = year + "_" + quarter
        outputfilename = 'papers_'+thrust+'_'+status+'_'+datename+'.tex'
        outputfile = outputfiledictionary[outputfilename]
        outputcount = outputcountdictionary[outputfilename]

        # writing postamble
        outputfile.write('\\end{itemize}')

        # remove empty files
        if outputcount == 0: os.remove('reporting/'+outputfilename)

        print(outputfilename + ' : ' + str(outputcount))
        

# Closing the bibtex key files
for thrust in ['T','E','A','F']:
  outputfile = open('reporting/iaifi_paper_key_'+thrust+'.tex',"w")
  output_string = output_thrust_keys_string_dictionary[thrust]
  if output_string[-1] == ',':
    output_string = output_string[:-1]
  output_string += '}'
  outputfile.write(output_string)
