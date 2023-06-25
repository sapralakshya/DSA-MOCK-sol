stack=[]
def push(a):
    stack.append(a)
    return stack
def pop ():
    stack.pop()
    return stack

def isempty(stack):
    if stack is None:
        print("empty")
    else:
        print("not empty")

push(10)
push(20)
push(30)
print(stack)
pop()
print(stack)
isempty(stack)



