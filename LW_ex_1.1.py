def calc_time():
    res = 0
    chosen = ''
    time = int(('input seconds from the beginning of the day'))
    p = int(input('Choose time convertion : 1 година'))
    n = int(input('Choose time convertion : 2 хвилина'))
    s = int(input('Choose time convertion : 3 секунда'))
    if p == 1:
        choosen = 'година'
        res = (86400 - time)/ 60 /60
    elif n ==2:
        choosen = 'хвилина'
        res = (86400 - time)/60
    elif s == 3:
        choosen = 'секунда'
        res = 86400 - time
    print(f'{res}{choosen} left')



calc_time()

