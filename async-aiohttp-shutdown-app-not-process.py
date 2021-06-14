import asyncio
from aiohttp import web
import aiohttp

app = web.Application()
routes = web.RouteTableDef()


@routes.get("/")
async def hello(request):
    """
    GET /
    greets world
    """
    text = 'hello world'
    return web.Response(text=text)

@routes.get("/hello/{name}")
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
    print('start fetching')
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
    print('done fetching')
    return web.Response(text=text)

@routes.get("/shutdown")
async def shutdown(request):
    """
    GET /shutdown
    shuts down the app gracefully
    !!Warning!!: This shutdown does not exit the process, as the graceful shutdown is not available in aiohttp as of now. Refer : https://github.com/aio-libs/aiohttp/issues/2950#issuecomment-814821555
    Manual process kill is suggested
    """
    await app.shutdown()
    await app.cleanup()
  

async def bootup(this_app):
    asyncio.create_task(background())

async def background():
    await asyncio.sleep(5)
    print("Start shutting down")
    await app.shutdown()
    print("Start cleaning up")
    await app.cleanup()

if __name__ == "__main__":
    app.add_routes(routes)
    app.on_startup.append(bootup)
    web.run_app(app, host="0.0.0.0", port=8080)
    print("Finished")



