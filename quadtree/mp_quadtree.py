import multiprocessing as mp
from queue import Empty

e = mp.Event()
q = mp.JoinableQueue()

def worker():
    while True:
        try:
            task = q.get(timeout=1)

            # do some work
            print(task)
            
            q.task_done()
        except Empty:  # queue.Empty
            if e.is_set():
                return
        

def main():
    q.put('foo')

    p = mp.Process(target=worker)
    p.start()

    q.join()
    e.set()
    p.join()
    print('Done!')

main()