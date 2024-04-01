import asyncio
import csv
import os
import datetime

from swap_comparator.utils.utils_1inch import run_1inch


def write_on_timestamp(path: str, data: list[dict]):
    file_exists = os.path.isfile(path)

    with open(path, "a") as csvfile:
        headers = [
            "timestamp",
            "platform",
            "chainId",
            "fromToken",
            "toToken",
            "gasCost",
            "amountIn",
            "amountOut",
        ]
        writer = csv.DictWriter(csvfile, delimiter=",", lineterminator="\n", fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        for row in data:
            writer.writerow(row)


async def run_each_hour():
    current_datetime = datetime.datetime.now()
    datetime_up_to_hour = current_datetime.replace(minute=0, second=0, microsecond=0)
    data = []

    await asyncio.gather(
        run_1inch(data, datetime_up_to_hour),
    )

    write_on_timestamp(os.path.join("data", "timestamp.csv"), data)


async def main():
    await run_each_hour()


if __name__ == "__main__":
    asyncio.run(main())
