// shared_code.c

#include <stdio.h>
#include <stdlib.h>

void save_csv(const char* path, double* timestamps, double* cpu, double* mem, int n) {
    FILE* file = fopen(path, "w");
    if (!file) {
        printf("❌ No se pudo abrir el archivo: %s\n", path);
        return;
    }

    fprintf(file, "timestamp,cpu_percent,memory_used_MB\n");
    for (int i = 0; i < n; i++) {
        fprintf(file, "%.6f,%.2f,%.2f\n", timestamps[i], cpu[i], mem[i]);
    }

    fclose(file);
    printf("✅ Resultados guardados en %s\n", path);
}
