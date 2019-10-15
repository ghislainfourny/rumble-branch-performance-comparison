#!/bin/bash
set -e # exit if any command fails

# read parameters
branch1=$1
branch2=${2:-master}
repetition_count=${3:-5}
dataset=${4:-"large"}       # large, medium, small
project_root=${5:-"${HOME}/Project/rumble"}
executable=${6:-"${HOME}/Project/rumble/target/spark-rumble-1.1-jar-with-dependencies.jar"}

echo $branch1
echo $branch2
echo $repetition_count
echo $dataset
echo $project_root
echo $executable

# get executables from project branches
for branch in ${branch1} ${branch2}
do
    echo "Getting executable for branch: $branch"
    pushd $project_root
    git co $branch
    mvn clean compile assembly:single
    popd
    cp $executable "./bin/${branch}_exec.jar" 
done

# clean leftover logs and outputs
find . -name "*log*.txt" -type f | xargs rm -rf 
find . -name "*output*.txt" -type d | xargs rm -rf

export SPARK_SUBMIT_OPTS=-agentlib:jdwp=transport=dt_socket,server=y,suspend=n,address=5005;

for ((i=0; i<=repetition_count; i++));
do
    echo "Iteration: $i "
    for query in "query1" "query4" "query5"
    do
        echo "Query: $query "
        for branch in $branch1 $branch2
        do
            echo "Branch: $branch "
            # define query parameters
            query_path="./${query}/${dataset}-${query}.jq"
            query_ouput_path="./output/${dataset}-${branch}-${query}-output${i}.txt"
            query_log_path="./output/${dataset}-${branch}-${query}-log${i}.txt"

            spark-submit --master local[*] "./bin/${branch}_exec.jar" --query-path "${query_path}" --output-path "${query_ouput_path}" --log-path "${query_log_path}" --result-size 16000000
        done
    done
done

