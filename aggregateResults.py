import os
import sys

# sys.argv[0] is aggregateResults.py
branch1 = sys.argv[1]
branch2 = 'master'
iteration_count = 5
dataset = 'large'
path = './output/'

if (len(sys.argv) >= 3):
    branch2 = sys.argv[2]
if (len(sys.argv) >= 4):
    iteration_count = sys.argv[3]
if (len(sys.argv) >= 5):
    dataset = sys.argv[4]
if (len(sys.argv) >= 6):
    path = sys.argv[5]

# print(f"branch1: {branch1}, branch2: {branch2}, iteration_count: {iteration_count}, dataset:{dataset}, path: {path}")
print("branch1: " + str(branch1) + ", branch2: " + str(branch2) + " , iteration_count: " + str(iteration_count) + " , dataset: " + str(dataset) + " , path: " + str(path))

branch1_q1_results = []
branch2_q1_results = []

branch1_q4_results = []
branch2_q4_results = []

branch1_q5_results = []
branch2_q5_results = []

def Average(lst): 
    return sum(lst) / len(lst) 

listing = os.listdir(path)

with open('./aggregate_results.txt', 'w') as output:
    for infile in listing:
        print("current file is: " + infile)
        with open(path + infile, 'r') as input:
            if infile.startswith('{0}-{1}-query1-log'.format(dataset, branch1)):
                branch1_q1_results.append(int(input.readline()[10:-1]))
            elif infile.startswith('{0}-{1}-query1-log'.format(dataset, branch2)):
                branch2_q1_results.append(int(input.readline()[10:-1]))
            
            elif infile.startswith('{0}-{1}-query4-log'.format(dataset, branch1)):
                branch1_q4_results.append(int(input.readline()[10:-1]))
            elif infile.startswith('{0}-{1}-query4-log'.format(dataset, branch2)):
                branch2_q4_results.append(int(input.readline()[10:-1]))
            
            elif infile.startswith('{0}-{1}-query5-log'.format(dataset, branch1)):
                branch1_q5_results.append(int(input.readline()[10:-1]))
            elif infile.startswith('{0}-{1}-query5-log'.format(dataset, branch2)):
                branch2_q5_results.append(int(input.readline()[10:-1]))

    branch1_q1_avg = Average(branch1_q1_results)
    branch2_q1_avg = Average(branch2_q1_results)

    branch1_q4_avg = Average(branch1_q4_results)
    branch2_q4_avg = Average(branch2_q4_results)

    branch1_q5_avg = Average(branch1_q5_results)
    branch2_q5_avg = Average(branch2_q5_results)

    results = [
        '{0}-Q1: {1}\n'.format(branch1, branch1_q1_avg),
        '{0}-Q1: {1}\n'.format(branch2, branch2_q1_avg),
        '{0}-Q4: {1}\n'.format(branch1, branch1_q4_avg),
        '{0}-Q4: {1}\n'.format(branch2, branch2_q4_avg),
        '{0}-Q5: {1}\n'.format(branch1, branch1_q5_avg),
        '{0}-Q5: {1}\n'.format(branch2, branch2_q5_avg),
    ]

    print(''.join(results))
    output.writelines(results)

if ((branch2_q1_avg > branch1_q1_avg * 11/10)
    or (branch2_q4_avg > branch1_q4_avg * 11/10)
    or (branch2_q5_avg > branch1_q5_avg * 11/10)):
    # sys.exit([f"Performance degredation detected... Please investigate recent merges to {branch2}"])
    sys.exit(["Performance degredation detected... Please investigate recent merges to " + str(branch2)])
