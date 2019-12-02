def voto(x):
    from datetime import date
    ano_atual = date.today().year
    idade = (ano_atual - x)
    if idade < 16:
        return f'Com {idade} anos: VOTO NEGADO!!'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

ano = int(input('Digite o ano de nascimento: '))
print(voto(ano))
