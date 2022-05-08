def derivative_value(n, x, function, h=0.00000001):
    if n <= 0:
        return None
    elif n == 1:
        return (function(x + h) - function(x)) / h
    return (derivative_value(n - 1, x + h, function) - derivative_value(n - 1, x, function)) / h


def max_derivative_value(x, function, h=0.00000001):
    return max((function(x + h) - function(x)) / h)


def chord_method(a, b, func, error, max_iter=100):
    trace = [['a', 'b', 'x', 'f(a)', 'f(b)', 'f(x)', '|x - x0|']]

    x = a - (b - a) / (func(b) - func(a)) * func(a)
    trace.append([a, b, x, func(a), func(b), func(x), abs(a - b)])

    iter = 0
    while abs(a - b) > error and iter < max_iter:
        if func(a) * func(x) < 0:
            b = x
        else:
            a = x
        x = a - (b - a) / (func(b) - func(a)) * func(a)
        trace.append([a, b, x, func(a), func(b), func(x), abs(a - b)])
        print(trace)
        iter += 1
    print(trace)
    return x, func(x), iter, trace


def simple_iteration_method(a, b, func, error, max_iter=100):
    trace = [['x', 'f(x)', 'x0', 'g(x)', '|x - x0|']]

    if func(a) * derivative_value(2, a, func) > 0:
        x0 = a
    else:
        x0 = b

    def g(g_x):
        return g_x + (-1 / derivative_value(1, g_x, func)) * func(g_x)

    la = max(derivative_value(1, a, func), derivative_value(1, b, func))
    fi_a = 1 + (-1 / la) * derivative_value(1, a, func)

    fi_b = 1 + (-1 / la) * derivative_value(1, b, func)
    print(-1 / derivative_value(1, a, func))
    print(-1 / derivative_value(1, b, func))
    print(fi_a)
    print(fi_b)
    x = g(x0)
    trace.append([x0, func(x0), x, g(x0), abs(x - x0)])

    # if derivative_value(1, a, func) < 1:
    #     print(derivative_value(1, a, func))
    # if derivative_value(1, b, func) < 1:
    #     print(derivative_value(1, b, func))

    itr = 0
    while abs(x - x0) > error and itr < max_iter:
        # if derivative_value(1, x, g) >= 1:
        #     return None
        x0 = x
        x = g(x0)
        trace.append([round(x, 3), func(round(x, 3)), round(x0, 3), g(x.real), abs(x.real - x0.real)])
        print(trace)
        itr += 1

    return x.real, func(round(x, 3)), itr, trace


def newtons_method(a, b, func, error):
    trace = [['x0', 'f(x)', 'f`(x)', 'x', '|x0-x|']]
    print(derivative_value(2, a, func))
    if func(a) * derivative_value(2, a, func) < 0:
        x0 = a
    elif func(b) * derivative_value(2, a, func) < 0:
        x0 = b
    else:
        return None
    try:
        iter = 0
        while True:
            x1 = x0 - (func(x0) / derivative_value(1, x0, func))
            if abs(x1 - x0) < error:
                break
            iter += 1
            x0 = x1
            trace.append([x0, func(x0), derivative_value(1, x0, func), x1, abs(x1 - x0)])
            print(trace)
        return x1, func(x1), iter, trace
    except ValueError:
        print("Value not invalidate")
