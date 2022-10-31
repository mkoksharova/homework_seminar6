import re

string = '0+(1+2)*3-4010/(33-7)'


def calc_str(inp):
    res = re.findall(r'[\d]+|[*/+-]', inp)
    if res[0] == '(' and res[-1] == ')':
        res.pop(0)
        res.pop(-1)
    for i in range(res.count('*')):
        f = res.index('*')
        res[f-1] = int(res[f-1])*int(res[f+1])
        res.pop(f+1)
        res.pop(f)
    for i in range(res.count('/')):
        f = res.index('/')
        res[f-1] = int(res[f-1])/int(res[f+1])
        res.pop(f+1)
        res.pop(f)
    for i in range(res.count('+')):
        f = res.index('+')
        res[f-1] = int(res[f-1])+int(res[f+1])
        res.pop(f+1)
        res.pop(f)
    for i in range(res.count('-')):
        f = res.index('-')
        res[f-1] = int(res[f-1])-int(res[f+1])
        res.pop(f+1)
        res.pop(f)
    return str(res[0])

def so_skobkami(inp):
    if len(inp)<3:
        return inp
    while '(' in inp and ')' in inp:
        temp = inp[inp.find('(')+1:inp.find(')')]
        inp = inp[:inp.find('(')]+calc_str(temp)+inp[inp.find(')')+1:]
    inp = calc_str(inp)
    return inp
    

print(f'{string} = {so_skobkami(string)}')