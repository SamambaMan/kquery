#!/bin/bash
for i in $(find ./ -iname *.ui)
do 
    name=${i//.ui/''}
    echo Compiling $i
    pyuic5  $name.ui > $name.py
done
