#此为百度Ai开发平台的云打码，识别图片正确率极低，仅为展示调用接口。
from aip import AipOcr

""" 你的 APPID AK SK """
APP_ID = '你的APP_ID'
API_KEY = '你的API_KEY'
SECRET_KEY = '你的SECRET_KEY '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)



""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

image = get_file_content('./images/verifycode2.gif')

""" 调用通用文字识别, 图片参数为本地图片 """
client.basicGeneral(image)

""" 如果有可选参数 """
options = {}
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

""" 带参数调用通用文字识别, 图片参数为本地图片 """
res = client.basicGeneral(image, options)
print(res)