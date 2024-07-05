import asyncio
from swap_comparator import run_each_hour


async def main():
    await run_each_hour()


if __name__ == "__main__":
    asyncio.run(main())
