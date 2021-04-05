# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received vites
# 3. The percentage f votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

#path to csv file Resources\election_results.csv

# Assign a variable for the file to load and the path.
file_to_load = 'Resources/election_results.csv'

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)

# Add our dependencies
import csv
import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.(3.4.3)
file_to_save = os.path.join("analysis", "election_analysis.txt")

#open the election results and read the file
with open(file_to_load) as election_data:

    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read and print the header row 3.4.4
    headers = next(file_reader)
    print(headers)


# Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    # Write 3 counties to the file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")

