from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):

    def test_show_watchlist_resolved(self):         
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist_html"))
        self.assertEquals(response.status_code,200)
    
    def test_show_xml_resolved(self):         
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist_html"))
        self.assertEquals(response.status_code,200)
    
    def test_show_json_resolved(self):         
        client = Client()
        response = client.get(reverse("mywatchlist:show_mywatchlist_html"))
        self.assertEquals(response.status_code,200)