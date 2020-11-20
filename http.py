
# urllib
# requests 需要安装 pipenv install requests
import requests
class HTTP:
    def get(self, url, return_json = True):
        r = requests.get(url)
        # 接口返回的格式 JSON 或 text

        # 简化版本
        if r.status_code != 200:
            return {} if return_json else ''
        return r.json() if return_json else r.text

        # v1 版本
        # if r.status_code == 200:
        #     if return_json:
        #         return r.json()
        #     else:
        #         return r.text
        # else:
        #     if return_json:
        #         return {}
        #     else:
        #         return ''