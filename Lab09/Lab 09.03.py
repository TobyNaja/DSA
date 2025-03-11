def lcs(str1, str2):
    n = len(str1)
    mylist = [[0 for _ in range(n)] for _ in range(n)]
    longs = 0
    row = 0
    for i in range(n):
        for j in range(n):
            if str1[i] == str2[j]:
                mylist[i][j] = mylist[i-1][j-1] + 1
                
            if mylist[i][j] > longs:
                longs = mylist[i][j]
                row = i
                
    if longs > 0:
        print(str1[row-longs+1: row+1])
        print(longs)
    else:
        print("No common substring.")

def main():
    str1 = input()
    str2 = input()
    lcs(str1,str2)
    
main()