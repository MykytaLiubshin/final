#The coding part. It codes a link into a sequence of symbols
from textwrap import fill
def coding(id):
    id1 = str(id)
    string = 'qwertyuiopasdfghjklzxcvbnm'
    id1 = "%06i"%int(id1)
    for i in range(10):
        id1 = id1.replace(str(i),string[i])
    return id1

def decode(string):
    lst = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(10):
        string = string.replace(lst[i], str(i))
    return int(string)
