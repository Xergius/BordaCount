#-------------------------------------------------------------------------------------
#
# Program to create a Bords rank aggregated list based on a list of individual ranks
#
#-------------------------------------------------------------------------------------

import csv
import pandas
import pprint


rankings = []

# Getting the data from a csv file.
with open('Ranked_list.csv', newline='') as csvfile:
    lists = csv.reader(csvfile, delimiter=',')
    for row in lists:
        if (row[1] != '') and (row[1] != 'Rank of parameters'): # Omits the first line with title.
            row[1].replace("  ", " ")             # Replace double spacebar for a single one
            ranklist = row[1].split(', ')
            for item in ranklist:
                if item[0]==' ':
                    ranklist[ranklist.index(item)] = ranklist[ranklist.index(item)][1:]
            rankings.append(ranklist)

# For testing:
# rankings  = [["banana","pera", "naranja"],["banana", "naranja", "pera"],["naranja", "banana"],["pera", "naranja", "manzana", "banana"]]
maxpoints = 0
alternatives = set()
for i in rankings:
    for j in i:
        alternatives.add(j)                # Add alternative to a set to avoid repetitions.
rankdict = []
scores = {}
maxpoints = len(alternatives)               # max score for an alternative.

# Create a list of dictionaries for the list of rankings
for i in rankings:
    dict = {}
    for j in i:
        dict[j] = maxpoints-i.index(j)
    rankdict.append(dict)                   

# Add the scores for every alternative and add them into a dictionary (scores)
for item in alternatives:
    count = 0
    for list in rankdict:
        if item in list:
            count = count+list[item]
    scores[item] = count

# Orders the scores dict into a finalRanking dict
finalRanking = {k: v for k, v in sorted(scores.items(),reverse=True, key=lambda item: item[1])}

pprint.pprint(finalRanking, sort_dicts=False)

# Saves the dict into a csv file.
print(maxpoints)
print(len(alternatives))
with open('Final Ranking.csv', 'w') as f:
    for key in finalRanking.keys():
        f.write("%s,%s\n"%(key,finalRanking[key]))
