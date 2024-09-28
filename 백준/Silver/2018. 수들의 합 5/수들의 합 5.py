n = int(input())

count = 1
strat_idx = 1
end_idx = 1
sum = 1

while end_idx != n:
    if sum < n:
        end_idx += 1
        sum += end_idx
    elif sum > n:
        sum -= strat_idx
        strat_idx += 1
    else:
        count += 1
        end_idx += 1
        sum += end_idx

print(count)
