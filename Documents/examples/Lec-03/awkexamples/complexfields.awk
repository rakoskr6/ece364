BEGIN { FS=","; line=0 } # use ; to separate statements

{
    if(line == 0) {
        line++
        next # skip to the next line                                         
    }
    max = $1; min = $1; sum = $1

    # NF is a special variable that contains the Number of Fields            
    for (i=2; i<=NF; i++) {
        sum += $i # $i will expand into $2 and get the ith field             
        if($i > max) max = $i
        if($i < min) min = $i
    }

    print "Line " line ": min=" min " max=" max " avg=" max/NF
    line++
}
