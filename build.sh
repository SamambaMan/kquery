for i in $(find ./ -iname *.ui)
do 
    name=$(echo $i | sed -e "s/.ui//g"); 
    echo Compiling $i
    pyuic5  $name.ui > $name.py
done
