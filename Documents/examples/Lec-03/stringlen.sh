#! /bin/bash

One="This is a big line"
Two="12345"
Three=$(pwd)

printf "%2d %s\n" ${#One} "${One}"
printf "%2d %s\n" ${#Two} "${Two}"
printf "%2d %s\n" ${#Three} "${Three}"

exit 0