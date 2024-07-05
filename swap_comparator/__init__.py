import asyncio
import csv
import datetime
import os

from swap_comparator.utils import run_1inch, run_odos, run_0x, run_lifi, run_paraswap


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
        run_odos(data, datetime_up_to_hour),
        run_0x(data, datetime_up_to_hour),
        run_lifi(data, datetime_up_to_hour),
        run_paraswap(data, datetime_up_to_hour),
    )

    os.makedirs("data", exist_ok=True)
    write_on_timestamp(os.path.join("data", "timestamp.csv"), data)
