import unittest
import os

class TestFractalStrategy(unittest.TestCase):
    def test_pine_script_file_exists(self):
        self.assertTrue(os.path.exists("Fractal_Model_Strategy_v6.pine"), "Fractal_Model_Strategy_v6.pine must exist")

    def test_pine_script_contents(self):
        with open("Fractal_Model_Strategy_v6.pine", "r", encoding="utf-8") as f:
            content = f.read()
            self.assertIn('//@version=6', content)
            self.assertIn('strategy(', content)
            self.assertIn('strategy.entry', content)
            self.assertIn('strategy.exit', content)
            self.assertIn('commission_value=0.04', content)
            self.assertIn('slippage=1', content)

if __name__ == '__main__':
    unittest.main()
