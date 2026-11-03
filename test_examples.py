#!/usr/bin/env python3
# Developer: Hamdy Abou El Anein
# Contact: hamdy.aea@protonmail.com
"""Offline smoke tests for the three independent Go examples."""
import pathlib
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parent


class GoExamplesTests(unittest.TestCase):
    def test_examples(self):
        expected = {
            "hello-world.go": "hello world\n",
            "Variables.go": "initial\n1 2\ntrue\n0\nshort\n",
            "if-else.go": "7 is odd\n8 is divisible by 4\n9 has 1 digit\n",
        }
        for filename, output in expected.items():
            with self.subTest(filename=filename):
                result = subprocess.run(
                    ["go", "run", filename], cwd=ROOT, capture_output=True,
                    text=True, timeout=30, check=True,
                )
                self.assertEqual(result.stdout, output)


if __name__ == "__main__":
    unittest.main()
