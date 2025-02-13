def selectionSort(lst,last):
    time = 0
    for current in range(last):
        smallest = current
        walker = current + 1
        
        for walker in range(current + 1, last + 1):
            time += 1
            if lst[walker][0] == lst[smallest][0]:
                if int(lst[walker][1:]) < int(lst[smallest][1:]):
                    smallest = walker
            elif lst[walker] < lst[smallest]:
                smallest = walker
                
        lst[current], lst[smallest] = lst[smallest], lst[current]
        print(lst)
    print("Comparison times:",time)
        
def main():
    import json
    lst = json.loads(input())
    last = int(input())
    selectionSort(lst,last)
main() 