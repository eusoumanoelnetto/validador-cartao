def validar_cartao(numero_cartao):
    # Remove espaços e hifens do número do cartão
    numero_cartao = numero_cartao.replace(' ', '').replace('-', '')

    # Verifica se o número do cartão tem apenas dígitos
    if not numero_cartao.isdigit():
        return False

    # Verifica se o número do cartão tem um comprimento válido (geralmente entre 13 e 19 dígitos)
    if not 13 <= len(numero_cartao) <= 19:
        return False

    # Algoritmo de Luhn
    soma = 0
    reverso = numero_cartao[::-1]

    for i, digito in enumerate(reverso):
        n = int(digito)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        soma += n

    return soma % 10 == 0
