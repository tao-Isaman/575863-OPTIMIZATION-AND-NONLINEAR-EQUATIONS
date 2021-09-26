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


x = [4,2]
xn = [-4,-2]
steps = [(4.0, 2.0)]
i = 0
imax = 10

#golden_section
golden_section = ((5**(1/2)) + 1) / 2
a , b = metrix(x) , metrix(xn)
c = b - (b - a) / golden_section
d = a + (b - a) / golden_section
alpha  = 1.2
while i < imax :
    # golden section method
    # print(a,b,c,d)
    # print(deMetrix(a),deMetrix(b),deMetrix(c),deMetrix(d))

    if objective_function(deMetrix(c)) < objective_function(deMetrix(d)):
      b = d
    else:
      a = c

    c = b - (b - a) / golden_section
    d = a + (b - a) / golden_section

    # steps.append((b + a) / 2)
    result = deMetrix(alpha * (b + a) / 2)
    print(result)
    steps.append((result[0], result[1]))
    i += 1
    contoursteps(x1, x2, zs, steps, i)