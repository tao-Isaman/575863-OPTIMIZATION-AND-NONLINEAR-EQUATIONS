def bisection(max_round, input_function, a, b, error):
    if f(a)*f(b) >= 0:
        print("Bisection method fails.")
        return None
    round = 1
    error_k = abs(a - b)
    ak = a
    bk = b 
    temp_bisec_point = 0

    while (error_k > error and max_round > round) :
        print("round no. " , round)
        bisec_point = (ak + bk) / 2 # bisec inerval
        function_bisec_value = f(bisec_point) 

       
        # relative change less then error
        if (abs(temp_bisec_point - bisec_point) / abs(bisec_point)) <= error and round > 1:
            print("Found exact solution. fuctional value less then error")
            return bisec_point

        # fuctional value less then error
        if abs(function_bisec_value) <= error:
            print("Found exact solution. relative change less then error")
            return bisec_point

        if f(ak) * function_bisec_value < 0:
            bk = bisec_point
            error_k = abs(ak - bk)

        elif f(bk) * function_bisec_value < 0:
            ak = bisec_point
            error_k = abs(ak - bk)

        elif function_bisec_value == 0:
            print("Found exact solution.")
            return bisec_point

        else:
            print("Bisection method fails.")
            return None

        round = round + 1
        temp_bisec_point = bisec_point
        
    return (ak + bk)/2 

f = lambda x: x**3 - 7 * x**2 + x - 1
approx_phi = bisection(25, f , 0 , 100 , 0.01)
print(approx_phi)

