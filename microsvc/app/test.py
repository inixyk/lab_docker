import unittest
import aplikasi
class TestCase(unittest.TestCase):
    def setUp(self):
        aplikasi.app.config["TESTING"] = True
        self.app = aplikasi.app.test_client()
    def test_get_mainpage(self):
        page = self.app.post("/", data=dict(name="Joni"))
        assert page.status_code == 200
        assert 'Hallo' in str(page.data)
        assert 'Joni' in str(page.data)
    def test_html_escaping(self):
        page = self.app.post("/", data=dict(name='"><b>TEST</b><!--'))
        assert '<b>' not in str(page.data)
if __name__ == '__main__':
    unittest.main()