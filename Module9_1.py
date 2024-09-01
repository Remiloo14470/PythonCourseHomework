def apply_all_func(int_list, *functions):
    results = {}
    for func in functions:
        res = func(int_list)
        results[func.__name__] = res
    return results

def min_(list):
    return min(list)

def max_(list):
    return max(list)

def len_(list):
    return len(list)

def sum_(list):
    return sum(list)

def sorted_(list):
    return sorted(list)


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
