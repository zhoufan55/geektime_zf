# -*- coding: utf-8 -*-
# @Time : 2023/8/1 15:11
# @Author : zhoufan
# @File : retry.py
# @Project : geektime_0-master
import allure


def retry(fun):
    def wrap(*args, **kwargs):
        # 找到当前的状态
        po = args[0]
        fun_info = f"{fun.__name__}({args}, {kwargs})"

        for _ in range(3):  # 最多重试3次
            try:
                r = fun(*args, **kwargs)
                print(f"{r} = {fun_info}")
                allure.attach(
                    name=fun_info,
                    body=po.driver.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG)
                return r
            except:
                # 保存现场
                allure.attach(
                    name=fun_info,
                    body=po.driver.get_screenshot_as_png(),
                    attachment_type=allure.attachment_type.PNG)

                # 异常处理
                po.exception_handle()

        # 若重试失败，则抛出异常
        raise Exception(f"Failed to execute {fun.__name__} after 3 retries.")

    return wrap
