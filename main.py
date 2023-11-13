# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


from case.data import App_config
from case.data import get_verification_code

# 要调用一个类里的函数，我们首先需要创建类的实例,实例就像是类的具体化身，它可以执行类里定义的函数。
jk = App_config()

jk.setup()

jk.test_api_demo()


# jk.teardown()