openmatrix = open("output_blosum.matrix")
readmatrix = openmatrix.read()
splitmatrix = readmatrix.split("\n")
output = ""
for line in splitmatrix:
    if len(line)>0:
        #print (line)
        splitline = line.split("\t")
        name1 = splitline[0]
        name2 = splitline[1]
        blosum_score = int(splitline[2])
        for lines in splitmatrix:
            if len(lines)>0:
                if name2 + "\t" + name2 +"\t" in lines:
                    splitlines = lines.split("\t")
                    self_blosum = int(splitlines[2])
        output = output + name1 + "\t" + name2 + "\t" + str(blosum_score) + "\t" + str(self_blosum) + "\tselfblosum for name 2 only\n"
outfileopened = open("output_BLOSUM_with_selfBLOSUM_for_name_2_in_matrix_fix_attempt.matrix","w")
outfileopened.write(output)
outfileopened.close()
print ("done")
