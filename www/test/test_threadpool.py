import sys
import time
sys.path.append("../")
from common.thread_pool import ThreadPool
from common.loghandler import getLogger
pool = ThreadPool(thread_num = 30,task_max_size = 100)

log = getLogger(name='test')

def fuck(i):
    print('fuck %d'%i)
    time.sleep(0.1)
    log.info('fuck %d'%i)

for i in range(0,200):
    pool.queue_task(fuck,(i,))

pool.join_all()