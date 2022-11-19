def run2(letters, target):
    for item in letters:
        if item > target:
            return item
    return letters[0]


def run(letters, target):
    n = len(letters)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) >> 1
        if target < letters[mid]:
            right = mid - 1
        else:
            left = mid + 1
    if left > n - 1: return letters[0]
    return letters[left]


print(run(['c', 'f', 'j'], 'a'))
print(run(['c', 'f', 'j'], 'c'))
print(run(['c', 'f', 'j'], 'd'))
print(run(['c', 'f', 'j'], 'g'))
print(run(['c', 'f', 'j'], 'j'))
print(run(['c', 'f', 'j'], 'k'))

print("--" * 10)

print(run2(['c', 'f', 'j'], 'a'))
print(run2(['c', 'f', 'j'], 'c'))
print(run2(['c', 'f', 'j'], 'd'))
print(run2(['c', 'f', 'j'], 'g'))
print(run2(['c', 'f', 'j'], 'j'))
print(run2(['c', 'f', 'j'], 'k'))
