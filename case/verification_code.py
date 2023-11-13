# -*- coding: utf-8 -*-            
# @Author : ben
# @Time : 2023/11/13 14:09
import re
import subprocess


def get_verification_code(phone_number):
     # 构建adb命令
     adb_command = f'adb shell "content query --uri content://sms/inbox --projection body --where "address=\'{phone_number}\'"'
     # 执行命令，取得输出
     output = subprocess.check_output(adb_command).decode('utf-8')
     # 解析验证码
     match = re.search(r'(\d{4})',output)
     if match:
          return match.group(1)

     return None
a =get_verification_code(1068385300363005)

b = list(a)




