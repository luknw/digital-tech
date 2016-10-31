import csv
import xlsxwriter

def karnaugh(seg):
    array = [['x', bin(0), bin(1), bin(3), bin(2)]]
    for i in range(0, 4):
        arr = []
        for j in range(0, 4):
            arr.append(seg((4 * i + j) % 10))
        appendix = [bin(i)] + arr
        array.append(appendix)
    tmp = array[4]
    array[4] = array[3]
    array[3] = tmp
    for i in range(0,5):
        print(array[i])
    print()
    return array

def seg0(num):
    if num in [0, 2, 3, 6, 7, 8, 9]:
        return 1
    else:
        return 0

def seg1(num):
    if num in [0, 4, 5, 6, 8, 9]:
        return 1
    else:
        return 0

def seg2(num):
    if num in [0, 1, 2, 3, 4, 7, 8, 9]:
        return 1
    else:
        return 0

def seg3(num):
    if num in [2, 3, 4, 5, 6, 8, 9]:
        return 1
    else:
        return 0

def seg4(num):
    if num in [0, 2, 6, 8]:
        return 1
    else:
        return 0

def seg5(num):
    if num in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        return 1
    else:
        return 0

def seg6(num):
    if num in [0, 2, 3, 5, 6, 8, 9]:
        return 1
    else:
        return 0



karnaugh(seg0)
karnaugh(seg1)
karnaugh(seg2)
karnaugh(seg3)
karnaugh(seg4)
karnaugh(seg5)
karnaugh(seg6)

segs=[seg0,seg1,seg2,seg3,seg4,seg5,seg6]
workbook = xlsxwriter.Workbook('7seg.xlsx')

for s in range (0,7):
    worksheet = workbook.add_worksheet('seg'+str(s))
    for i in range (0,5):
        for j in range (0,5):
            worksheet.write(i,j, karnaugh(segs[s])[i][j])

workbook.close()







