#! /bin/bash

for file in ./config/*.cfg
do 
    run_experiment $file &	
done
