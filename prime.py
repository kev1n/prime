def prime(number):
    prime_number_list = []
    for num in range(100 ** 100):
        if_prime = []
        for i in range(1, num):
            divided = num / i
            checked = divided.is_integer()
            if checked:
                if_prime.append(i)
        if len(if_prime) == 1:
            prime_number_list.append(num)
        if len(prime_number_list) == number:
            return prime_number_list

print(prime(1000))