
# coding: utf-8

# In[4]:


class Stack(list):
    #push
    push = list.append
    #pop
    #구현안함

    #empty
    def empty(self):
        if not self:
            return True
        else:
            return False
    #peek
    def peek(self):
        return self[-1]


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    while not s.empty():
        data = s.pop()
        print(data,end = '  ')
        

