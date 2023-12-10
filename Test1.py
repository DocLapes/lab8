import unittest


from lab1 import Tests

class TestPolindromTrue(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_polindrom(self):
        self.assertEqual(self.tests.Polindrom('dovod'), True)
class TestPolindromFalse(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_polindrom(self):
        self.assertEqual(self.tests.Polindrom('povod'), False)

class TestProstoeTrue(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()
    def test_prostoe(self):
        self.assertEqual(self.tests.prostoe(5), True)

class TestProstoeFalse(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()
    def test_prostoe(self):
        self.assertEqual(self.tests.prostoe(6), False)

class TestSortirovka1(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()
    def test_sortirovka1(self):
        array1=[1, 3, 2, 4]
        self.assertEqual(self.tests.Sortirovka(array1), [1, 2, 3, 4])

class TestSortirovka2(unittest.TestCase):
    def setUp(self):
        self.tests = Tests()

    def test_sortirovka(self):
        array1=[0, 6, -1, 3, 2, 4]
        self.assertEqual(self.tests.Sortirovka(array1), [-1, 0, 2, 3, 4, 6])

class TestFactorial1(unittest.TestCase):
    def test_factorial(self):
        from lab1 import factorial
        self.assertEqual(factorial(3), 6)

class TestFactorial2(unittest.TestCase):
    def test_factorial(self):
        from lab1 import factorial
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(factorial(-1),1)


class Testfibonacci1(unittest.TestCase):
    def test_fibonacci(self):
        from lab1 import fibonacci
        self.assertEqual(fibonacci(5), 3)

class Testfibonacci2(unittest.TestCase):
    def test_fibonacci(self):
        from lab1 import fibonacci
        with self.assertRaises(Exception) as assert_error:
            self.assertEqual(fibonacci(-5),1)

class Teststepen1(unittest.TestCase):
    def test_stepen(self):
        from lab1 import stepen
        self.assertEqual(stepen(0,5), 0)

class Teststepen2(unittest.TestCase):
    def test_stepen(self):
        from lab1 import stepen
        a = 4.5;
        b =1.5
        self.assertEqual(stepen(a , b), 9.54594154601839)
if __name__ == "__main__":
    unittest.main()
