# /////////
def media_calculation():
    amount = int(input("Digite a quantidade de numeros: "))
    numbers = []
    
    for i in range(amount):
        number = float(input("Digite o numero {}: ".format(i+1)))
        numbers.append(number)
    
    media = sum(numbers) / amount
    return media

result = media_calculation()
print("A media dos numeros e:", result)