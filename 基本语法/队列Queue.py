'''
@Author: your name
@Date: 2020-02-22 16:06:10
@LastEditTime: 2020-03-14 10:52:21
@LastEditors: Please set LastEditors
@Description: In User Settings Edit
@FilePath: \vscode_code\vscode_python_test\基本语法\collections deque.py
'''
#https://blog.csdn.net/weixin_43533825/article/details/89155648?depth_1-utm_source=distribute.pc_relevant.none-task&utm_source=distribute.pc_relevant.none-task
import threading,queue
import time,random
from queue import Queue
'''
q = queue.Queue()#创建一个队列

def Producer(name):
    count =0
    while count < 10:
        print('making.........')
        time.sleep(random.randrange(3))
        q.put(count)
        print('Product %s has produced %s baozi...' % (name,count))
        count += 1
        q.task_done()
        print('ok.......')
        
def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(4))
        print("..............waiting..............")
        q.join()
        data = q.get()          
        print(data)
        print('Comsumer %s has eat %s baozi...' % (name,data))        
        count += 1             
       
p1 = threading.Thread(target = Producer,args = ('厨师',))
c1 = threading.Thread(target = Consumer,args = ('食客1',)) 
c2 = threading.Thread(target = Consumer,args = ('食客2',))                

p1.start()
c1.start()
c2.start()            
'''

'''
q=Queue(maxsize=0)
 
def product(name):
    count=1
    while True:
        q.put('气球兵{}'.format(count))
        print ('{}训练气球兵{}只'.format(name,count))
        count+=1
        time.sleep(5)
def consume(name):
    while True:
        print ('{}使用了{}'.format(name,q.get()))
        time.sleep(1)
        q.task_done()
t1=threading.Thread(target=product,args=('wpp',))
t2=threading.Thread(target=consume,args=('ypp',))
t3=threading.Thread(target=consume,args=('others',))
 
t1.start()
t2.start()
t3.start()
'''
    
#FIFO先进先出
q = Queue()
for i in range(5):
    q.put(i)
while not q.empty():
    print (q.get())
print(q.empty())

#其实队列和列表类似，多线程的时候两者都可以用，都是从其内部抽取元素，然后该元素就消失直至所有元素被抽取
p = []
for i in range(5):
    p.append(i)
while len(p) > 0:
    print(p.pop())
print(len(p) == 0)
