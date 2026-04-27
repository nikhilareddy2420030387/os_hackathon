# sync_deadlock_demo.py

import threading

# Shared variable
counter = 0

# Lock for synchronization
lock = threading.Lock()

# -------------------------------
# Part A: Race Condition (Unsafe)
# -------------------------------
def increment_unsafe(n):
    global counter
    for _ in range(n):
        counter += 1


# -------------------------------
# Part B: With Synchronization
# -------------------------------
def increment_safe(n):
    global counter
    for _ in range(n):
        with lock:
            counter += 1


# -------------------------------
# Part C: Deadlock Demonstration
# -------------------------------
lock1 = threading.Lock()
lock2 = threading.Lock()

def thread1():
    with lock1:
        print("Thread 1 acquired lock1")
        with lock2:
            print("Thread 1 acquired lock2")


def thread2():
    with lock2:
        print("Thread 2 acquired lock2")
        with lock1:
            print("Thread 2 acquired lock1")


# -------------------------------
# Main Execution
# -------------------------------
if __name__ == "__main__":
    n = int(input("Enter number of increments per thread: "))

    # Race Condition
    counter = 0
    t1 = threading.Thread(target=increment_unsafe, args=(n,))
    t2 = threading.Thread(target=increment_unsafe, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("\n--- Race Condition (Unsafe) ---")
    print("Final Counter Value:", counter)

    # Synchronization
    counter = 0
    t1 = threading.Thread(target=increment_safe, args=(n,))
    t2 = threading.Thread(target=increment_safe, args=(n,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("\n--- After Synchronization ---")
    print("Final Counter Value:", counter)

    # Deadlock
    print("\n--- Deadlock Demonstration ---")
    d1 = threading.Thread(target=thread1)
    d2 = threading.Thread(target=thread2)
    d1.start()
    d2.start()
    d1.join()
    d2.join()