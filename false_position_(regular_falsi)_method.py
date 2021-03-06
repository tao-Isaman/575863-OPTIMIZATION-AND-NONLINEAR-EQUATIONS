# -*- coding: utf-8 -*-
"""False Position (Regular Falsi) Method

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1N9NrjuABR9m_mQuAwOnKfM97q0joI_K6
"""

def false_position(input_fuction, cx, px):
  '''
  x is a current value of fucntion

  return next x
  '''
  return cx - (input_fuction(cx) * ((cx - px) / ((input_fuction(cx) - input_fuction(px)))))

def find_root(max_round, input_fuction, a, b, error):
    
    round = 1

    # inital estimates 
    previous_estimation  = a
    current_estimation  = b

    while (max_round > round) :
      print("round no. " , round)
      next_estimation = false_position(input_fuction, current_estimation, previous_estimation)

      current_estimation_value = input_fuction(current_estimation)
      next_estimation_value = input_fuction(next_estimation)
      print('current f(x) = ', next_estimation)

      # small value
      if abs(next_estimation_value) < error :
        print("Found exact solution. value less then error")
        return next_estimation

      # relative change less then error
      if (abs(next_estimation_value - current_estimation_value) <= error and round > 1):
          print("Found exact solution. fuctional value less then error")
          return next_estimation

      if next_estimation_value == 0 :
        print("Found exact solution. a point is root")
        return next_estimation
      elif current_estimation_value * next_estimation_value < 0 :
        current_estimation = next_estimation
      else:
        previous_estimation = next_estimation
        
      round = round + 1



    return next_estimation

from numpy import arange , cos , exp , pi , sqrt , e , meshgrid , sin , absolute

objective_function = lambda x: x**3 - 5*x**2 - x + 1
approx_phi = find_root(1000, objective_function, -10, 10, 0.01)
print(approx_phi)
objective_function(approx_phi)