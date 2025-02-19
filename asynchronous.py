import asyncio
import time

async def makeCoffee():
    print("This is making coffee")
    await asyncio.sleep(2)
    print("Coffee made")
    return "Coffee is ready to consume"

async def makeToast():
    print("This is making Toast")
    await asyncio.sleep(3)
    print("Toast made")
    return "Toast is ready to consume"

async def peelBanana():
    print("This is peeling banana")
    await asyncio.sleep(2)
    print("Banana ready")
    return "Banana is ready to consume"


async def main():
    startTime = time.time()
    coffeeRes,toastRes,resultBanana = await asyncio.gather(makeCoffee(),makeToast(),peelBanana())

    # coffeeRes,toastRes,resultBanana = await asyncio.gather(makeCoffee(),makeToast(),peelBanana())
    # coffeeRes,toastRes,resultBanana = makeCoffee(),makeToast(),peelBanana()
    endTime = time.time()
    print("Coffee ",coffeeRes)
    print("Toast ",toastRes)
    print("Banana ",resultBanana)
    print("Total Time taken ",endTime-startTime)

if __name__ == '__main__':
    asyncio.run(main())
