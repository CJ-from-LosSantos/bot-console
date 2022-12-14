import os
from urllib.parse import quote

from requests import request


class Spider:
    token = "EOk6j38PELxUwJy8"

    def __init__(self):
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}

    @staticmethod
    def other(key):
        url = f'https://cn.bing.com/search?q={quote(key, "utf-8")}&FORM=BESBTB'
        return f'ð¢æ²¡æè¯¥æä»¤ï¼å·²èªå¨æ ¹æ®ä½ çæä»¤æç´¢å°å¦ä¸åå®¹ï¼è¯·ç¹å»æ¥ç\n{url}'

    @staticmethod
    def what_to_eat_today(*args):
        """
        ä»å¤©åä»ä¹
        :docs: https://www.apispace.com/eolink/api/eat222/apiDocument
        """
        url = "https://eolink.o.apispace.com/eat222/api/v1/forward/chishenme"
        payload = {"size": "3"}
        headers = {
            "X-APISpace-Token": "zbxmug9fyd25pvq7b37urfl2yqm46f0g",
            "Authorization-Type": "apikey"
        }

        result = request('GET', url, params=payload, headers=headers).json()
        if result['code'] == 200:
            return f'äº²~ï¼ä»æ¥æ¨èçé£è°±ï¼ä¸éä¸å§ð¥:\nã{result["data"]}ã'

        return 'api éè¯¯æèå¤±æäº'

    @staticmethod
    def get_healthy_travel(self, from_, to):
        """
        åºè¡é²ç«æ¿ç­æå
        :docs: https://alapi.cn/api/view/87
        """
        return 'è¯¥æ¥å£å·²åæ¶'
        # table = City()
        # from_id = table.get_city_id(from_)
        # to_id = table.get_city_id(to)
        #
        # url = "https://v2.alapi.cn/api/springTravel/query"
        # payload = {
        #     'token': self.token,
        #     'from': from_id,
        #     'to': to_id
        # }
        #
        # result = request('POST', url, params=payload, headers=self.headers).json()
        # if result['code'] == 200:
        #     out_desc = result['config']['from_info']['out_desc']
        #     out_code_name = result['config']['from_info']['health_code_name']
        #     in_desc = result['config']['to_info']['low_in_desc']
        #     in_code_name = result['config']['to_info']['health_code_name']
        #
        #     return f"ð {from_}åºç«ï¼\nð å¥åº·ç ï¼{out_code_name}\nð {out_desc}\nð {to}è¿ç«ï¼\nð å¥åº·ç ï¼{in_code_name}\nð {in_desc}\n"

    @staticmethod
    def oneiromancy(self, key):
        """
        å¨å¬è§£æ¢¦
        :docs: https://www.apispace.com/eolink/api/zgjm/guidence/
        """
        url = "https://eolink.o.apispace.com/zgjm/common/dream/searchDreamDetail"
        payload = {"keyword": key}
        headers = {
            "X-APISpace-Token": "zbxmug9fyd25pvq7b37urfl2yqm46f0g",
            "Authorization-Type": "apikey",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        result = request('POST', url, data=payload, headers=headers).json()
        if result['statusCode'] == '000000':
            contents = result["result"]
            return ''.join(f'å³é®å­ï¼{key}\nåå®¹ï¼{c["content"]}' for c in contents)

        return 'api éè¯¯æèå¤±æäº'

    def help_(self, *args):
        return f'ð© å½ä»¤æ ¼å¼ï¼/å½ä»¤åç§°\nð© æ³¨æï¼å½ä»¤å¸¦æä¸åçº¿è¯·å¿½ç¥å¡«å\nð© å½ä»¤åè¡¨ï¼{list(self.By.keys())}'

    def query_virus_cities(self, province, city=None, county=None):
        """
        ç«æé£é©å°åºæ¥è¯¢
        :docs: https://alapi.cn/api/view/106
        """
        url = "https://v2.alapi.cn/api/springTravel/risk"
        payload = {
            'token': self.token,
            'province': province,
            'city': city,
            "country": county
        }

        result = request('POST', url, params=payload, headers=self.headers).json()
        if result['code'] == 200:

            if 10 > len(result['data']['high_list']) > 0:
                high_list = result['data']['high_list']
                msg = ''.join(f"{row['area_name']} - â é«é£é©ç¤¾åºï¼{len(row['communitys'])}ä¸ª\n" for row in high_list)
            elif city is None:
                msg = f"{province} â å­å¨é«é£é©å°åºï¼{result['data']['high_count']}ä¸ª\n"
            else:
                msg = f"{city} â å­å¨é«é£é©å°åºï¼{result['data']['high_count']}ä¸ª\n"
            msg = f"{msg}â  å­å¨ä¸­é£é©å°åºï¼{result['data']['middle_count']}ä¸ª\nææ°åå¸æ¶é´ï¼{result['data']['end_update_time']}"

            return msg

        return 'api éè¯¯æèå¤±æäº'

    def get_weather(self, city=None):
        """
        å½åå¤©æ°æ¥è¯¢
        :docs: https://alapi.cn/api/view/65
        """
        url = 'https://v2.alapi.cn/api/tianqi'
        payload = {
            'token': self.token,
            'city': city
        }

        result = request('POST', url, params=payload, headers=self.headers).json()
        if result['code'] == 200:
            hour_list = result['data']['hour']
            msg = ''.join(f"â° {row['time'].split()[-1]} - {row['wea']} - {row['temp']}Â°\n" for row in hour_list)
            msg = f'ä»æ¥æ©æ¨-ææ¥æ©æ¨\n{msg}'

            return msg

        return 'api éè¯¯æèå¤±æäº'

    def query_logistics(self, number):
        """
        å¿«éæ¥è¯¢
        :docs: https://alapi.cn/api/view/63
        """
        url = 'https://v2.alapi.cn/api/kd'
        payload = {
            'token': self.token,
            'number': number,
            'order': 'asc'
        }

        result = request('POST', url, params=payload, headers=self.headers).json()
        if result['code'] == 200:
            new_state = result['data']['info'][-1]
            return f"â° ææ°æ´æ°æ¶é´ï¼{new_state['time']}\nð¦ {new_state['content']}"

        return 'api éè¯¯æèå¤±æäº'

    def get_news_to_day(self):
        """
        æ¯æ¥60ç§æ©æ¥
        :docs: https://alapi.cn/api/view/93
        """
        url = 'https://v2.alapi.cn/api/zaobao'
        payload = {
            'token': self.token,
            'format': 'json'
        }

        result = request('POST', url, params=payload, headers=self.headers).json()
        if result['code'] == 200:
            image_url = result['data']['image']
            c = request('GET', image_url).content
            file = f'{os.path.join(os.getcwd(), "images")}\zaobao.png'

            with open(file, 'wb') as f:
                f.write(c)

            return file

        return 'api éè¯¯æèå¤±æäº'


class BySpiderCommand(Spider):
    By = None

    def __init__(self):
        super().__init__()
        self.By = {
            'help': self.help_,
            'other': self.other,
            'ç«ææ¥è¯¢': self.query_virus_cities,
            'åºè¡é²ç«': self.get_healthy_travel,
            'å¤©æ°': self.get_weather,
            'å¿«é': self.query_logistics,
            'æ©æ¥': self.get_news_to_day,
            'åä¸è¥¿': self.what_to_eat_today,
            'è§£æ¢¦': self.oneiromancy,
        }
