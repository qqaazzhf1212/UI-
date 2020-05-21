import sys
import unittest

sys.path.append('../../')

from Cms_base import CMS


class TextCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cms = CMS()
        cls.cms.login()
        cls.cms.customer_flow()
        cls.cms.customer_opertion_add()

    def test_01(self):
        num = self.cms.customer_num()
        self.assertEqual('6', num)

    @classmethod
    def tearDownClass(cls):
        cls.cms.cms_close()


if __name__ == '__main__':
    unittest.main()
