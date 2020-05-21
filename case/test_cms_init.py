import sys
import unittest

sys.path.append('../')

from Cms_base import CMS


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cms = CMS()

    def test_01(self):
        ti = self.cms.driver.title
        title = 'CRM'
        self.assertEqual(title, ti)

    def test_02(self):
        url = 'http://ztwxwh.eatuo.com:8070/login'
        ul = self.cms.driver.current_url
        self.assertEqual(url, ul)

    @classmethod
    def tearDownClass(cls):
        cls.cms.cms_close()


if __name__ == '__main__':
    unittest.main()
