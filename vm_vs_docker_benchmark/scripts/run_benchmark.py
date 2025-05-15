import time
import psutil
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import csv
import os

def heavy_task():
    total = 0
    for i in range(100_000_000):
        total += i % 2
    return total

def monitor_resources(interval=0.5, stats_list=None, stop_flag=None):
    while not stop_flag["stop"]:
        cpu = psutil.cpu_percent(interval=interval)
        mem = psutil.virtual_memory().used / (1024 ** 2)  # MB
        stats_list.append((time.time(), cpu, mem))

def benchmark(num_threads, results_path):
    print(f"🔧 Ejecutando benchmark con {num_threads} hilos...")
    stats = []
    stop_flag = {"stop": False}

    monitor_thread = Thread(target=monitor_resources, args=(0.5, stats, stop_flag))
    monitor_thread.start()

    start_time = time.time()
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        _ = list(executor.map(lambda _: heavy_task(), range(num_threads)))
    end_time = time.time()

    stop_flag["stop"] = True
    monitor_thread.join()

    total_time = end_time - start_time
    print(f"⏱️ Tiempo total: {total_time:.2f} segundos")

    os.makedirs(os.path.dirname(results_path), exist_ok=True)
    with open(results_path, mode='w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "cpu_percent", "memory_used_MB"])
        writer.writerows(stats)

    print(f"📁 Resultados guardados en {results_path}")
    return total_time


# 🔁 Ejecutar para 1, 2, 4, 6 y 8 hilos
for n_threads in [1, 2, 4, 6, 8]:
    output_path = f"results/run_{n_threads}_threads.csv"
    benchmark(n_threads, output_path)
