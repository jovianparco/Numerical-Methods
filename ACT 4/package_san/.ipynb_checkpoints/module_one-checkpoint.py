import numpy as np
import scipy as opt
import matplotlib.pyplot as plt






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
    
##--------------------------------------------------------

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

##----------------------------------------------

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

##--------------------------------------------------------------

def bisection(funct,intval,n_roots,rnd_off = 3,bilim=100,tol=1.0e-06):
    end_bisect = []
    roots = [] 
    if len(intval) != 2 or intval [0] >= intval [1]:
        return "Something Wrong With The Interval"
    for loop in range(intval[1]-intval[0]):
        i1, i2 = intval[0], intval[1]
        y1, y2 = funct(i1), funct(i2)
        if np.sign(y1) == np.sign(y2):
            pass
        else:
            for bisect in range(bilim):
                midp = np.mean([i1,i2])
                ymid = funct(midp)
                y1 = funct(i1)
                if np.allclose(0,y1, atol=tol):
                    roots.append(round(i1,rnd_off)) 
                    end_bisect.append(bisect)
                    break
                elif np.sign(y1) != np.sign(ymid):
                    i2 = midp
                else:
                    i1 = midp

        if len(roots) == n_roots:
            return list(set(roots)), list(set(end_bisect))
        else:
            intval[1], intval[0] = intval[1], intval[0]+1
        
    if len(roots) < bilim-1:
        return list(set(roots)), list(set(end_bisect))
    
###--------------------------------------------------------

def regula_falsi(funct, N_roots, pos = range(0,100), a_range = range(-2,10,1), b_range = range(0,10,1), rnd_off = 3, Print = False):
  roots = []
  posn = []
  unsort_root_pos = []
  fi_root_pos = []
 
  for b in b_range:
    for a in a_range:
      i = b/(3*5 + 1e-10)
      b += i
      y1, y2 = funct(a), funct(b)
      if np.allclose(0,y1): unsort_root_pos.append([a,0])
      elif np.allclose(0,y2): unsort_root_pos.append([b,0])
      elif np.sign(y1) != np.sign(y2):
        for p in pos: 
          c = b - (funct(b)*(b-a))/(funct(b)-funct(a)) ##false root
          if np.allclose(0,funct(c), 1e-06):
            unsort_root_pos.append([round(c,3),p]) 
            break
          if np.sign(funct(a)) != np.sign(funct(c)): b,y2 = c,funct(c)
          else: a,y1 = c,funct(c)
      else:
        pass 

  #delete common roots and their position
  for i in range(len(unsort_root_pos)):
    for l in range(len(unsort_root_pos)):
      if (i == l):
        break
      if (unsort_root_pos[i][0] == unsort_root_pos[l][0]):
          del unsort_root_pos[l]
          unsort_root_pos.insert(0,[0])

  #gets the root and position of the equation
  for x in range(len(unsort_root_pos)):
    if any(unsort_root_pos[x]) == True:
      fi_root_pos.append(unsort_root_pos[x])

  #separate the roots and position and add them in their respective list
  if N_roots <= len(fi_root_pos):
      for elem in range(N_roots):  
        roots.append(fi_root_pos[elem][0])
        posn.append(fi_root_pos[elem][1])
  else:
      for elem in range(len(fi_root_pos)):  
        roots.append(fi_root_pos[elem][0])
        posn.append(fi_root_pos[elem][1])

  # Catch statement when there is no roots found
  if len(roots) < N_roots:
    print(f"Warning! The roots found does not meet the number of expected roots please readjust arguments, Expected Number of Roots:{N_roots}, a_range:{a_range}, b_range:{b_range}, or pos:{pos} or check the input function.")
    print("Note: Make sure that the equation used passes through the negative and positive x-axis or no roots would be found.")

  # Prints the root/s and its position where it was found
  if Print == True:
    print(f'  Roots   |   Position ')
    for num in range(len(roots)):
      print(f'  {roots[num]}   |     {posn[num]}')
    
##----------------------------------------------------------

def secant(funct,intval,n_roots,rnd_off = 3,bilim=100,tol=1.0e-06):
    end_secant = []
    roots = [] 
    if len(intval) != 2 or intval [0] >= intval [1]:
        return "Something Wrong With The Input Interval"
    for loop in range(intval[1]-intval[0]):
        i1, i2 = intval[0], intval[1]
        y1, y2 = funct(i1), funct(i2)
        if np.sign(y1) == np.sign(y2):
            pass
        else:
            for secant in range(bilim):
                midp = (i1*y2 - i2*y1)/(y2 - y1)
                ymid = funct(midp)
                y1 = funct(i1)
                if np.allclose(0,y1, atol=tol):
                    roots.append(round(i1,rnd_off)) 
                    end_secant.append(secant)
                    break
                elif np.sign(y1) != np.sign(ymid):
                    i2 = midp
                else:
                    i1 = midp

        if len(roots) == n_roots:
            return list(set(roots)), list(set(end_secant))
        else:
            intval[1], intval[0] = intval[1], intval[0]+1
        
    if len(roots) < bilim-1:
        return list(set(roots)), list(set(end_secant))



