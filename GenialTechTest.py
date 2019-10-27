def rev_list(in_lst):
    n = len(in_lst)
    out_lst = []
    for i in range(n-1,-1,-1):
        out_lst.append(in_lst[i])
    return out_lst


if __name__ == '__main__':
    lst1 = [1, 2, 4, 8, 16, 32]
    lst2 = rev_list(lst1)
    print(str(lst1) + ' -> ' + str(lst2))
