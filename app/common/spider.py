from requests import request

from app.models.city import City


class Spider:
    token = "EOk6j38PELxUwJy8"
    virus_url = "https://v2.alapi.cn/api/springTravel/risk"
    healthy_travel_url = "https://v2.alapi.cn/api/springTravel/query"

    def __init__(self):
        self.headers = {'Content-Type': "application/x-www-form-urlencoded"}
        self.command_list = [
            'help',
            '疫情查询',
            '出行防疫',
        ]

    def help_(self):
        return f'🚩 命令格式：/命令名称\n🚩 注意：命令带有下划线请忽略填写\n🚩 命令列表：{self.command_list}'

    def query_virus_cities(self, province, city=None, county=None):
        """
        疫情风险地区查询
        :docs: https://alapi.cn/api/view/106
        """
        payload = {
            'token': self.token,
            'province': province,
            'city': city,
            "country": county
        }
        result = request('POST', self.virus_url, params=payload, headers=self.headers).json()

        if result['code'] == 200:
            if 10 > len(result['data']['high_list']) > 0:
                high_list = result['data']['high_list']
                msg = ''.join(f"{row['area_name']} - ⛔ 高风险社区：{len(row['communitys'])}个\n" for row in high_list)
            elif city is None:
                msg = f"{province} ⛔ 存在高风险地区：{result['data']['high_count']}个\n"
            else:
                msg = f"{city} ⛔ 存在高风险地区：{result['data']['high_count']}个\n"

            msg = f"{msg}⚠ 存在中风险地区：{result['data']['middle_count']}个\n最新发布时间：{result['data']['end_update_time']}"

            return msg

    def get_healthy_travel(self, from_, to):
        """
        出行防疫政策指南
        :docs: https://alapi.cn/api/view/87
        """
        table = City()
        from_id = table.get_city_id(from_)
        to_id = table.get_city_id(to)

        payload = {
            'token': self.token,
            'from': from_id,
            'to': to_id
        }
        result = request('POST', self.healthy_travel_url, params=payload, headers=self.headers).json()
        if result['code'] == 200:
            out_desc = result['data']['from_info']['out_desc']
            out_code_name = result['data']['from_info']['health_code_name']
            in_desc = result['data']['to_info']['low_in_desc']
            in_code_name = result['data']['to_info']['health_code_name']
            return f"🌏 {from_}出站：\n📕 健康码：{out_code_name}\n🚆 {out_desc}\n🌏 {to}进站：\n📕 健康码：{in_code_name}\n🚆 {in_desc}\n"

