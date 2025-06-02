import multiprocessing
import os

def busy_loop():
    while True:
        pass  # Infinite loop to keep the CPU busy

if __name__ == "__main__":
    num_cores = os.cpu_count()  # Includes hyperthreads
    print(f"Starting busy loop on {num_cores} cores...")
    processes = []
    for _ in range(num_cores):
        p = multiprocessing.Process(target=busy_loop)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()