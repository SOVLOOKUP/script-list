import json,sys
a =  json.dumps({
	"id": "111111111112",
	"taskname": "测试任务",
	"author": "安伟",
	"version": "V0.0.1",
	"description": "这是招办数据分析示例任务。",
	"template": "https://v.gonorth.top:444/file/111111111112/template.docx",
	"icon": "https://v.gonorth.top:444/file/111111111111/img/2.png",
	"word": [
		{
			"name": "招生数据分析.docx",
			"content": [
				{
					"key": "理工男生",
					"type": "img",
					"value": [
						"https://s1.ax1x.com/2020/10/26/BKUsjP.png"
					]
				},
				{
					"key": "理工女生",
					"type": "img",
					"value": [
						"https://s1.ax1x.com/2020/10/26/BKURAg.png"
					]
				},
				{
					"key": "文科男生",
					"type": "img",
					"value": [
						"https://s1.ax1x.com/2020/10/26/BKUIcq.png"
					]
				},
				{
					"key": "文科女生",
					"type": "img",
					"value": [
						"https://s1.ax1x.com/2020/10/26/BKU7uV.png"
					]
				}
			]
		}
	]
})
def main():
	# 接受工作路径
	wordir = sys.argv[-1]
	print(wordir)
	# 写入结果
	with open(wordir + "/config.json","w+") as f:
		f.write(a)

if __name__ == "__main__":
	main()
