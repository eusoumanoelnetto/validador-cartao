# Validador de Cartões

Este repositório contém uma função em Python para validar números de cartões de crédito usando o algoritmo de Luhn.

## Funcionalidades

- Validação de números de cartões de crédito
- Suporte para diversos formatos de entrada (com espaços e hifens)
- Implementação do algoritmo de Luhn

## Como usar

1. Clone este repositório.
    ```sh
    git clone https://github.com/eusoumanoelnetto/validador-cartao.git
    cd validador-cartao
    ```

2. Importe a função `validar_cartao` em seu projeto.
    ```python
    from validar_cartao import validar_cartao
    ```

3. Passe o número do cartão como string para a função e obtenha um valor booleano indicando a validade.
    ```python
    numero_cartao = "4539 1488 0343 6467"
    print(validar_cartao(numero_cartao))  # Output: True ou False dependendo do número
    ```

## Estrutura do Projeto

```
validador-cartao/
├── LICENSE
├── README.md
├── validar_cartao.py
└── tests/
    ├── __init__.py
    └── test_validar_cartao.py
```

## Testes

Para rodar os testes, execute o seguinte comando na raiz do repositório:

```sh
python -m unittest discover -s tests
```

## Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.