"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", side_effect=["2010", "15", "2023", "Fulano"])
    def test_idade_2010_15_2023_fulano(self, _mock_input):
        """
        Testa se o programa imprime "Fulano, no ano de 2023 você terá 28 anos"
        quando o usuário digita 2010, 15, 2023, Fulano
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Fulano, no ano de 2023 você terá 28 anos",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", side_effect=["0", "0", "0", "Beltrano"])
    def test_idade_0_0_0_beltrano(self, _mock_input):
        """
        Testa se o programa imprime "Beltrano, no ano de 0 você terá 0 anos"
        quando o usuário digita 0, 0, 0, Beltrano
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Beltrano, no ano de 0 você terá 0 anos", captured_output.getvalue().strip()
        )

    @patch("builtins.input", side_effect=["2000", "10", "1990", "Ciclano"])
    def test_idade_2000_10_1990_ciclano(self, _mock_input):
        """
        Testa se o programa imprime "Ciclano, no ano de 1990 você terá 0 anos"
        quando o usuário digita 2000, 10, 1990, Ciclano
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Ciclano, no ano de 1990 você terá 0 anos",
            captured_output.getvalue().strip(),
        )

    @patch("builtins.input", side_effect=["2001", "0", "2010", "Alice"])
    def test_idade_2001_0_2010_alice(self, _mock_input):
        """
        Testa se o programa imprime "Alice, no ano de 2010 você terá 9 anos"
        quando o usuário digita 2001, 0, 2010, Alice
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn(
            "Alice, no ano de 2010 você terá 9 anos", captured_output.getvalue().strip()
        )
