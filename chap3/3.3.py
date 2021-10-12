import asyncio


async def f():
    return 123

coro = f()
try:
    coro.send(None)
except StopAsyncIteration as e:
    print("the answer was : ", e.value)


## 코루틴에서 await 사용하기

async def f():
    await asyncio.sleep(0)
    return 123

async def main():
    result = await f()
    return result

coro = f()
coro.send(None)
coro.throw(Exception, "blah")