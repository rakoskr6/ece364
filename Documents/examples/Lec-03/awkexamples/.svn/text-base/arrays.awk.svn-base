{
    # Arrays are associative so you can use strings as an index
    # Building a map: "word" => count
    # No need to declare the array in BEGIN, just start assigning values
    # default value is 0/empty
    for (i = 1; i <= NF; i++)
	freq[$i]++
}

END {
    for (word in freq) {
	# Print only very frequent words
	if(freq[word] > 5000) {
	    # printf acts like all other printfs
	    printf "%s\t%d\n", word, freq[word]
	}
    }
}