# Qn 4 : Count multiples of 1-10 in list

def Count_multiples(nums):
    freq = {}
    for i in range(1, 10):
        count= 0
        for j in nums:
            if j % i == 0:
                count += 1
        freq[i]= count

    return freq


values= [1,2,8,9,12,46,76,82,15,20,30]

value = Count_multiples(values)
print(value)
