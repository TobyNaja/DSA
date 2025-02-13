def PointSorting(data):
    new_data = []
    for i in data:
        k = i.split(" ")
        total = sum(int(j) for j in k)
        new_data.append(total)
        
    for current in range(1, len(data)):
        hold = new_data[current]
        hold_data = data[current]
        walker = current - 1
        
        while walker >= 0 and (hold < new_data[walker] or (hold == new_data[walker] and int(hold_data.split(" ")[1]) > int(data[walker].split(" ")[1]))):
            new_data[walker + 1] = new_data[walker]
            data[walker + 1] = data[walker]
            walker -= 1
        
        new_data[walker + 1] = hold
        data[walker + 1] = hold_data
    for i in data:
        print(i)


def main(loop):
    pointlist = []
    for _ in range(loop):
        num = int(input())
        listx = []
        for _ in range(num):
            x = input()
            listx.append(x)
        pointlist.append(listx)
    for i in pointlist:
        PointSorting(i)
main(int(input()))
            