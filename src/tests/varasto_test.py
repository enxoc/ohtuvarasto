import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_ei_luo_negatiivista_tilavuutta(self):
        uusi_varasto = Varasto(-10)

        self.assertAlmostEqual(uusi_varasto.tilavuus, 0.0)

    def test_negatiivinen_alku_saldo_laittaa_saldoksi_0(self):
        uusi_varasto = Varasto(10, -3)

        self.assertAlmostEqual(uusi_varasto.saldo, 0.0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_ei_hyväksy_negatiivista_arvoa(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.lisaa_varastoon(-3)

        self.assertAlmostEqual(self.varasto.saldo, 5)

    def test_lisays_ei_anna_ylittää_tilatuutta(self):
        self.varasto.lisaa_varastoon(15)

        self.assertAlmostEqual(self.varasto.saldo, self.varasto.tilavuus)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        #Rikkinäinen testi
        self.assertAlmostEqual(3, 1)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ottaminen_ei_hyvaksy_negatiivista_arvoa(self):
        self.varasto.lisaa_varastoon(10)
        self.varasto.ota_varastosta(-5)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_ottaa_vain_minka_pystyy_saldosta(self):
        self.varasto.lisaa_varastoon(5)
        otettu = self.varasto.ota_varastosta(10)

        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_saldo_palautus_merkkijonona_on_oikein(self):
        self.varasto.lisaa_varastoon(2.5)

        self.assertEqual(str(self.varasto), "saldo = 2.5, vielä tilaa 7.5")