from django.shortcuts import render
from sympy import symbols, inverse_laplace_transform, Function, exp, Heaviside
from sympy.abc import s, t
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sympy import symbols, inverse_laplace_transform, sympify, Symbol, exp, laplace_transform, collect, diff, integrate
from sympy.abc import s, t
from sympy import latex



# Create your views here.
def index(request):
    return render(request, 'index.html')
def demo(request):
    return render(request, 'demo.html')

@csrf_exempt
def solve_laplace_v1(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            a = Symbol('a', positive=True)
            F_s = sympify(data.get('function', ''))
            result = inverse_laplace_transform(F_s, s, t,)
            return JsonResponse({'result': str(result)})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def solve_laplace(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        function = data.get('function', '')

        try:
            # F_s = sympify(function)
            # f_t = inverse_laplace_transform(F_s, s, t)
            # result = latex(f_t)  # Convert to LaTeX format
            s, t = symbols('s t', positive=True)

            f_t = exp(-2*t)
            a = 3
            time_shifted_f_t = Heaviside(t - a) * f_t.subs(t, t - a)
            result = latex(time_shifted_f_t)  # Convert to LaTeX format

            return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)


@csrf_exempt
def original_function(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        F_t = data.get('function', '')
        print("data: ",data)
       
        try:
            F_t = sympify(F_t)
            print("F_t: ",F_t)
            f_s = laplace_transform(F_t, t, s, noconds=True)
            print("fs: ",f_s)

            laplace_result = latex(f_s)  # Convert to LaTeX format
            print("laplace_result: ",laplace_result)


            # Compute the inverse Laplace Transform
            inverse_f_s = inverse_laplace_transform(f_s, s, t)
            print("inverse_f_s: ",inverse_f_s)
            inverse_f_s = collect(inverse_f_s, Heaviside(t))

            inverse_result = latex(inverse_f_s)  # Convert to LaTeX format
            print("inverse_result: ",inverse_result)

            return JsonResponse({'laplace_result': laplace_result, 'inverse_result': inverse_result})

        #     # result = latex(f_t)  # Convert to LaTeX format
        #     t = symbols('t',real = True ,positive=True)
        #     s = symbols('s', real=True)
        #     # f_t = exp(-2*t)
        #     # Compute the Laplace Transform of the original function
        #     f_s = sp.laplace_transform(F_s, t, s, noconds=True)
        #     print(f"The Laplace Transform of {F_s} is: {f_s}")

        #     # Compute the inverse Laplace Transform
        #     inverse_F_t = sp.inverse_laplace_transform(F_s, s, t)
        #     print(f"The inverse Laplace Transform of {F_s} is: {inverse_F_t}")


        #     return JsonResponse({'result': result})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    # return render(request, 'linearity_property.html')

@csrf_exempt
def first_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        F_t = data.get('function', '')
        print("data: ",data)
       
        try:
            F_t = sympify(F_t)
            F_prime_t = diff(F_t, t)
            f_prime_s = laplace_transform(F_prime_t, t, s, noconds=True)
            f_prime_s_inverse = inverse_laplace_transform(f_prime_s, s, t)

            f_prime_s_inverse_result = latex(f_prime_s_inverse)
            f_prime_s_result = latex(f_prime_s)
            F_prime_t_result = latex(F_prime_t)

            return JsonResponse({'f_prime_s_result': f_prime_s_result, 'f_prime_s_inverse_result': f_prime_s_inverse_result, 'F_prime_t_result': F_prime_t_result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)



@csrf_exempt
def second_order(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        F_t = data.get('function', '')
        print("data: ",data)
       
        try:
            F_t = sympify(F_t)
            F_double_prime_t = diff(F_t, t, 2)
            f_double_prime_s = laplace_transform(F_double_prime_t, t, s, noconds=True)
            f_double_prime_s_inverse = inverse_laplace_transform(f_double_prime_s, s, t)

            f_double_prime_s_inverse_result = latex(f_double_prime_s_inverse)
            f_double_prime_s_result = latex(f_double_prime_s)
            F_double_prime_t_result = latex(F_double_prime_t)

            return JsonResponse({'f_prime_s_result': f_double_prime_s_result, 'f_prime_s_inverse_result': f_double_prime_s_inverse_result, 'F_prime_t_result': F_double_prime_t_result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

   
@csrf_exempt
def integration_property(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        F_t = data.get('function', '')
        print("data: ",data)
       
        try:
            F_t = sympify(F_t)
            laplace_transform_function = laplace_transform(F_t, t, s, noconds=True)
            laplace_transform_integral = laplace_transform_function / s
            
            inverse_transform = inverse_laplace_transform(laplace_transform_integral, s, t)

            inverse_result = latex(inverse_transform)
            laplace_result = latex(laplace_transform_integral)
            function_result = latex(laplace_transform_function)

            return JsonResponse({'f_prime_s_result': laplace_result, 'f_prime_s_inverse_result': inverse_result, 'F_prime_t_result': function_result})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
