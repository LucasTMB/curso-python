# Não é comum usar while com coisas que a gente sabe onde termina

texto = 'Python'

novo_texto = ''
for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)
    
print(novo_texto + '*')