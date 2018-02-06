
def likes(names):
    # if names == [] print "no one likes this"
    if names == []:
        return ("no one likes this")
    # if len(names) == 1 print names[0] likes this
    elif len(names) == 1:
        return ("{} likes this".format(names[0]))
    # if len(names) == 2 print: names[0], and, names [1] likes this
    elif len(names) == 2:
        return ("{} and {} like this".format(names[0], names[1]))
    # if len(names) > 2 print: names[0], names [1] and (len(names) - 2) other
    elif len(names) == 3:
        return ("{}, {} and {} like this".format(names[0], names[1], names[2]))
    elif len(names) > 3:
        others = len(names) - 2
        return ("{}, {} and {} others like this".format(names[0], names[1], others))
