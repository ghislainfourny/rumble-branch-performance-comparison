# rumble-branch-performance-comparison

Daily pipeline set up on Travis CI and is accessible [here](https://travis-ci.org/CanBerker/rumble-branch-performance-comparison/builds)  

----------------

Run `./compare_branches.sh $branch_name` to compare the performance of the branch given by **$branch_name** against the **master** branch of the rumble project.  
  
`aggregate_results.txt` contains the results in the following format: 
- `$branch_name-$query_id: $average_execution_time`
 
  	
----------------
 
compare_branches.sh takes the following parameters:
- param1 (_required_) - **branch1**: branch to measure the performance for
- param2 (_optional_) - **branch2**: branch to compare the performance against (_default: master_)
- param3 (_optional_) - **repetition_count**: \# of times to repeat the performance measurement (_default: 5_)
- param4 (_optional_) - **dataset**: Dataset to run the experiments with (_default: large_)
- param5 (_optional_) - **project_root**: Root directory of the rumble project (_default: ../rumble_) (_This project is assumed to be co-located with rumble project in the local directory_) 
- param6 (_optional_) - **executable**: rumble executable(.jar) location (_default: ../rumble/target/spark-rumble-1.1-jar-with-dependencies.jar_)

The Great Language game dataset is used for performance measurements and can be accessed at the below link:
http://lars.yencken.org/datasets/languagegame/

2 smaller sample sets are created locally with:  
```
head -n 500000 confusion-2014-03-02.json > confusion500k.json  
head -n 5000000 confusion-2014-03-02.json > confusion5m.json  
```

Data size for performance measurement is specificed by following values of dataset parameter:  
- large : Full (~16.5m lines) dataset
- medium : 5m lines dataset
- small : 500k lines dataset
