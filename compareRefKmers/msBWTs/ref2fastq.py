## Script to convert fasta to fasta
## Started 09 January 2015
## Christian Parobek

## Takes genomes (with chrs represented in multiple lines of text, arbitrary length)
## Pads any short lines with N's
## Converts to fastq format

## Import libraries
import re
import sys

## Read command line, first argument after script name should be input fasta name
## Fasta should be broken up into lines of arbitrary length
name = sys.argv[1]

## Open IN and OUT files
fa_in=open(name,"r")
fa_out=open(name + ".fq", "wa")


## Determine string length
for line in iter(fa_in):
	if re.match('>', line):
		continue
	else:
		strLen=len(line)
		print "All reads should be", strLen, "characters long!"
		break

fa_in=open(name,"r") # Need to re-open the file to iterate from the top

## Using an iterator to read through each line
## Print the line if it's the right length
## Add N's if the line is too short
for line in iter(fa_in):
	line = line.upper() # convert to upper case
	if re.search('>|M|R|W|S|Y|K|V|H|D|B|X|N', line): # remove all non-ATGC bases
		continue
	else:
		if strLen == len(line):
			fa_out.write('@anotherLineFrom ' + name)
			fa_out.write("\n")
			fa_out.write(line.rstrip())
			fa_out.write("\n")
			fa_out.write("+")
			fa_out.write("\n")
			fa_out.write("I" * (strLen-1)) # not sure why I have to subtract 1
			fa_out.write("\n")
		else:
			diff = strLen - len(line) # determine number of N's I'll have to add
			fa_out.write('@anotherLineFrom ' + name)
			fa_out.write("\n")
			fa_out.write(line.rstrip() + "N" * diff)
			fa_out.write("\n")
			fa_out.write("+")
			fa_out.write("\n")
			fa_out.write("I" * (strLen -1)) # not sure why I have to subtract 1
			fa_out.write("\n")

