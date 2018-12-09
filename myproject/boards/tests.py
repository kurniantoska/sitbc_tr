from django.urls import reverse, resolve
from django.test import TestCase
from . views import home


class HomeBoardTests(TestCase):
    def test_board_home_view_status_code(self):
        url = reverse('boards_home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_board_home_url_resolver_home_view(self):
        view = resolve('/boards/')
        self.assertEquals(view.func, home)
