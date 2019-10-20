from unittest import TestCase, main
from src.leilao.domain import User, Lance, Leilao
from src.leilao.excecoes import LanceInvalido


class TestLeilao(TestCase):

    def setUp(self):
        self.mat = User("mat", 300)
        self.yuri = User("yuri", 300)
        self.lance_do_mat = Lance(self.mat, 100.0)
        self.lance_do_yuri = Lance(self.yuri, 120.0)
        self.leilao = Leilao('Celularzinho')

    def test_deve_retornar_o_maior_e_o_menor_valor_de_um_lance_quando_adicionados_em_ordem_crescente_(self):
        self.leilao.propoe(self.lance_do_mat)
        self.leilao.propoe(self.lance_do_yuri)

        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(120.0, self.leilao.maior_lance)

    def test_nao_deve_permitir_propor_um_lance_em_ordem_decrescente(self):
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_yuri)
            self.leilao.propoe(self.lance_do_mat)
            self.assertEqual(100.0, self.leilao.menor_lance)
            self.assertEqual(120.0, self.leilao.maior_lance)


    def test_deve_retorno_o_menor_valor_para_o_maior_e_menor_lance_quando_leilao_tiver_um_lance(self):
        mat = User("mat", 300)
        lance = Lance(mat, 120.0)

        leilao = Leilao('Celularzinho')

        leilao.propoe(lance)


        self.assertEqual(120.0, leilao.menor_lance)
        self.assertEqual(120.0, leilao.maior_lance)

    def test_deve_retornar_o_maior_e_o_menor_valor_quando_tiver_3_lances(self):
        xico = User("xico", 300)


        lance_do_xico = Lance(xico, 122.2)
        self.leilao.propoe(self.lance_do_mat)
        self.leilao.propoe(self.lance_do_yuri)



        self.leilao.propoe(lance_do_xico)


        self.assertEqual(100.0, self.leilao.menor_lance)
        self.assertEqual(122.2, self.leilao.maior_lance)


    def test_deve_permitir_propor_um_lance_caso_o_leilao_nao_tenha_lances(self):
        self.leilao.propoe(self.lance_do_mat)
        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(1, quantidade_de_lances_recebida)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = User("Yuri", 300)
        lance_do_yuri = Lance(yuri , 200.0)
        self.leilao.propoe(self.lance_do_yuri)
        self.leilao.propoe(lance_do_yuri)

        quantidade_de_lances_recebida = len(self.leilao.lances)
        self.assertEqual(2, quantidade_de_lances_recebida)

    def test_nao_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        lance_mat = Lance(self.mat, 200)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_mat)
            self.leilao.propoe(lance_mat)


if __name__ == "__main__":
    main()
