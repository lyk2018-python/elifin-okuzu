from bs4 import BeautifulSoup
import requests
from dictionary.models import Node,Edge
from django.core.management import BaseCommand

class Command(BaseCommand):

    def __init__(self):
        self.main_url = "https://www.etimolojiturkce.com/kelime/{}"
        self.word = ""

    def add_arguments(self, parser):
        parser.add_argument('word', type=str)

    def origin_crawler(self,word):
        webpage = requests.get(self.main_url.format(word).lower())
        content = webpage.content
        if webpage.status_code == 404:
            return None
        soup = BeautifulSoup(content,"lxml")
        soup3 = soup.find('h2',{"id" : "koken"})
        a = str(soup3.find_next_sibling('p'))
        first = a.find("<b>")+3
        end = a.find("</b>")
        origin = a[first:end]
        self.origin_word(a)
        return origin,self.word

    def origin_word(self,html):

         end = str(html).find("</i>")+3
         html = html[end:]
         first = str(html).find("<i>")+3
         end = str(html).find("</i>")
         self.word = str(html)[first:end]
         print(self.word)

    def new_node(self,node_name="null",node_lang="null"):
        n = Node()
        n.name = node_name
        n.language = node_lang
        n.save()

    def new_edge(self,destination,source):
        e = Edge()
        e.source = Node.objects.get(name=source)
        e.destination = Node.objects.get(name=destination)
        e.type_of_edge = "derives_from"
        e.is_directed = True
        e.save()

    def handle(self, *args, **options):
        word = options['word']
        try:
            destination,origin = self.origin_crawler(word)
        except TypeError:
            print("404 Not Found.")
            return None
        if origin.startswith("+"):       # when the word dont have a origin.
            print("Skipped",word)
            return None
        self.new_node(word,"tr")
        self.new_node(origin,destination)
        self.new_edge(origin,word)
        print("Added",word)