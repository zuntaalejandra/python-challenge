import os
import csv


# Function: print a line of 20 caracteres like this "-"

def print_line():

    line = "-"
    for i in range(20):
        line = line + "-"
    return line


# Function: write the result data in a file

def print_in_file(print_Data):
    
    resulting = os.path.join("", "analysis", "election_result.txt")
    with open(resulting, "w") as f:
        f.write("\n".join(print_Data))

# Function: print the result calculation of voting data 

def print_Results(numVotes,winner_Name,data):

    # build array to print on file
    print_Data = []

    print("Election Results")
    print_Data.append("Election Results")

    print(print_line())
    print_Data.append(print_line())

    print(f"Total Votes : "+str(numVotes))
    print_Data.append(f"Total Votes : "+str(numVotes))

    print(print_line())
    print_Data.append(print_line())
    
    for item in data:
        print(f"{item[1]}: %{((int(item[2])/numVotes)*100):.3f} ({item[2]})")
        print_Data.append(f"{item[1]}: %{((int(item[2])/numVotes)*100):.3f} ({item[2]})")
    

    print(print_line())
    print_Data.append(print_line())

    print(f"Winner : "+winner_Name)
    print_Data.append(f"Winner : "+winner_Name)
    
    print(print_line())
    print_Data.append(print_line())

    # write the results in file        
    print_in_file(print_Data)



election_csv = os.path.join("", "Resources", "election_data.csv")

with open(election_csv) as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=',')

    # Si tiene header la sig linea lee el header 
    header = next(csv_reader)

    # variables to hold rows in input file

    index = []
    i_BallotID = []
    i_County = []
    i_Candidate = []

    # hold the first computation of data file, For-1 
    o_Index = []
    o_Candidate = []
    o_NumVote = []

    # hold the last summary of vote counting, For-2  
    f_Index = []
    f_Candidate = []
    f_NumVote = []


    # read the input file
    
    rownumber = 1

    # read the file and store info in arrays

    for row in csv_reader:
        
        index.append(rownumber)
        i_BallotID.append(row[0])
        i_County.append(row[1])
        i_Candidate.append(row[2])

        rownumber += 1

print("num de rows "+str(rownumber))

# add a last row    
index.append(rownumber)
i_BallotID.append("End")
i_County.append("End")
i_Candidate.append(0)

rownumber += 1


    # calculate votation results

# this variable holds the number or rows of the first result matriz
curr_o_index = 1
curr_Candidate = i_Candidate[1]    
curr_votes = 1

#
# For-1 to make the first summary from the data file (several rows per candidate)
#
#


for i in range(1,rownumber):

    # change Candidate

    if (i_County[i] =="End"):

        break

    if (curr_Candidate != i_Candidate[i+1]): 

        o_Index.append(curr_o_index)
        o_Candidate.append(curr_Candidate)
        curr_votes += 1
        o_NumVote.append(curr_votes)
        curr_o_index += 1

        curr_Candidate = i_Candidate[i+1]
        curr_votes = 0

    else: # the same candidate

        curr_votes += 1       

# add a last row    
o_Index.append(curr_o_index)
o_Candidate.append("End")
o_NumVote.append(0)

curr_o_index += 1

#
# For-2 to make a summary from the first's loop data (just one single row per candidate)
#
#

# holds the index of the most voting candidate
Winner_name = "" 
Winner_votes = 0 

found_Cand_Index = 1

for i in range(0,curr_o_index+1):

    found = False

    if i==0:

        f_Index.append(i)
        f_Candidate.append(o_Candidate[i])
        f_NumVote.append(int(o_NumVote[i]))
        Winner_name = o_Candidate[i]
        Winner_votes = o_NumVote[i]

    elif o_Candidate[i]=="End":

        break

    else:

        for j in range(0,found_Cand_Index):

            # did found the candidate

            if o_Candidate[i]==f_Candidate[j]:

                f_NumVote[j] += o_NumVote[i]
                found = True

                # this Candidate has more votes? 
                if f_NumVote[j]> Winner_votes:
                    Winner_votes = f_NumVote[j]
                    Winner_name = o_Candidate[i]
                break

        if found==False: # did not find the candidate
                
            found_Cand_Index += 1    
            f_Index.append(found_Cand_Index)
            f_Candidate.append(o_Candidate[i])
            f_NumVote.append(o_NumVote[i])
            
            # this Candidate has more votes? 
            if o_NumVote[i]> Winner_votes:
                Winner_votes = o_NumVote[i]
                Winner_name = o_Candidate[i]   



# final process, show in screen results and creates a file with final data

data_list_f = zip(f_Index, f_Candidate, f_NumVote)

print_Results(rownumber-2,Winner_name,data_list_f)






 