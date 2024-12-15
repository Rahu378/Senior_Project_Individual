from django.shortcuts import render

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_range(request):
    primes = []
    start = end = None

    if request.method == 'POST':
        start = request.POST.get('start')
        end = request.POST.get('end')

        if start.isdigit() and end.isdigit():
            start, end = int(start), int(end)
            primes = [n for n in range(start, end + 1) if is_prime(n)]

    return render(request, 'prime/prime_range.html', {
        'primes': primes,
        'start': start,
        'end': end
    })
