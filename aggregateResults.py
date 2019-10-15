import os
import sys

branch1 = sys.argv[0]
branch2 = 'master'
iteration_count = 5
dataset = 'large'
# path = '/home/can/Project/rumble-branch-performance/output/'
path = './output'

if (len(sys.argv) == 2):
    branch2 = sys.argv[1]
if (len(sys.argv) == 3):
    iteration_count = sys.argv[2]
if (len(sys.argv) == 4):
    dataset = sys.argv[3]
if (len(sys.argv) == 5):
    path = sys.argv[4]
  
branch1_q1_results = []
branch2_q1_results = []

branch1_q4_results = []
branch2_q4_results = []

branch1_q5_results = []
branch2_q5_results = []

def Average(lst): 
    return sum(lst) / len(lst) 

listing = os.listdir(path)

with open('aggregate_results.txt', 'w') as output:
    for infile in listing:
        print("current file is: " + infile)
        with open(path + infile, 'r') as input:
            if infile.startswith(f"{dataset}-{branch1}-query1-log"):
                branch1_q1_results.append(int(input.readline()[10:-1]))
            elif infile.startswith(f"{dataset}-{branch2}-query1-log"):
                branch2_q1_results.append(int(input.readline()[10:-1]))
            
            elif infile.startswith(f"{dataset}-{branch1}-query4-log"):
                branch1_q4_results.append(int(input.readline()[10:-1]))
            elif infile.startswith(f"{dataset}-{branch2}-query4-log"):
                branch2_q4_results.append(int(input.readline()[10:-1]))
            
            elif infile.startswith(f"{dataset}-{branch1}-query5-log"):
                branch1_q5_results.append(int(input.readline()[10:-1]))
            elif infile.startswith(f"{dataset}-{branch2}-query5-log"):
                branch2_q5_results.append(int(input.readline()[10:-1]))

    branch1_q1_avg = Average(branch1_q1_results)
    branch2_q1_avg = Average(branch2_q1_results)

    branch1_q4_avg = Average(branch1_q4_results)
    branch2_q4_avg = Average(branch2_q4_results)

    branch1_q5_avg = Average(branch1_q5_results)
    branch2_q5_avg = Average(branch2_q5_results)

    output.writelines([
        "Branch1-Q1: " + str(branch1_q1_avg) + "\n",
        "Branch2-Q1: " + str(branch2_q1_avg) + "\n",
        
        "Branch1-Q4: " + str(branch1_q4_avg) + "\n",
        "Branch2-Q4: " + str(branch2_q4_avg) + "\n",
        
        "Branch1-Q5: " + str(branch1_q5_avg) + "\n",
        "Branch2-Q5: " + str(branch2_q5_avg) + "\n",
    ])
