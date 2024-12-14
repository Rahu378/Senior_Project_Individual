from django.shortcuts import render

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime_number_view(request):
    result = None
    if request.method == "POST":
        number = int(request.POST.get('number', 0))
        result = is_prime(number)
    return render(request, 'primeapp/prime_number.html', {'result': result})
