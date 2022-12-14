"""
- python 3.4 -> 비동기 표준라이브러리
import asyncio

- python 3.7 미만
asyncio.get_event_loop().run_until_complete(task())
- python 3.7 이상
asyncio.run(task()) (아직은 버그가 있음)

async func():
    await task1()
    await task2()
    ...

    await asyncio.wait([
        task1(),
        task2(),
        task3(),
    ])

비동기 안에서는 비동기를 호출해야 한다.
requests 은 sync 방식으로 동작한다.
따라서 async 함수 내부에서 사용해서는 안된다.
aiohttp 는 async 방식으로 동작하는 http 관련 라이브러리이다.

<< aiohttp >>
s = aiohttp.ClientSession()
t = asyncio.ensure_future(task(a, b))
tasks.append(t)
await asyncio.gather(*tasks, return_exceptions=True)
"""
