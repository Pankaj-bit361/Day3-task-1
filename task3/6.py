



from queue import Queue

class Stack:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, value):
        self.queue2.put(value)
    
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
    
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

stack = Stack()
output = []


stack.push(1)
stack.push(2)


output.append(stack.pop())
stack.push(3)
output.append(stack.pop())
output.append(stack.pop())

output_str = ", ".join([str(item) for item in output])
print(output_str)
