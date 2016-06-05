# TOC-Parser
Quick n' dirty parser for creating intra-linked TOCs from HTML page subheadings. Requires Python 3.x

Reads a HTML file and creates a Table of Contents in an Unordered List structure from all h2 & h3 -level subheadings in the file. 

Usage:

```
python tocparser.py [filename]
```

Creates a *temptoc.txt* file that contains the TOC in the same directory where the script is run.