import asyncio
from aioredis import create_redis

class A:
    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if self.x > 2:
            raise StopIteration
        else:
            self.x += 1
            return self.x

for i in A():
    print(i)

print('아래는 비동기 for')


class OneAtTime:
    def __init__(self,redis, keys):
        self.redis = redis
        self.keys = keys

    def __aiter__(self):
        self.ikeys = iter(self.keys)
        return self

    async def __anext__(self):
        try:
            k = next(self.keys)
        except StopIteration:
            raise StopAsyncIteration
        value = await self.redis.get(k)
        return value


async def main():
    redis = await create_redis(("localhost",6379))
    keys = ["Americas", "Africa", "Europe", "Asia"]


    # async를 사용하면 , 중요한점은 반복중에 다음데이터를 얻기 위해
    # 반복 자체를 멈출 수 있다는 것이다.
    async for value in OneAtTime(redis, keys):
        await print(value)

