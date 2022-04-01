import requests


class NamozVaqti():

    def __init__(self, city):
        self.city = city
        self.url = 'http://api.aladhan.com/v1/timingsByCity?city=' + \
            self.city + '&country=Uzbekistan&method=2'
        self.response = requests.get(self.url)
        self.data = self.response.json()

    def get_namoz_vaqt(self):
        return self.data['data']['timings']

    def bomdod(self):
        return self.get_namoz_vaqt()['Fajr']

    def quyosh_chiqishi(self):
        return self.get_namoz_vaqt()['Sunrise']

    def peshin(self):
        return self.get_namoz_vaqt()['Dhuhr']

    def asr(self):
        return self.get_namoz_vaqt()['Asr']

    def quyosh_botishi(self):
        return self.get_namoz_vaqt()['Sunset']

    def shom(self):
        return self.get_namoz_vaqt()['Maghrib']

    def xufton(self):
        return self.get_namoz_vaqt()['Isha']
