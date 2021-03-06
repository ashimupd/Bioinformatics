#has all the rna ->amino acid codes
import amino_acid_dictionary as aa
#beck's read fasta file code
import readfasta as rf
#write fasta file code
import writefasta as wf

#uses amino acid dictionary function to create the amino acid dictionary used
amino_acid_codes = aa.create_aa_dict()

'''
Takes an RNA sequence and translates it into amino acids.
@param gene: RNA sequence
@param early_stop: automatically set to true, if false, translation will continue past
    stop sequences
@return: string of amino acids

NOTE: does not currently check for start sequence, that will be added later.
'''
def rna_to_amino_acid(gene,early_stop = True):
    #Flag that says we are not done with our translation, will flip to exit the
    #while when we complete translation
    not_done = True
    #Says we want to start translation at beginning of the rna string
    section_start = 0
    #Where we will store our amino acids we get from translation
    amino_acids = ""
    while not_done:
        #Grabs 3 characters from the string
        section = gene[section_start:section_start+3]
        #Checks if that group is a complete triple
        if len(section) < 3:
            #Since it is not complete, the loop can be over
            not_done = False
            #Add the incomplete RNA sequence to the end of the Amino Acids
            #Within brackets
            amino_acids = amino_acids + '[' + section + ']'
        else:
            #Since it is a complete triple add it's Amino Acid translation
            #to the end of the amino acid string
            amino_acids = amino_acids + amino_acid_codes[section]
            #If you hit a stop sequence end translation, unless early stop mode
            #is false, which means you want it to translate through stop sequences
            if amino_acid_codes[section] == "*" and early_stop == True:
                #Since we are done, flip the flag
                not_done = False
        #Moves the window to the next group of three characters
        section_start +=3
    #returns the amino acid translation
    return amino_acids

#tests a couple of key cases of RNA to amino acid translations and prints results
def test_rna_to_amino_acid():
    #test case sequences
    test_gene_1 = ""
    test_gene_2 = "AAAA"
    test_gene_3 = "UUUUUCUUAUUGCUUCUCCUACUGAUUAUCAUAAUGGUUGUCGUAGUGUCUUCCUCAUCGCCUCCCCCACCGACUACCACAACGGCUGCCGCAGCGUAUUACUAAUAGCAUCACCAACAGAAUAACAAAAAGGAUGACGAAGAGUGUUGCUGAUGGCGUCGCCGACGGAGUAGCAGAAGGGGUGGCGGAGGG"
    #get the amino acid translations
    aa_1 = rna_to_amino_acid(test_gene_1)
    aa_2 = rna_to_amino_acid(test_gene_2)
    aa_3 = rna_to_amino_acid(test_gene_3,False)
    print(aa_2)
    print(aa_3)
    #compate test cases with expect result and print true if the result is correct
    print("Test Cases")
    print(f"Empty RNA String Blank []: {(aa_1 == '[]')}")
    print(f"Incomplete RNA String []: {aa_2 == 'K[A]'}")
    print(f"All Letters Correct: {aa_3 == 'FFLLLLLLIIIMVVVVSSSSPPPPTTTTAAAAYY**HHQQNNKKDDEECC*WRRRRSSRRGGGG[]'}")

'''
Reads a Fasta formated file and converts each sequence to amino acids
@param file name of file you are importing 
'''

def process_cases(file):
    cases_rna = rf.readfasta(file)
    cases_aa = []
    #translates each rna and puts it into a new list of lists of the names and
    #amino acids
    for case in cases_rna:
        cases_aa.append([case[0], rna_to_amino_acid(case[1])])
    return cases_rna, cases_aa

'''
Sets file name, starts the processing function, and writes the results to a file
'''
def main():
    file_name = 'Assignment1Sequences.txt'
    rna, aa = process_cases(file_name)
    wf.write_fasta("Assignment1AminoAcids.txt", aa)

if __name__ == "__main__":
    main()

