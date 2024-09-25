accounts_list = [23, 45, 65, 26, 75, 29]
bank_count = len(accounts_list)
print("Bank count = ", bank_count )
indexlist = [0, 0, 0]
combinations = []
chs_no = len(indexlist)
print("choose no =", chs_no)
end_loop = False


def variation_fill(nth_row):
    while indexlist[chs_no - nth_row] < bank_count:
        grouped_set = []
        for i in indexlist:
            grouped_set.append(accounts_list[i])
        combinations.append(grouped_set)
        indexlist[chs_no - nth_row] += 1


def create_poss():
    poss_set = []
    print("creating using", indexlist)
    for i in indexlist:
        print(i)
        poss_set.append(accounts_list[i])
    combinations.append(poss_set)

def index_fix():
    base = bank_count
    index_count = chs_no - 1
    while index_count > 0:
        if indexlist[index_count] > (base-1):
            indexlist[index_count - 1] += int(indexlist[index_count]/base)
            indexlist[index_count] = indexlist[index_count] - base
        index_count -= 1
    if indexlist[0] >= base - 1:
        global end_loop
        end_loop = True
    else:
        end_loop = False


def distinction_check(arr):
    distinction = True
    temp_arr = arr.copy()
    for i in temp_arr:
        temp_arr.remove(i)
        for j in temp_arr:
            if i == j:
                print(i , j)
                distinction = False
                break
    if distinction:
        return True
    else:
        return False


def clear_repeats(arr):
    for k in arr:
        k.sort()
    index_count_i = 0
    for i in arr:
        index_count_j = 0
        for j in arr:
            if i == j and not index_count_i == index_count_j:
                print("removing ", j)
                arr.remove(j)
            index_count_j += 1
        index_count_i += 1





indexlist = [0, 0, 0]
count = 1
while not end_loop:
    print(indexlist)
    if distinction_check(indexlist):
        create_poss()
        print("comination formed")
        print(count)
        count += 1
    indexlist[chs_no - 1] += 1
    index_fix()
    if end_loop:
        print("End")
clear_repeats(combinations)
print(combinations)
print("Total combinations formed =", len(combinations))
print(distinction_check(combinations))


