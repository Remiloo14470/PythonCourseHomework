import asyncio


async def start_strongman(name, power):
    ball_num = 1
    print(f'Силач {name} начал соревнования')
    while ball_num <= 5:
        print(f'Силач {name} поднял {ball_num} шар')
        await asyncio.sleep(1/power)
        ball_num+=1
    print(f'Силач {name} закончил соревнования')


async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Vlad', 3))
    task2 = asyncio.create_task(start_strongman("Den", 4))
    task3 = asyncio.create_task(start_strongman("Yoda", 5))
    await task1
    await task2
    await task3


asyncio.run(start_tournament())
