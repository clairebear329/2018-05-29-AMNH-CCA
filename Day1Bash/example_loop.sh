for myfile in {A..Z}.txt;
do
    touch $myfile
    echo $myfile
done

#edited the file to get rid of everything except the loop