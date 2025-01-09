def split_and_join(line):
    # write your code here
    split = line.split()
    result = "-".join(split)
    return result


line = "r t yur "
print(split_and_join(line))
