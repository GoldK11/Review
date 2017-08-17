
# coding: utf-8

# In[5]:


class Queue(list):
    #enqueue
    enqueue = list.append
    #dequeue
    def dequeue(self):
        return self.pop(0)
    #peek
    def peek(self):
        return self[0]
    #empty
    def empty(self):
        if not self:
            return True
        else:
            return False


# In[6]:


if __name__ == '__main__':
    q = Queue()
    
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    while not q.empty():
        data = q.dequeue()
        print(data,end = '  ')
        


# In[ ]:




