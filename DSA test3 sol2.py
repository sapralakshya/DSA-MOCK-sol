queue=[]

def enqueue(a):
    queue.append(a)
    return queue

def dequeue():
    queue.pop(0)
    return queue

def isempty(queue):
    if queue is None:
        print("empty")
    else:
        print("not empty")

enqueue(10)
enqueue(20)
enqueue(30)
print(queue)
dequeue()
print(queue)
isempty(queue)
