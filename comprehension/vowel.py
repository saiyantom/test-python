words = {'Learning':1,'Python':2,'Together':3,'is':4,'Interesting':5}

words_new={''.join(alpha for alpha in k if alpha not in 'aeiou'):v
               for (k,v) in words.items() }

print(words_new)
