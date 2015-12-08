# User defined function with arguments
function longest(line) {

    # split takes a string, an array to fill, and a separator
    # returns number of elements split
    n=split(line, words, FS)
    
    long=1
    for(i = 2; i <= n; i++) {
	# length(str) returns the length of a string
	if(length(words[i]) > length(words[long])) {
	    long = i
	}
    }

    return words[long]
}

BEGIN { line=1 }

/[a-z0-9A-Z]/ {
    printf "Line %d: %s\n", line, longest($0)
    line++
}