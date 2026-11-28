import multiprocessing
import time

def Process1():
    for i in range(5):
        print("Process1 --- Iteration", i + 1)
        time.sleep(1)

def Process2():
    for i in range(5):
        print("Process2 --- Iteration", i + 1)
        time.sleep(1)

if __name__ == "__main__":
    p1 = multiprocessing.Process(target=Process1)
    p2 = multiprocessing.Process(target=Process2)

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Both processes completed")
