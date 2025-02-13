def insertionSort(lst, last):
    time = 0
    for current in range(1, last + 1):
        hold = lst[current]
        walker = current - 1
        
        while walker >= 0 and hold < lst[walker]:
            if hold[0] == lst[walker][0]:
                if int(hold[1:]) > int(lst[walker][1:]):
                    lst[walker + 1] = hold
                    break
            lst[walker + 1] = lst[walker]
            walker -= 1
            time += 1
        lst[walker + 1] = hold
        time += 1 if walker >= 0 else 0
        print(lst)
    print("Comparison times:",time)
        
def main():
    import json
    lst = json.loads(input())
    last = int(input())
    insertionSort(lst,last)
main()
