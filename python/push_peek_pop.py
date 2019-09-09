

def stack_push(s, value):
    s.append(value)

def stack_peek(s):
    return s[-1]

def stack_pop(s):
    return s.pop()

stack = []

stack_push(stack, 10)
stack_push(stack, 20)
stack_push(stack, 30)
stack_push(stack, 40)
stack_push(stack, 50)
stack_push(stack, 300)

print(stack)

print(stack_peek(stack))
print(stack)

print(stack_pop(stack))
print(stack)

new_stack = []
while stack:
    value = stack_pop(stack)
    stack_push(new_stack, value)

print(stack)
print(new_stack)