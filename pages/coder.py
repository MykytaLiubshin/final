#The coding part. It codes a link into a sequence of symbols
from textwrap import fill
from django.shortcuts import redirect

def coding(id):
    """
    coding(id,/) takes an id 
    returns it coded to a 6-symbol sequence
    """
    id1 = str(id)
    string = 'qwertyuiopasdfghjklzxcvbnm'
    try:
        id1 = "%06i"%int(id1)
    except:
        return redirect(https://linksho.herokuapp.com/home/)
    for i in range(10):
        id1 = id1.replace(str(i),string[i])
    return id1

def decode(string):
    """
    decode(string,/) takes a string
    returns it decoded from 6-symbol sequence to a number
    that represents it's id in the DB
    """
    lst = 'qwertyuiopasdfghjklzxcvbnm'
    for i in range(10):
        string = string.replace(lst[i], str(i))
    return int(string)
