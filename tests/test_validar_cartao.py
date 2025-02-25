import unittest
import sys
import os

# Adicione o caminho do diretório pai para permitir a importação do módulo validar_cartao
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from validar_cartao import validar_cartao

class TestValidarCartao(unittest.TestCase):

    def test_validar_cartao(self):
        testes = {
            "4539 1488 0343 6467": True,
            "1234 5678 9012 3456": False,
            "3714 4963 5398 431": True,  # American Express
            "6011 1111 1111 1117": True,  # Discover
            "5555 5555 5555 4444": True,  # MasterCard
            "4111 1111 1111 1111": True,  # Visa
            "4222 2222 2222 2": False     # Invalid Visa
        }

        for numero, esperado in testes.items():
            resultado = validar_cartao(numero)
            self.assertEqual(resultado, esperado, f"Erro: {numero} esperado {esperado}, mas obteve {resultado}")

if __name__ == '__main__':
    unittest.main()
