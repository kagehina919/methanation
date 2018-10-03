import os

def get_ref_dict():
    refs = {}
    with open('ref.txt') as f:
        lines_ = f.readlines()
    
    for num, lines in enumerate(lines_):
        ref = '.'.join(lines.split('.')[1:])
        refs[num+1] = ref
    
    print(refs)
    return refs

def get_from_csv():
    dictt = {}
    lis = []
    with open('rows.txt') as f:
        lines_ = f.readlines()
    
    for idx, lines in enumerate(lines_):
        print(lines.split(','))
        refs = list(map(int, lines.split(',')[:-1]))
        lis += refs
        dictt[idx+1] = refs
    
    print(lis)

    to_ep = []
    for i in range(len(lis)):
        to_ep.append((lis[i], i+1))

    to_ep.sort(key=lambda x: x[0])
    print(to_ep)
    return to_ep

def merge(refs, to_ep):
    new_lis = {}
    for tup in to_ep:
        new = tup[1]
        old = tup[0]
        new_lis[new] = refs[old]
    print(new_lis)

    keys = []   
    for key in new_lis:
        keys.append(key)
    
    keys.sort()

    for _ in keys:
        print(str(_) + ". " + new_lis[_])
    
    dictt = {}
    lis = []
    with open('rows.txt') as f:
        lines_ = f.readlines()
    
    for idx, lines in enumerate(lines_):
        refs = list(map(int, lines.split(',')[:-1]))
        new_refs = []
        for _ in refs:
            new_refs.append(str(to_ep[_-1][1]))

        # print(','.join(new_refs))    


if __name__ == '__main__':
    merge(get_ref_dict(), get_from_csv())