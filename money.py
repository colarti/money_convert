import requests
from bs4 import BeautifulSoup
from random import choice

class currency_exchange():
    def __init__(self):
        self._get_data()
        self._base_data()
    
    def _get_data(self):
        r = requests.get("https://www.investing.com/currencies/exchange-rates-table")
        soup = BeautifulSoup(r.content, 'html.parser')
        s = soup.find_all('tr')

        self.table = []

        for x,i in enumerate(s):
            if x < 8:
                info = (i.get_text()).strip().replace('\n', '').split()
                self.table.append(info)
        for p in self.table:
            for idx, q in enumerate(p):
                try:
                    p[idx] = float(q)
                except:
                    pass
        self.exchange = {}

        for x in range(1, len(self.table)):
            for y in range(1, len(self.table[0])):
                self.exchange[self.table[0][y], self.table[x][0]] = self.table[x][y]
    
    def _base_data(self):
        self.base_list = set()

        for x in range(1, len(self.table)):
            self.base_list.add(self.table[x][0])
        
        self.base_list = list(self.base_list)
    
    def get_exchange(self, base, exchange):
        return self.exchange[base, exchange]

    def get_base_list(self):
        return sorted(self.base_list)

if __name__ == '__main__':
    c = currency_exchange()
    print(f'exchange: {c.exchange}')
    print(f'base list: {sorted(c.get_base_list())}')

    for x in range(10):
        base = choice(c.base_list)
        convert = choice(c.base_list) 

        print(f'Convert Rate: 1 {base} = {c.get_exchange(base, convert)} {convert}')