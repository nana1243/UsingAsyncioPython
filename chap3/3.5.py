import asyncio
from asyncio import Future

f = Future()
f.done()


# Task를 써야하는 것이 일반적이지만,
# Future를 사용해야 하는 경우가 존재함

async def main(f:asyncio.Future):
    await asyncio.sleep(10)
    f.set_result("i have finished!")

loop = asyncio.get_event_loop()
fut = asyncio.Future()
loop.create_task(main(fut))
print("####################")
print(loop.run_until_complete(fut))
print(fut.done())
print(fut.result())
print("####################")
