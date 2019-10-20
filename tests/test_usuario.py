from src.leilao.domain import User, Leilao
from src.leilao.excecoes import LanceInvalido
import pytest


@pytest.fixture()
def xico():
    return User('xico', 100.0)


@pytest.fixture()
def leilao():
    return Leilao('Celular')


def test_deve_subtratir_valor_da_carteira_do_usuario_quando_este_propor_um_lance(xico, leilao):
    xico.propoe_lance(leilao, 50.0)
    assert xico.carteira == 50.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(xico, leilao):
    xico.propoe_lance(leilao, 1.0)
    assert xico.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(xico, leilao):
    xico.propoe_lance(leilao, 100)
    assert xico.carteira == 0


def test_nao_deve_permitir_propor_lance_maior_que_o_valor_da_carteira(xico, leilao):
    with pytest.raises(LanceInvalido):
        xico.propoe_lance(leilao, 200)
        assert xico.carteira == 100


