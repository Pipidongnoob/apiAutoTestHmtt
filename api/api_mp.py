import api
import requests
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiMp(object):
    def __init__(self):
        # 1. 登录接口url:
        self.mp_login_url = api.host + "/mp/v1_0/authorizations"
        log.info("正在初始化自媒体登录url: {}".format(self.mp_login_url))
        # 2. 发布文章接口url
        self.mp_article_url = api.host + "/mp/v1_0/articles"
        log.info("正在初始化自媒体发布文章url".format(self.mp_article_url))

    # 2. 登录接口
    def api_mp_login(self, mobile, code):
        """

        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 1. 定义请求数据
        data = {"mobile": mobile, "code": code}
        log.info("正在调用自媒体登录接口，请求数据：{}".format(data))
        # 2. 调用post方法
        return requests.post(self.mp_login_url, json=data, headers=api.headers)

    # 3. 发布文章接
    def api_mp_article(self, title, content, channel_id):
        """

        :param title: 文章标题
        :param content: 文章内容
        :param channel_id: 频道id
        :return: 响应对象
        """
        # 1. 定义请求数据
        data = {"title": title, "content": content, "channel_id": channel_id, "cover": {"type": 0, "images": []}}
        log.info("正在调用自媒体发布文章接口，请求数据：{}".format(data))
        # 2. 调用post方法
        return requests.post(self.mp_article_url, json=data, headers=api.headers)
