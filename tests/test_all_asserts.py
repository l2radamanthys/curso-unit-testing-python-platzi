import unittest
import sys

SERVER = "Local"

class AllAssertsTest(unittest.TestCase):
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("hola", "hola")
        self.assertNotEqual(10, 5)

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_exception(self):
        with self.assertRaises(Exception):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [20, 5, 10, 6])
        self.assertNotIn(7, [20, 5, 10, 6])

    def test_assert_dict_equal(self):
        user = {"first_name": "luis", "last_name": "martinez"}
        self.assertDictEqual(user, {"first_name": "luis", "last_name": "martinez"})

    def test_assert_set(self):
        self.assertSetEqual({1, 3, 4}, {1, 4, 3})

    def test_assert_list(self):
        self.assertListEqual([1, 2, 3, 4], [1, 2, 3, 4])

    @unittest.skip("Trabajo en progreso queda pendiente")
    def test_skip(self):
        self.assertEqual("Hola", "Mundo")

    @unittest.skipIf(SERVER != "PRODUCTION", "Saltada porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)

    @unittest.skipUnless(sys.platform.startswith("linux"), "Solo corre en Linux")
    def test_solo_linux(self):
        self.assertTrue(True)
