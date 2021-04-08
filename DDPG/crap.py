def num_duplicates(ls):
    c = 0
    non_duplicates = 0
    for l in ls:
        t_c = 0
        temp = [0,0,0,0,0,0,0,0,0]
        for i in l:
            if i != 0:
                temp[i-1] += 1
        
        for t in temp:
            if t > 1:
                t_c += 1
        if t_c < 1:
            non_duplicates += 1
        else:
            c += t_c
    return c,non_duplicates

ls = [[1, 9, 4, 3, 2, 5, 6, 7, 7], [3, 0, 0, 0, 9, 9, 0, 6, 0], [2, 6, 9, 5, 5, 1, 5, 4, 4]]
print(num_duplicates(ls))