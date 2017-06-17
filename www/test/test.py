import asyncio

import sys,os
import time
import datetime

print(time.time())
print(datetime.datetime.fromtimestamp(time.time()))
print (datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d %H:%M:%S"))
print(datetime.date.today())
today = datetime.datetime.fromtimestamp(time.time())
tomorrow = datetime.date.today() + datetime.timedelta(days=-1)
print (tomorrow.strftime("%Y-%m-%d %H:%M:%S"))


import multiprocessing
from multiprocessing import Pool, Process,Queue,Lock


class Processer:
    def __init__(self,no):
        self.no = no
        self.value = 10000
    def process(self,item):
        print("no:",self.no," ", item)
        time.sleep(0.01)

manager = multiprocessing.Manager()
processer_list = manager.Queue()
q_lock = manager.Lock()
#while not processer_list.full():
    #processer_list.put()
for i in range(0,20):
    #processer_list.append(Processer(i))
    processer_list.put(Processer(i))

def doTask(item):
    processer = processer_list.get()
    processer.process(item)
    processer_list.put(processer)

list = []
start_time = time.time()
num = 0
pool = Pool(9)
for item in range(0,320):
    num += 1
    list.append(item)
    if len(list)>=100:
        ret = pool.map(doTask,list)
        print("ret:" )
        del list[:]

print("time:",time.time() - start_time)



#loop = asyncio.get_event_loop()
#loop.run_until_complete(print_sum(1, 2))
#loop.close()