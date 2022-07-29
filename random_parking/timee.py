
from random import randrange
from datetime import timedelta
from datetime import datetime



def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)
def tim():     
    d1 = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    d2 = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    m=random_date(d1, d2)
    m=int(str(m)[-8:-6]) 
    if m<=1 and m>0 :
        m=20
    elif m<=10:
        m=m*10
    else: 
        m=m*5   
    return m