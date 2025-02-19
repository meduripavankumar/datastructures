from multiprocessing import Process,Manager
import time

def process1(shared_dict):
    print("Process 1 add 10 to the global val")
    shared_dict["global_val"] +=10
    return shared_dict

def process2(shared_dict):
    print("Process 2 removes 10 to the global val")
    shared_dict["global_val"] -=10
    return shared_dict

def main():
    start_time = time.time()
    with Manager() as manager:
        shared_dict=  manager.dict({"global_val":0})
        p1 = Process(target=process1,args=(shared_dict,))
        p2 = Process(target=process2,args=(shared_dict,))
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        end_time = time.time()
        print("val of global var ",shared_dict["global_val"])
        print("time taken ",end_time-start_time)

if __name__ == '__main__':
    main()

                     

