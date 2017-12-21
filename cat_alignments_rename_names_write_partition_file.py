import os
import re
from Bio import AlignIO

##listofnames = open("common_cegma_names213.txt")
##
##for line in listofnames:
##    trim = line.replace("\n","")
##    #print "___"+trim+"___"
##    print r"cat "+ trim +"* > " + trim+".fa"
##
parition_string = ""
oldlength = 1
all_alns = None
for filename in os.listdir("."):
    if re.search( "_trimal.txt", filename):
        
        #print filename
        align = AlignIO.read(filename, "fasta")
        align.sort()
        for r in align:
            r.id = r.id.split("_")[0]
            length = len(r.seq)
        #print (str(length))
        parition_string = parition_string + "DNA, part1 = " + str(oldlength) +"-"+str(oldlength + length -1)+"\n"
        oldlength = oldlength + length
        if all_alns is None:
            all_alns = align
        else:
            all_alns += align
print all_alns.format("fasta")

outparition_file= open("partition_file.part","w")
outparition_file.write(parition_string)
outparition_file.close()

    
