#!/bin/bash

#download file
wget -nv 'ftp://sunsite.informatik.rwth-aachen.de/pub/mirror/ibiblio/gnome/README'
# to lowercase
tr [:upper:] [:lower:] < README |
# remove unnecessary spaces
tr -s " " |
#remove line break 
tr -d "\n" |
#remove digits
tr -d [:digit:] |
#remove punctuation
tr -d [:punct:] |
#split words per line
sed 's/ /\n/g;' |
#sort alphabetically
sort |
#remove duplicates and count occurances
uniq -c |
#sort reverse
sort -r |
#remove digits
tr -d [:digit:] | 
#stdout first 10 lines
head 



