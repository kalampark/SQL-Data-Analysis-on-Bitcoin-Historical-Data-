def order_time(x):
    time_of_day = {
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: '10',
        11: '11',
        12: '12',
        13: '1',
        14: '2',
        15: '3',
        16: '4',
        17: '5',
        18: '6',
        19: '7',
        20: '8',
        21: '9',
        22: '10',
        23: '11',
        0: '12',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5'
    }
    return time_of_day.get(x)


def time_split(x):
    if x in [0,1,2,3,4,5,6,7,8,9,10,11]:
        return 'AM'
    if x in [12,13,14,15,16,17,18,19,20,21,22,23]:
        return 'PM'
    return x


def order_time_general(x):
    if x in [6,7,8,9,10,11,12]:
        return 'The order was made in the morning'
    if x in [13,14,15,16,17]:
        return 'The order was made in the afternoon'
    if x in [18,19,20,21,22]:
        return 'The order was made in the evening'
    if x in [23,24,0,1,2,3,4,5]:
        return 'The order was made at night'
    return x


def days_past(x):
    if x in [0,1,2,3,4,5]:
        return '0-5 days'
    if x in [6,7,8,9,10]:
        return '6-10 days'
    if x in [11,12,13,14,15]:
        return '11-15 days'
    if x in [16,17,18,19,20]:
        return '16-20 days'
    if x in [21,22,23,24,25]:
        return '21-25 days'
    if x in [26,27,28,29,30]:
        return '26-30 days'
    return x

def number_cart_order(x):
    if x <= 5 :
        x= '1-5 orders'
    elif x >5 and x <=10:
        x= '6-10 orders'
    elif x >10 and x <=15:
        x= '11-15 orders'
    elif x >15 and x <=20:
        x= '16-20 orders'
    elif x >20 and x <=25:
        x= '21-25 orders'
    elif x >25 and x <=35:
        x= '26-35 orders'    
    else:
        x= '35-100 orders'
    return x