def selectionSort(lst,last):
    time = 0
    for current in range(last):
        smallest = current
        walker = current + 1
        
        while walker <= last:
            time += 1
            if lst[walker] < lst[smallest]:
                smallest = walker
            walker += 1
        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)
    print("Comparison times:",time)
        
def main():
    import json
    lst = json.loads(input())
    last = int(input())
    selectionSort(lst,last)
main() 