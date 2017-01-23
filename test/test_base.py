import unittest

class BaseTestCase(unittest.TestCase):
    def setUp(self):
        print 'setUp'

    def tearDown(self):
        print 'tearDown'

    def test_default_size(self):
        self.assertEqual(1, 1)
