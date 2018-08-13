openmatrix = open("BLOSUM62_as_two_column.matrix")
readmatrix = openmatrix.read()
splitmatrix = readmatrix.split("\n")


inputfasta = open("CLEs_FINAL_Fished.domains_only_all_species_for_align.fa.refine.minus_first_and_last_3_positions_and_any_with_missing_info.fa")
readfasta= inputfasta.read()
splitfasta = readfasta.split(">")

fastamatrix = ""
for line in splitfasta:
    if len(line)>0:
        #print (line+ "\n")
        splitline = line.split("\n")
        fastamatrix = fastamatrix + splitline[0] + "\t" + splitline[1] + "\n"

print (fastamatrix)
splitfastamatrix = fastamatrix.split("\n")

output = ""
for line in splitfastamatrix:
    if len(line)>0:
        linesplit = line.split("\t")
        name1 =  linesplit[0]
        seq1 = linesplit[1]
        #print (seq1)
        for lines in splitfastamatrix:
            if len(lines)>0:
                linessplit = lines.split("\t")
                name2 =  linessplit[0]
                seq2 = linessplit[1]

                seq1split = list(seq1)
                seq2split = list(seq2)
                #print (seq1split)
                
                BLOSUM_score = 0
                ID_number = 0
                for x in range(len(seq2)):
                    if seq1split[x] in seq2split[x]:
                        ID_number = ID_number + 1
                    for liners in splitmatrix:
                        if len(liners)>0:
                            if seq1split[x] +"\t"+ seq2split[x] in liners:
                                #print (liners)
                                linerssplit = liners.split("\t")
                                #print (linerssplit[2])
                                BLOSUM_score= BLOSUM_score + int(linerssplit[2])
                output = output + name1 + "\t" + name2 + "\t" + str(BLOSUM_score) + "\t"+ str(ID_number) + "\n"
                    #print (seq1split[x])
outfileopened = open("output_blosum_and_id_number_matrix","w")
outfileopened.write(output)
outfileopened.close()
print ("done")
            
                #print (line + " " + lines)
