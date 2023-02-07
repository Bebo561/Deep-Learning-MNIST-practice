# -*- coding: utf-8 -*-
"""Assignment 2_Carlodavid Soto.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E6mD0EpRpy0PRC5LNWG6NbBn74S0xFB7
"""

from keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

(x_train, y_train), (x_test, y_test) = mnist.load_data()

def shuffle(x_train_01, y_train_01):
  num_train_img = x_train_01.shape[0]
  train_ind = np.arange(0, num_train_img)
  
  train_ind_s = np.random.permutation(train_ind)

  x_train_01=x_train_01[train_ind_s,:,:]
  y_train_01 = y_train_01[train_ind_s]

  #selecting 500 of data set
  x_valid_01 = x_train_01[0:500, :, :]
  y_valid_01 = y_train_01[0:500]
  #rest of data set
  x_train_01 = x_train_01[500:, :, :]
  y_train_01 = y_train_01[500:]
  return x_valid_01, y_valid_01 , x_train_01, y_train_01



def digitplot(x_temp , y_temp, callctr):
  if callctr == 0:
    ctr = 1
    for i in range(5):
      x_train_d = x_temp[y_temp==i,:, :]
      x_train_i=x_train_d[10,:,:]
      plt.subplot(2, 5, ctr)
      plt.imshow(x_train_i,cmap='gray')
      plt.title('Label: ' + str(i))
      ctr+= 1
    for i in range(5,10):
      x_train_d = x_temp[y_temp==i,:, :]
      x_train_i=x_train_d[10,:,:]
      plt.subplot(2, 5, ctr)
      plt.imshow(x_train_i,cmap='gray')
      plt.title('Label: ' + str(i))
      ctr+= 1
    plt.show()
  else:
    ctr = 1
    for i in range(5):
      x_train_i=x_temp[i,:,:]
      digit = y_temp[i]
      
      plt.subplot(2, 5, ctr)
      plt.imshow(x_train_i,cmap='gray')
      plt.title('Label: ' + str(digit))
      ctr+= 1
    for i in range(5, 10):
      x_train_i=x_temp[i,:,:]
      digit = y_temp[i]
      
      plt.subplot(2, 5, ctr)
      plt.imshow(x_train_i,cmap='gray')
      plt.title('Label: ' + str(digit))
      ctr+= 1
    plt.show()
  
def finplot(xzerolist, yzerolist, xeightlist, yeightlist):
    xzerolist = np.array(xzerolist, dtype=float)
    yzerolist = np.array(yzerolist, dtype=float)
    xeightlist = np.array(xeightlist, dtype=float)
    yeightlist = np.array(yeightlist, dtype=float)
    plt.xlabel("Sample #")
    plt.ylabel("Average of the 4x4 grid")
    
    plt.xlim([0, 500])
    plt.ylim([0, 300])  
    
    
    plt.scatter(xzerolist, yzerolist, color = "green", marker = "s")
    plt.scatter(xeightlist, yeightlist, color = "red", marker = "^")

    plt.legend(["Digit 0", "Digit 8"], loc = "upper left")

    plt.show()

def acc( th, acclist, y_temp01, size):
  zeroarr = [ ]
  eightarr = [ ]
  sum = 0;
  for i in range(size):
    if(th <= acclist[i] ):
      eightarr.append(i)
    elif(th > acclist[i]):
      zeroarr.append(i)

  for i in zeroarr:
    if(y_temp01[i] == 0):
      sum+=1
  for i in eightarr:
    if(y_temp01[i] == 8):
      sum+=1
    
  return sum/size
    
def main():
  print("The number of images in training set is :", x_train.shape[0])
  print("The number of images in testing set is :", x_test.shape[0])
  print("The images dimensions are", x_train.shape[1], "x", x_train.shape[2])
  print("Selecting 10 images from training set.")
  callctr = 0
  
  digitplot(x_train, y_train, callctr)
  callctr = 1
  x_train_01 =x_train[np.logical_or(y_train==0, y_train == 8), :, :]
  y_train_01 =y_train[np.logical_or(y_train==0, y_train == 8)]

  x_test_01 =x_test[np.logical_or(y_test==0, y_test == 8), :, :]
  y_test_01 =y_test[np.logical_or(y_test==0, y_test == 8)]

  x_valid_01, y_valid_01, x_train_01, y_train_01 = shuffle(x_train_01, y_train_01)

  print("The number of images in training set is :", x_train_01.shape[0])
  print("The number of images in validation set is :", x_valid_01.shape[0])
  print("The number of images in testing set is :", x_test_01.shape[0])
  print("Samples of validation images.")
  digitplot(x_valid_01, y_valid_01, callctr)
  
  x_train_01_center = x_train_01[:, 12:16, 12:16]
  x_valid_01_center = x_valid_01[:, 12:16, 12:16]
  x_test_01_center = x_test_01[:, 12:16, 12:16]

  #avgs
  trainavg = np.sum(x_train_01_center, axis = 2)
  trainavg = np.sum(trainavg, axis = 1)/16

  validavg = np.sum(x_valid_01_center, axis = 2)
  validavg = np.sum(validavg, axis = 1)/16

  testavg = np.sum(x_test_01_center, axis = 2)
  testavg = np.sum(testavg, axis = 1)/16

  xeightlist = [ ]
  xzerolist = [ ]
  yeightlist = [ ]
  yzerolist = [ ]

#valid accuracy lists
  for i in range(500):
    if y_valid_01[i] == 8:
      xeightlist.append(i)
      yeightlist.append(format(validavg[i], ".2f"))
    if y_valid_01[i] == 0:
      xzerolist.append(i)
      yzerolist.append(format(validavg[i], ".2f"))

  #testing accuracy lists
  xtestzero = [ ]
  ytestzero = [ ]
  xtesteight = [ ]
  ytesteight = [ ]
  for i in range(1954):
    if y_test_01[i] == 8:
      xtesteight.append(i)
      ytesteight.append(format(testavg[i], ".2f"))
    if y_test_01[i] == 0:
      xtestzero.append(i)
      ytestzero.append(format(testavg[i], ".2f"))

  #training accuracy lists
  xtrainzero = [ ]
  ytrainzero = [ ]
  xtraineight = [ ]
  ytraineight = [ ]
  for i in range(11274):
    if y_train_01[i] == 8:
      xtraineight.append(i)
      ytraineight.append(format(trainavg[i], ".2f"))
    if y_train_01[i] == 0:
      xtrainzero.append(i)
      ytrainzero.append(format(trainavg[i], ".2f"))

  

  while True:
    th_x = input("Enter a threshold value to test, or enter x to exit:")
    if th_x == "x":
            print("The program will close!")
            return 
    try:
            float(th_x)
        
    except ValueError:
            print("Error, enter a valid number")
            continue
    
    trainacc = acc( float(th_x), trainavg, y_train_01, 11274) * 100
    validacc = acc(float(th_x), validavg, y_valid_01, 500) * 100
    testacc = acc(float(th_x), testavg, y_test_01, 1954) * 100
    
    print("The validation accuracy of the threshold is: ", format(validacc, ".2f"))
    print("The testing accuracy of the threshold is: ", format(testacc, ".2f"))
    print("The training accuracy of the threshold is: ", format(trainacc, ".2f"))
    finplot(xzerolist, yzerolist, xeightlist, yeightlist)

  
main()