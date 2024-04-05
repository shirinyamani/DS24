def sum_(n):
    #base case
    if n == 0:
         
        return 0
    else: return n + sum_(n-1)


def sum1(n):
    for _, i in enumerate(n):
        n[i] + n[i+1]



def exist(phrase, list_words, output=None):
    if output is None:
        output= []
    
    for word in list_words:
        if phrase.startswith(word):
            output.append(word)
            return exist(phrase[len(word):], list_words, output)
    return output


print(exist('shirinnoosh',['shirin','noosh']))