/* Bubble Sort */
void bubbleSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            comparaciones++;
            if (arr[j] > arr[j + 1]) {
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                intercambios++;
            }
        }
    }
}

cout << bubbleSort(arr, n) << endl;
cout << "Comparaciones: " << comparaciones << endl;
cout << "Intercambios: " << intercambios << endl;

/*contar cuantas comparaciones e intercambios se hacen en cada algoritmo e imprimir el resultado*/
int intercambios = 0;
int comparaciones = 0;

/* Selection Sort */
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        for (int j = i + 1; j < n; j++) {
            comparaciones++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
                intercambios++;
            }
        }
        int temp = arr[minIdx];
        arr[minIdx] = arr[i];
        arr[i] = temp;
    }
}
cout << selectionSort(arr, n) << endl;
cout << "Comparaciones: " << comparaciones << endl;
cout << "Intercambios: " << intercambios << endl;

/* Insertion Sort */
void insertionSort(int arr[], int n) {
    for (int i = 1; i < n; i++) {
        comparaciones++;
        int key = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > key) {
            intercambios++;
            arr[j + 1] = arr[j];
            j--;
        }
        arr[j + 1] = key;
    }
}
cout << insertionSort(arr, n) << endl;
cout << "Comparaciones: " << comparaciones << endl;
cout << "Intercambios: " << intercambios << endl;