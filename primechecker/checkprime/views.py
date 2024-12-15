from django.shortcuts import render

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def prime_checker(request):
    result = None
    number = None

    if request.method == 'POST':
        number = request.POST.get('number')
        if number and number.isdigit():
            number = int(number)
            result = is_prime(number)
        else:
            result = "Invalid input"

    return render(request, 'checkprime/prime_checker.html', {
        'number': number,
        'result': result
    })
