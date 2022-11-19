def reverse_stack(stack):
    if not stack:
        return
    num = get_stack_last(stack)
    reverse_stack(stack)
    stack.append(num)


def get_stack_last(stack):
    res = stack.pop()
    if not stack:
        return res
    last = get_stack_last(stack)
    stack.append(res)
    return last


stack = [1, 2, 3]
#
# while stack:
#     print(stack.pop())
#
# stack = [1, 2, 3]
# reverse_stack(stack)
# print(stack)
#
# while stack:
#     print(stack.pop())

print(get_stack_last(stack))

