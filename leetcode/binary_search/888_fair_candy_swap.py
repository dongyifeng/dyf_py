def fair_candy_swap(alice_sizes, bob_sizes):
    alice_sum = sum(alice_sizes)
    bob_sum = sum(bob_sizes)

    alice_sub_map = dict([(alice_sum - 2 * alice_sizes[i], i) for i in range(len(alice_sizes))])
    bob_sub_list = [bob_sum - 2 * item for item in bob_sizes]

    for i in range(len(bob_sub_list)):
        if bob_sub_list[i] in alice_sub_map:
            j = alice_sub_map[bob_sub_list[i]]
            return [alice_sizes[j], bob_sizes[i]]


print(fair_candy_swap([1, 1], [2, 2]))
print(fair_candy_swap([1, 2], [2, 3]))
print(fair_candy_swap([2], [1, 3]))
print(fair_candy_swap([1, 2, 5], [2, 4]))
