from core.application import Application
from core.response import Response

app = Application()


@app.route("/")
async def hello(request):
    return Response("Hello, world!")


@app.route("/another")
async def another_route(request):
    return Response("This is another route!")
