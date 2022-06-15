
def encontrarMenor(arr):
  menor = arr[0]
  menor_index = 0
  for i in range(1, len(arr)):
    if arr[i] < menor:
      menor_index = i
      menor = arr[i]
  return menor_index

def selectionSort(arr):
  novoArr = []
  for i in range(len(arr)):
      # Finds the smallest element in the array and adds it to the new array
      menor = encontrarMenor(arr)
      novoArr.append(arr.pop(menor))
  return novoArr

print(selectionSort([1, 3, 6, 2, 10]))