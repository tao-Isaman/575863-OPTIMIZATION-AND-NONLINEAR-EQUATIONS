# Liner search -> not change learnign_rate
import numpy as np
def metrix(listData):
  return np.matrix(listData)

def deMetrix(metrix):
  return metrix.tolist()[0]

def derivative():
    '''
    please see derivative method in other file
    https://colab.research.google.com/drive/1DkZGX4iAmYVOfUVZ2hB-hvXnrnkDzck5?authuser=2#scrollTo=isAlBdazCwo9
    '''
    pass

def objective_function():
    '''
    please see objective_function method in other file
    https://colab.research.google.com/drive/1DkZGX4iAmYVOfUVZ2hB-hvXnrnkDzck5?authuser=2#scrollTo=isAlBdazCwo9
    '''
    pass

def contoursteps():
    '''
    please find contoursteps function in colab
    https://colab.research.google.com/drive/1DkZGX4iAmYVOfUVZ2hB-hvXnrnkDzck5?authuser=2#scrollTo=isAlBdazCwo9
    '''
x1, x2, zs = 'is' , 'a' , 'temp value' # please see in https://colab.research.google.com/drive/1DkZGX4iAmYVOfUVZ2hB-hvXnrnkDzck5?authuser=2#scrollTo=isAlBdazCwo9


x = [6,2]
steps = [(6.0, 2.0)]
i = 0
imax = 10
error = 0.01
learnign_rate = 0.1
learnign_rate0 = learnign_rate
mx = metrix(x)
while i < imax :
    # if (learnign_rate > eps**2 * learnign_rate0):
    #   print("learnign_rate not change ")
    #   break
    if (i != 0):
      mx = metrix(mx) # handle first round
    mx = mx - 1.1 * (learnign_rate * metrix(derivative(objective_function,deMetrix(mx))))
    mx = deMetrix(mx)
    steps.append((mx[0], mx[1]))
    # learnign_rate = derivative(objective_function2,x) - (objective_function2(x) * x)
    i += 1
    contoursteps(x1, x2, zs, steps, i)