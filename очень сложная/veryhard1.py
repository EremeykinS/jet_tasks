from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, quote_plus
from urllib import request
import xml.etree.ElementTree as ET
import json
class searchHandler(BaseHTTPRequestHandler):
    api_url = "http://blogs.yandex.ru/search.rss?text="
    def echo(self, text):
        self.wfile.write(bytes(text,"utf-8"))
    def do_GET(self):
        links = set()
        self.send_response(200, 'OK')
        self.send_header("Content-type", "application/json")
        self.end_headers()
        p = urlparse(self.path)
        q = parse_qs(p.query)
        if (p.path == '/search') and ('query' in q):
            ql = q['query']
            for kw in ql:
                url = self.api_url + quote_plus(kw)
                response = request.urlopen(url).read()
                tree = ET.fromstring(response)
                for item in tree.iter('item'):
                    for link in item.iter('link'):
                        links.add(link.text)
        domain_list = ['.'.join(urlparse(link).netloc.split('.')[-2:]) for link in links]
        domains = dict((el, domain_list.count(el)) for el in set(domain_list))
        result = json.dumps(domains, ensure_ascii=False, sort_keys=True, indent=4)
        self.echo(str(result))
                
hostname, port = "localhost", 8080
searchServer = HTTPServer((hostname, port),searchHandler)
print("Сервер запущен и готов отвечать на запросы.\nДля заврешения работы нажмите Ctrl+C.")
try:
    searchServer.serve_forever()
except KeyboardInterrupt:
    print("\nСервер остановлен и больше не будет отвечать на запросы.")