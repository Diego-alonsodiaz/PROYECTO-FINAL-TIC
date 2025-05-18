# PROYECTO-FINAL-TIC
# 🧪 Evaluación Comparativa de Rendimiento: Máquinas Virtuales vs Contenedores Docker

Este proyecto evalúa el rendimiento de contenedores Docker frente a máquinas virtuales VirtualBox, utilizando un conjunto de pruebas controladas y análisis comparativo detallado.

---

## 📘 ¿Qué son las Máquinas Virtuales y los Contenedores?

### 🖥️ Máquinas Virtuales (VM)
Una VM simula un hardware físico completo, permitiendo ejecutar un sistema operativo completo sobre un hipervisor. Proporcionan alto aislamiento, pero con mayor sobrecarga de recursos.

### 📦 Contenedores (Docker)
Los contenedores ejecutan procesos aislados que comparten el kernel del sistema operativo. Son más livianos, rápidos de iniciar y escalan eficientemente, aunque con menor aislamiento comparado a las VMs.

---

## 📁 Estructura del Proyecto

.
├── README.md
├── install.ipynb
└── vm_vs_docker_benchmark/
├── notebooks/
│ ├── comparar_resultados.ipynb
│ └── vm_vs_docker.ipynb
├── results/
│ ├── Resultados Docker/
│ │ ├── run_1_threads.csv
│ │ └── run_2_threads.csv
│ └── Resultados VM/
│ ├── run_1_threads.csv
│ ├── run_2_threads.csv
│ ├── run_4_threads.csv
│ ├── run_6_threads.csv
│ └── run_8_threads.csv
└── scripts/
├── Dockerfile
├── run_benchmark.py
├── shared_code.c
└── shared_code.so

---

## ⚙️ Requisitos del Proyecto

- Python 3.13.3
- Docker
- VirtualBox
- pip (gestor de paquetes Python)

---

## 📦 Bibliografía y Recursos Utilizados

- **Docker**: Plataforma de contenedores para desarrollar, distribuir y ejecutar aplicaciones rápidamente ([docs](https://docs.docker.com/)).
- **Python 3.13.3**: Lenguaje utilizado para el análisis de datos y automatización.
- **VirtualBox**: Software de virtualización para crear y gestionar máquinas virtuales ([docs](https://www.virtualbox.org/)).
- **Jupyter Notebook**: Entorno interactivo para análisis y visualización de datos ([jupyter.org](https://jupyter.org)).

---

## 🧰 Librerías necesarias

Instalación recomendada mediante pip:

```bash
pip install jupyter pandas matplotlib psutil
Jupyter: Para visualizar y ejecutar notebooks interactivos.

Pandas: Manipulación y análisis de estructuras de datos (CSV).

Matplotlib: Gráficos y visualizaciones.

Psutil: Obtención de estadísticas de uso del sistema.

📏 Métricas Medidas
Uso de CPU (% bajo carga y reposo)

Uso de RAM

Tiempo de ejecución de tareas computacionales

Tiempo de arranque de contenedor/VM

Tiempo de despliegue de aplicación de prueba

Comparativa multi-thread (1, 2, 4, 6, 8 hilos)

Rendimiento de código en C compartido entre entornos

📊 Estructura de Resultados
Los resultados se almacenan en archivos .csv en la carpeta results/:

Resultados Docker: contiene las pruebas ejecutadas dentro de contenedores Docker.

Resultados VM: contiene las pruebas ejecutadas en la máquina virtual.

Cada archivo corresponde a una prueba con distinto número de hilos (run_1_threads.csv, etc).

📈 Comparativa y Análisis (Notebook)
En los notebooks comparar_resultados.ipynb y vm_vs_docker.ipynb se incluye:

Gráficos comparativos del rendimiento entre VM y Docker.

Evaluación visual de escalabilidad por hilos.

Comentarios detallados sobre el comportamiento de cada entorno.

Conclusiones respaldadas por datos medidos.

Los gráficos permiten apreciar diferencias en consumo de CPU, RAM, y tiempo de ejecución por número de hilos.

✅ Conclusiones
Criterio	Docker	VirtualBox
Tiempo de arranque	✅ Rápido (~1s)	❌ Lento (~30s)
Consumo de recursos	✅ Bajo	❌ Alto
Aislamiento	❌ Parcial (kernel host)	✅ Completo
Portabilidad	✅ Muy alta	⚠️ Moderada
Rendimiento con multithread	✅ Escala eficientemente	⚠️ Menor eficiencia

Docker se muestra como una alternativa ágil y eficiente para despliegue rápido y pruebas ligeras, mientras que las VMs siguen siendo necesarias en contextos donde el aislamiento completo es crítico.

📚 Referencias
Docker: https://docs.docker.com/

VirtualBox: https://www.virtualbox.org/wiki/Documentation

Python: https://www.python.org/doc/

Ficheros CSV de resultados (carpeta /results)

Notebooks comparativos (carpeta /notebooks)