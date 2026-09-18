# comparo dos vecinos si estan al reves los intercambio y repito el proceso 
# hast que nadie mas se mueva bubble sort

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            global comparaciones
            comparaciones += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                global intercambios
                intercambios += 1
                swapped = True
        if not swapped:
            break
    return arr

arr = [64, 25, 12, 22, 11, 90, 45, 33]

comparaciones = 0
intercambios = 0

print(bubble_sort(arr))
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)

#buscar el más pequeño y ponerlo al 
# principio selection sort

comparaciones = 0
intercambios = 0

def selection_sort(arr):
    global comparaciones, intercambios
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparaciones += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        intercambios += 1
    return arr

print(selection_sort(arr))
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)

def insertion_sort(arr):
    global comparaciones, intercambios
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            comparaciones += 1
        arr[j + 1] = key
        intercambios += 1
    return arr

comparaciones = 0
intercambios = 0

print(insertion_sort(arr))
print("Comparaciones:", comparaciones)
print("Intercambios:", intercambios)

# datos: [64, 25, 12, 22, 11, 90, 45, 33]