word = "vocatie"
accounts_list = []
for letter in word:
    accounts_list.append(letter)

print(accounts_list)

combinations = []
bank_count = len(accounts_list)
print("Bank count = ", bank_count )
indexlist = []
for i in range(0,len(accounts_list)):
    indexlist.append(0)
print(indexlist)
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
    for i in indexlist:
        if i < len(accounts_list) - 1:     #IF there exists such an i, append it, if say list is from 0 to 6 and indexvalue is 7, then that element is not included and it is now a 6 letter word with that one letter missing
            poss_set.append(accounts_list[i])
    combinations.append(poss_set)

def index_fix():
    base = bank_count
    index_count = chs_no - 1
    while index_count > 0:
        if indexlist[index_count] > (base): #used to be base-1, now i have changed the upper limit to be greater than the number of possible letters
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
                arr.remove(j)
            index_count_j += 1
        index_count_i += 1





indexlist = []
for i in range(0,len(accounts_list)):
    indexlist.append(0)
count = 1
while not end_loop:
    if distinction_check(indexlist):
        create_poss()
        count += 1
    indexlist[chs_no-1] += 1
    index_fix()
    if end_loop:
        print("End")
clear_repeats(combinations)
print(combinations)

for i in combinations:
    str = ""
    for j in i:
        str += j
    print(str)
