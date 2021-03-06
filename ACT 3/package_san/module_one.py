


import numpy as np
import scipy as opt
import matplotlib.pyplot as plt




# ### Brute Force Algorithm ( F(x)=0 )


def brute_forcefx(funct,start,n_roots,epochs=100,tol=1.0e-06,incre=1):
  roots = []
  for epoch in range(epochs):
    if np.allclose(0,funct(start),atol=tol):
      roots.append(start)
      if len(roots) == n_roots:
        return roots, epoch
        break
    if epoch == epochs-1:
      epoch+1
      return roots, epoch
      break
    start+=incre


# ### Brute Force Algorithm (In terms of X)


def brute_forcef(funcs,n_roots,epochs=100,tol=1.0e-05):
  epoch_list = []
  roots = []
  for func in funcs:
    x = 0
    for epoch in range(epochs):
      x_prime = func(x)
      if np.allclose(x, x_prime,tol):
        roots.append(x_prime)
        epoch_list.append(epoch)
        break
      x = x_prime
    if len(roots) == n_roots:
      return roots, epoch_list
      break
  if len(roots) < n_roots:
    return roots, epoch_list




# ### Newton-Raphson Algorithm



def newton_raphson(funct, N_roots, epochs = 100, start = 0, end = 100, rnd_off = 3, Print = False):

  x_inits = range(start, end, 1) #range of x
  
  roots = []
  epochs_re = []
  root_epoch = []
  root_epoch_fi = []

  # loop for finding the root
  for x_init in x_inits:
    if len(roots) == N_roots:
      break
    x = x_init
    for epoch in range(epochs):
      derivative = ((funct(x + .1e-6)  - funct(x))/(.1e-6)) # Derivative formula

      if derivative == 0: # catch statement if derivative is equal to zero
        print("Derivative is equal to zero cannot proceed with operation")
        break

      x_prime = x - (funct(x)/derivative)
      if np.allclose(x, x_prime):
        root_epoch.append([round(x,rnd_off),epoch])
        break

      x = x_prime

 # selects 1 root of similar roots and its epoch
  for i in range(len(root_epoch)):
    for l in range(len(root_epoch)):
      if (i == l):
        break
      if (root_epoch[i][0] == root_epoch[l][0]):
          del root_epoch[l]
          root_epoch.insert(0,[0])

  #gets the root and epoch of the equation
  for x in range(len(root_epoch)):
    if any(root_epoch[x]) == True:
      root_epoch_fi.append(root_epoch[x])

  #separate the roots and epoch and add them in their respective list
  if N_roots <= len(root_epoch_fi):
      for elem in range(N_roots):  
        roots.append(root_epoch_fi[elem][0])
        epochs_re.append(root_epoch_fi[elem][1])
  else:
      for elem in range(len(root_epoch_fi)):  
        roots.append(root_epoch_fi[elem][0])
        epochs_re.append(root_epoch_fi[elem][1])

 # Catch statement when there is no roots found
  if len(roots) == False:
    print(f"There are no roots found, please readjust arguments, Expected Number of Roots:{N_roots}, start:{start}, end:{end}, or epochs:{epochs} or check the input function.")
    return f'ERROR! Expected is {N_roots}, while returend is {len(roots)}'

  # Prints the root/s and its epoch where it was found
  if Print == True:
    print(f'  Roots   |   Epochs ')
    for num in range(len(roots)):
     print(f'  {roots[num]}   |     {epochs_re[num]}')
  
  else:
    return epochs_re, roots




