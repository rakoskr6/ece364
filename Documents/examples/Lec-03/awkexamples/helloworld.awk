BEGIN { 
    print "BEGIN is a special pattern"
    print "that matches the beginning"
    print "of in a file\n"
    # comments can also be used
    # The print command is a basic command 
    # that writes to standard output
}

END { print "END matches the end of a file" }
