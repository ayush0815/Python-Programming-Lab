def sorted_list (x):
    copy = x.copy()
    return x == sorted(x)

    ls = list(input())
    out = sorted_list(ls)
    print('sorted' if out else 'unsorted')