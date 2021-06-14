import asyncio
from aiohttp import web
import aiohttp
import logging
# from aiohttp.web_runner import GracefulExit

app = web.Application()
routes = web.RouteTableDef()
log = logging.getLogger(__name__)

@routes.get("/")
async def hello(request):
    """
    GET /
    greets world
    """
    text = 'hello world'
    return web.Response(text=text)

@routes.get("/hello/{name}")
@routes.get("/hello")
async def hello(request):
    """
    GET /hello
    GET /hello/{<data>}
    gets the name from the url and greets the user
    """
    name = request.match_info.get('name', 'Anonymous')
    text = 'hello, '+name
    return web.Response(text=text)


@routes.get("/fetch")
async def fetch_data(request):
    """
    GET /fetch
    gets the web page from the given url and provides a custom output to the user; adds 0.5 seconds of delay to the process
    """
    log.info('start fetching')
    text = ''
    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:
            text += 'Status:' + str(response.status)
            text += '\nContent-type:'+str(response.headers['content-type'])
            await asyncio.sleep(0.5)
            html = await response.text()
            text += '\nBody:' + html[:15]+'...'
            text += '\n{"data": 1}'
            await session.close()
    log.info('done fetching')
    return web.Response(text=text)

@routes.get("/shutdown")
async def shutdown(request):
    """
    GET /shutdown
    shuts down the app gracefully
    !!Warning!!: app.shutdown() does not exit the process, as the graceful shutdown is not available in aiohttp as of now. Refer : https://github.com/aio-libs/aiohttp/issues/2950#issuecomment-814821555
    Manual process exit is applied through exit()
    """
    log.warning('!!Warning!!: app.shutdown() does not exit the process, as the graceful shutdown is not available in aiohttp as of now. Refer : https://github.com/aio-libs/aiohttp/issues/2950#issuecomment-814821555. Manual process exit is applied through exit()')
    log.info('exiting gracefully')
    await app.shutdown()
    await app.cleanup()
    exit()
    # raise GracefulExit()


# async def bootup(this_app):
#     asyncio.create_task(background())

# async def background():
#     await asyncio.sleep(5)


if __name__ == "__main__":
    app.add_routes(routes)
    # app.on_startup.append(bootup)
    web.run_app(app, host="0.0.0.0", port=8080)




