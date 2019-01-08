import logging; logging.basicConfig(level = logging.INFO)
import asyncio,os,json,time
from datetime import datetime
from aiohttp import web

#定义服务器响应请求的返回为“awesome website”
def index(request):
	return web.Response(body = b'<h1>awesome website<h1/>',headers = {'content-type':'text/html'})

#建立服务器应用，持续监听本地9000端口的http响应，并异步对首页”/“进行响应

async def init(loop):
	app = web.Application(loop = loop)
	app.router.add_route('GET','/',index)
	srv = await loop.create_server(app.make_handler(),'127.0.0.1',9000)


	logging.info('server started at http://127.0.0.1:9000...')

	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()






