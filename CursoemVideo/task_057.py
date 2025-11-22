gender = str(input('Enter the gender M/F: ').strip().lower()[0])

while gender not in ('m','f'):
    gender = str(input('Please enter a valid gender: ').strip().lower()[0])

print('Registered with success!')

# aprendi que o while deve estar (m,f) entre parenteses.
# o uso da variavel gender abaixo do while foi necessaria para atualizar a variavel.

# o 0 após o lower permite pegar somente a primeira letra, em caso o usuario digitar
# a palavra inteira masculino ou feminino



















