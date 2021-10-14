import asyncio

# 언제나 같은 루프 얻기
loop = asyncio.get_event_loop()
loop2 = asyncio.get_event_loop()

# 변수 loop와 loop2는 동일한 인스턴스를 참조한다.
print (loop is loop2) # True


# get_running_loop()가 도입된 이후로부터,
# 루프 인스턴스를 생성하지 않더라도 사용가능함
async def g():
    print("test")

async def f():
    for i in range(10):
        asyncio.create_task()

