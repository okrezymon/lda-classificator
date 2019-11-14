import csv
import numpy as np
import math as mth
import globals
import re
# import tkinter
# from tkinter import filedialog
from scipy import signal


def open_convert(path, number):
    counter = 0
    i = 0
    s_no = 1500  # spodziewana liczba probek, dlugosc sygnału
    results = []
    out = np.zeros([0, s_no, 6])

    with open(path) as csvfile:
        for line in csvfile:
            if len(line.split()) == 0:
                print("pusto")
            elif '#' in line:
                i += 1
                globals.labels.append(number)
                #print(i)
                if len(results) > 1:
                    # print(''.join(results))
                    # print(len(results))
                    # if len(results) == s_no:
                    #    #a_res = signal.resample(results, s_no)
                    #    a = np.array(results[0:], dtype = float)
                    #    a2 = a.reshape(1,s_no,6)
                    #    out = np.vstack([out,a2])
                    # if len(results) != s_no:
                    #a_res = signal.resample(results, s_no)

                    a_res=results
                    a = np.array(a_res[0:], dtype=float)
                    a2 = a.reshape(1, s_no, 6)
                    out = np.vstack([out, a2])
                    results = []
                    counter=0


            else:
                if counter <1500:
                    temp_l = line.strip()
                    results.append(temp_l[:-1].split(';'))
                    counter+=1
                else:
                    continue

        #print(len(results))
        if len(results) == s_no:
            a = np.array(results[0:], dtype=float)
            a2 = a.reshape(1, s_no, 6)
            out = np.vstack([out, a2])

    return out


def stack_matrices():
    j = 1
    stack = np.zeros([0, 1500, 6])
    while j < 13:
        path = 'data/' + str(j) + '.txt'
        a=open_convert(path,j)
        stack = np.vstack([stack,a])
        j+=1
    return stack


def findmax(a):
    max_value=np.max(a[:,:,:])
    return max_value
    # max = 0
    # for i in range(a.shape[0]):
    #     for j in range(a.shape[1]):
    #         if a[i][j][chn] > max:
    #             max = a[i][j][chn]
    # print(max)


def normalize(mvc):
    for i in range(globals.a.shape[0]):
        for j in range(globals.a.shape[1]):
            for k in range (globals.a.shape[2]):
                globals.a[i][j][k] = globals.a[i][j][k]/mvc
    return globals.a

#FEATURE EXTRACTION

def rms(matrix):
    sumchn1=0
    sumchn2=0
    sumchn3=0

    for i in range (matrix.shape[0]):
        for j in range(matrix.shape[1]):
            for k in range (matrix.shape[2]):
                if k==1:
                    sumchn1 +=(matrix[i][j][k]) ** 2
                if k==3:
                    sumchn2 += (matrix[i][j][k]) ** 2
                if k == 5:
                    sumchn3 += (matrix[i][j][k]) ** 2

        rms1 = mth.sqrt(sumchn1 / 1500)
        rms2 = mth.sqrt(sumchn2 / 1500)
        rms3 = mth.sqrt(sumchn3 / 1500)
        globals.feature_arr[i][0] = rms1
        globals.feature_arr[i][4] = rms2
        globals.feature_arr[i][8] = rms3





def mav(matrix):
    sumchn1 = 0
    sumchn2 = 0
    sumchn3 = 0


    for i in range (globals.a.shape[0]):
        for j in range (globals.a.shape[1]):
            for k in range (globals.a.shape[2]):
                if k==1:
                    sumchn1 += (matrix[i][j][k])
                if k==3:
                    sumchn2 += (matrix[i][j][k])
                if k == 5:
                    sumchn3 += (matrix[i][j][k])
        globals.feature_arr[i][1] = sumchn1 / 1500
        globals.feature_arr[i][5] = sumchn2 / 1500
        globals.feature_arr[i][9] = sumchn3 / 1500




def std(matrix):
    temp1 =[]
    temp2 = []
    temp3 =[]


    for i in range (globals.a.shape[0]):
        for j in range (globals.a.shape[1]):
            for k in range (globals.a.shape[2]):
                if k==1:
                    temp1.append(matrix[i][j][k])
                elif k==3:
                    temp2.append(matrix[i][j][k])
                elif k==5:
                    temp3.append(matrix[i][j][k])
        globals.feature_arr[i][2] = np.std(temp1)
        temp1.clear()
        globals.feature_arr[i][6] = np.std(temp2)
        temp2.clear()
        globals.feature_arr[i][10] = np.std(temp3)
        temp3.clear()

    # print(matrix[0,:,1])


def var(matrix):
    temp1 =[]
    temp2 =[]
    temp3 =[]


    for i in range (globals.a.shape[0]):
        for j in range (globals.a.shape[1]):
            for k in range (globals.a.shape[2]):
                if k==1:
                    temp1.append(matrix[i][j][k])
                elif k==3:
                    temp2.append(matrix[i][j][k])
                elif k==5:
                    temp3.append(matrix[i][j][k])
        globals.feature_arr[i][3]= np.var(temp1)
        temp1.clear()
        globals.feature_arr[i][7]= np.var(temp2)
        temp2.clear()
        globals.feature_arr[i][11]= np.var(temp3)
        temp3.clear()





a = stack_matrices()

max = findmax(a)

result = normalize(max)
rms(result)
mav(result)
std(result)
var(result)

print(len(globals.labels))
print(globals.labels[:250])
print(globals.labels[250])







