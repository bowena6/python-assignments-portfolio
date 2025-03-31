def approximate_arctan(x):
     #checking if x makes sense and is in range
    if x<0 or x>1:
        return "Error!"
    approximation = 0
    n = 0
    estimation_error = float('inf')
    #looping to imporve approximation
    while estimation_error>0.0001:
        term = ((-1)**n) * (x**(2*n+1))/(2*n+1)
        approximation += term
        #calculate estimation error
        estimation_error = x**(2*(n+1))/(2*(n+1))
        #increment n for next term
        n += 1
    return approximation, n, estimation_error
     #testing
test_values = [-1, 0, 0.25, 0.5, 0.75, 1]
results = {x: approximate_arctan(x) for x in test_values}
for x, result in results.items():
    print(f"arctan({x}) = {result}")