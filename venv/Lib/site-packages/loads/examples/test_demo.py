from loads.case import TestCase


class TestWebSite(TestCase):

    def test_mozilla_org(self):
        res = self.session.get('http://mozilla.org/en-US/')
        self.assertTrue('Work with us' in res.content)
