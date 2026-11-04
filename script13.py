# Script to create Kafka topic json config file.
import json
import os
import random 
list_of_partitions = [0,1,2,6,7,12,13,14,18,19,20]
#partitions = {"version":1,"partitions":[{"topic":"piq","partition":0,"replicas":[]},{"topic":"foo2","partition":1,"replicas":[2,3]}]}
with open('part.json', 'at',) as file:
    for par in list_of_partitions:
        brokers = [25,26,27]
        choice = random.choices(brokers, k=3)
        env = {"topic":"PIQ","partition": par,"replicas":choice, "log_dirs":["any","any","any"]}
        #env = {"version":1,"partitions":[{"topic":"piq","partition": par,"replicas":choice}]}
        json.dump(env, file, indent=4)
        #file.writelines(env2)
        #print(par)