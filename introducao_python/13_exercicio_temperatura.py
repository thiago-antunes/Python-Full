# Receba uma temperatura em Farenheit e exiba em graus Celsius
# (°F - 32) / 1.8000

temperatura_f = float(input('Informe a temperatura em Farenheit: '))
temperatura_c = (temperatura_f - 32) / 1.8000
print(f'{temperatura_f} °F equivale a {temperatura_c} °C')
