# -*- coding: utf-8 -*-
"""
Created on Wed Apr 18 18:00:45 2018

@author: longyin
"""
from bs4 import BeautifulSoup
from os import listdir
from os.path import isfile, join
import os
import codecs
inputpath = 'C:\\Project\\HTMLFolder' # input path of the folder which contains the html files
os.chdir(inputpath)
onlyfiles = [f for f in listdir(inputpath) if isfile(join(inputpath, f))]
for thisfile in onlyfiles:
    f=codecs.open(thisfile, 'r')
    soup = BeautifulSoup(f)
    # kill all script and style elements
    for script in soup(["script", "style"]):
        script.extract()    # rip it out
    
    # get text
    text = soup.get_text()
    
    # break into lines and remove leading and trailing space on each
    lines = (line.strip() for line in text.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    text = '\n'.join(chunk for chunk in chunks if chunk).encode('utf-8')
    print(thisfile)
    outputfilename=thisfile.replace('.html', '.txt')
    
    txt_file= open(outputfilename,"w")
    txt_file.write(text)
    txt_file.close()

