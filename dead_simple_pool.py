import threading
import time
import sys
import numpy as np
from multiprocessing import cpu_count
from multiprocessing import Pool, freeze_support
import time
import sys

def do_more_work(a,b):
    time.sleep(a)
    print(a,b)
    return(a+b)

def helper(input_values):
    function = input_values[0]
    index = input_values[1]
    arguments = input_values[2:]
    output = function(*arguments)
    return [index,output]
    

if __name__ == '__main__':
    function= do_more_work
    As = np.sort(np.random.rand(20))
    Bs = np.sort(np.random.rand(20))
    args = [[function,index,a,b] for index,a,b in zip(range(len(As)),As,Bs)]
    
    
    freeze_support()        
    p=Pool(cpu_count())
    results=["-"]*len(args)   
    for [i,output] in p.imap_unordered(helper, args):
        results[i]=output
        sys.stderr.write('\ndone {0}%'.format(100*i/len(args)))        
    p.terminate()
    sys.stderr.write('\ndone 100.0%')    

    
