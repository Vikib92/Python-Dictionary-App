import json
from difflib import get_close_matches

data = json.load(open("data.json","r"))

def meaning(w):
    w = w.lower()
    if w in data.keys():
        return data[w]
    elif w.title() in data.keys():
        return data[w.title()]
    elif w.upper() in data.keys():
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys())) > 0:
        pmp = input("Did you mean '{}' instead ? Enter Y or N : ".format(get_close_matches(w,data.keys())[0]))
        if pmp.lower() == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif pmp.lower() == "n":
            pmq = str(input("Did you mean any of these then ? {}".
                    format(', '.join([str(i)+"."+j for i, j in enumerate(get_close_matches(w,data.keys()),1)])) + "\nSelect your choice: "))
            if int(pmq) in [i for i,j in enumerate(get_close_matches(w,data.keys()),1)]:
                return data[get_close_matches(w,data.keys())[int(pmq) - 1]]
            else:
                return "Sorry incorrect choice."
        else:
            return "Word doesn't exist. Please double-check."
    else:
        return "Word doesn't exist."

word = input("Enter the word: ")

result = meaning(word)

if type(result) == list:
    print('\n'.join(str(i)+"."+j for i,j in enumerate(result,1)))
else:
    print(result)


#s = '\n'.join(str(i)+"."+j for i,j in enumerate(result,1))
#
#def ret(s):
#    return s
#
#print(ret(s))
#
#pmq = str(input("Did you mean any of these then ? {}".
#                    format(', '.join([str(i)+"."+j for i, j in enumerate(get_close_matches("rainnn",data.keys()),1)])) + "\nSelect your choice: "))
#        
#data[get_close_matches("rainn",data.keys())[int(pmq) - 1]]
#
#4 in [i for i,j in enumerate(get_close_matches("rainn",data.keys()),1)]
#
#q = ("Did you mean any of these then ? {}".format(', '.join([str(i)+"."+j for i, j in enumerate(get_close_matches("rainnn",data.keys()),1)])) + "\n")
#print(q)
#                                             
#f = ', '.join([str(i)+"."+j for i, j in enumerate(get_close_matches("rainnn",data.keys()),1)])
#print(f)
