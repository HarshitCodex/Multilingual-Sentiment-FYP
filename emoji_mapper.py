import emoji

def map_Emoji(sentence):
    sent = emoji.demojize(sentence)
    
    listSplit = sent.split(':')
    semiSolved = ''
    
    for i in range(len(listSplit)):
        semiSolved += listSplit[i]

        if len(listSplit[i])>0 and listSplit[i][-1]!=' ':
            semiSolved += ' '
    
    solved = semiSolved.replace('_', ' ',2)

    return solved



sentence = "a set of words that is complete in itself, typically containing a subject and predicate, conveying a statement, ques 👌👌"
processed = map_Emoji(sentence)

print(processed)
