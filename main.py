#Jonas York
#U3 L5
#Selection sort

def SelectionSort(numlist):
  
  for item in range(len(numlist)):
    currentIndex = item
    for otherItem in range(item + 1, len(numlist)):
      if numlist[currentIndex] > numlist[otherItem]:
        currentIndex = otherItem
    numlist[item], numlist[currentIndex] = numlist[currentIndex],  numlist[item]

  return numlist

def main():
  list1 = [66, 28, 1, 40, 70]

  list = SelectionSort(list1)
  print(list)

if __name__ == "__main__":
  main()
