def count_lower_upper(s):
    count={'upper':0,'lower':0,'space':0}
    for alpha in s:
        if alpha.isupper():
            count['upper']+=1
        elif alpha.islower():
            count['lower']+=1
        elif alpha.isspace():
            count['space']+=1
        else:
            pass
    return count

str=input('Enter the string: ')
print(count_lower_upper(str))
