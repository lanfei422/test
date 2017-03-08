#!/bin/bash

#get input parameters
source_dir=$1
project_name=$2
work_id=$3

#change to the source dir
cd $source_dir

#initiate git repository
git init
#add all files
git add -A
#create remote branch,named by workid.
git remote add origin_$work_id git@192.168.9.119:/home/git/srv/sample.git
#push all the file to the remote server.
git push -u origin_$work_id master