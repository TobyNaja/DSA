def bubbleSort(lst,last):
    time = 0
    current = 0
    sort = False
    while current <= last and sort is False:
        walker = last
        sort = True
        while walker > current:
            if lst[walker] < lst[walker-1]:
                sort = False
                lst[walker],lst[walker-1] = lst[walker-1],lst[walker]
            walker -= 1
            time += 1
        current += 1
        print(lst)
    print("Comparison times:",time)
    
def main():
    import json
    lst = json.loads(input())
    last = int(input())
    bubbleSort(lst,last)
main() 
 