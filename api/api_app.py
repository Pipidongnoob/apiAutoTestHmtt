import api
import requests
import time
from tool.get_log import GetLog

log = GetLog.get_logger()


class ApiApp(object):
    # 1. 初始化
    def __init__(self):
        # 1. 登录url
        self.url_login = api.host + "/aap/v1_0/authorizations"
        log.info("正在初始化app用户登录url:{}".format(self.url_login))
        # 2. 查询url
        self.url_article = api.host + "/app/v1_1/articles"
        log.info("正在初始化app用户查询指定频道下所有文章url：{}".format(self.url_article))

    # 2. 登录
    def api_app_login(self, mobile, code):
        """

        :param mobile: 手机号
        :param code: 验证码
        :return: 响应对象
        """
        # 1. 请求参数
        data = {"mobile": mobile, "code": code}
        log.info("正在调用app用户登录接口，请求参数为：{}".format(data))
        # 2. 调用post方法
        return requests.post(url=self.url_login, json=data, headers=api.headers)

    # 3. 查询频道下所有文章
    def api_app_article(self):
        """
        :param channel_id: 频道id 值来源__init__.py模块变量
        :param timestamp: 时间戳 单位毫秒
        :param with_top: 置顶文章 1：包含 0：不包含
        :return: 响应对象
        """
        # 1. 请求参数
        data = {"channel_id": api.channel_id, "timestamp": int(time.time()), "with_top": 1}
        log.info("正在调用app查询频道下所有文章接口，请求阐述为：{}".format(data))
        # 2. 调用get方法
        return requests.get(url=self.url_article, params=data, headers=api.headers)