import time
import psutil
from concurrent.futures import ThreadPoolExecutor
from threading import Thread
import ctypes
import numpy as np
import os

    # Cargar librería compartida
lib = ctypes.CDLL('./shared_code.so')

    # Definir los tipos de argumentos de la función C
lib.save_csv.argtypes = [
        ctypes.c_char_p,                      # path
        ctypes.POINTER(ctypes.c_double),     # timestamps
        ctypes.POINTER(ctypes.c_double),     # cpu
        ctypes.POINTER(ctypes.c_double),     # mem
        ctypes.c_int                         # número de muestras
    ]

def heavy_task():
        total = 0
        for i in range(100_000_000):
            total += i % 2
        return total

def monitor_resources(interval=0.5, stats_list=None, stop_flag=None):
        while not stop_flag["stop"]:
            cpu = psutil.cpu_percent(interval=interval)
            mem = psutil.virtual_memory().used / (1024 ** 2)  # en MB
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

        # Preparar arrays para pasar a C
        n = len(stats)
        timestamps = np.array([s[0] for s in stats], dtype=np.float64)
        cpu = np.array([s[1] for s in stats], dtype=np.float64)
        mem = np.array([s[2] for s in stats], dtype=np.float64)

        # Llamar a la función C para guardar el CSV
        lib.save_csv(
            results_path.encode('utf-8'),
            timestamps.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            cpu.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            mem.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
            n
        )

        return total_time

    # Ruta compartida dentro del contenedor o VM
shared_dir = "/mnt/shared_results"
if not os.path.exists(shared_dir):
        raise RuntimeError(f"❌ Carpeta compartida no existe: {shared_dir}")

    # Ejecutar benchmarks para diferentes números de hilos
for n_threads in [1, 2, 4, 6, 8]:
        output_file = f"{shared_dir}/run_{n_threads}_threads.csv"
        benchmark(n_threads, output_file)
