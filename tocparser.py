#### TOC Parser 0.3 ####
#
# Quick and dirty parser for creating intra-linked TOCs from HTML page subheadings with an 'id' #anchor attribute
# Created by Ilkka Klang 2014 
#
# Requires Python 3.x to run
#
# Version 0.3 - initial version, only works on h2 & h3 headings
# 
# To use, copy the script into your work directory and type 'python tocparser.py [filename]'
# The parser creates a text file called 'temptoc.txt' based on the [filename] in the same directory where it's run.
# 
# Free to use, distribute, and modify. Use at your own risk, though.
#########################

import re
import sys

sourcefile = sys.argv[1]
h2 = '<h2'
h3 = '<h3'

# defines how the parser switches between h2 and h3 headings
old_heading = 0

# open a file to generate the TOC in
file = open("temptoc.txt", "w")

file.write('\t\t<ul class="toc">\n')
file.write('\t\t\t<li><a href="#')

with open(sourcefile, 'r') as f:
	for line in f:
	#	utfline = line.encode('utf8')
		# only progress if heading also has an id marker
		if h2 in line and 'id' in line:
			# closing tags depending on previously processed heading
			if old_heading == 2:
				file.write ('</li>\n')
				file.write ('\t\t\t<li><a href="#')
			if old_heading == 3:
				file.write ('</li>\n')
				file.write ('\t\t\t\t</ul>\n')
				file.write ('\t\t\t</li>\n')
				file.write ('\t\t\t<li><a href="#')
			# extract the link anchor from the heading. anything between 'id="' and the next kaksoisheittomerkki is stored	
			link = re.search(r'id="(.*?)"', line).group(1)
			# extract the heading title
			title = re.search(r'>(.*?)<', line).group(1)
			file.write(link + '">' + title + '</a>')
			# when the parser moves to the next heading, this tells what type of heading it processed earlier
			old_heading = 2

		if h3 in line and 'id' in line:
			if old_heading == 2:
				file.write ('\n' + '\t\t\t\t<ul class="toc">\n')
				file.write ('\t\t\t\t<li><a href="#')
			if old_heading == 3:
				file.write ('</li>\n')
				file.write ('\t\t\t\t<li><a href="#')
			# similar processes as with h2 level
			link = re.search(r'id="(.*?)"', line).group(1)
			title = re.search(r'>(.*?)<', line).group(1)
			file.write(link + '">' + title + '</a>')
			old_heading = 3
		# print warnings if h2 and h3 headings without id classes found
		if h2 in line and 'id' not in line:
			print('Note: there is a h2 header without an id class')
		if h3 in line and 'id' not in line:
			print('Note: there is a h3 header without an id class')

# final cleanup and closing the tags in the TOC				
if old_heading == 3:
	file.write ('</li>' + '\n' + '\t\t\t\t</ul>' + '\n' + '\t\t\t</li>' + '\n' + '\t\t</ul>')
if old_heading == 2:
	file.write ('</li>' + '\n' + '\t\t</ul>')
file.close()

print('TOC created for ' + sourcefile)