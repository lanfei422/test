#!/bin/bash
echo "please execute like:./apply_patch.sh work_dir work_id"

#get the input parameters
work_dir=$1
work_id=$2

cd $work_dir
pre_patch="!@#$%"
for patch in `ls $work_dir/patches`
do
    if [ $pre_patch!="!@#$%" ]
    then
        echo "reverse previous patch."
        git apply -R $pre_patch
    fi
    git apply $patch
    git commit -a -m "$patch is already applied."
    git push origin_$work_id master
    pre_patch=$patch
done