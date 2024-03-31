import csv
import os
import time


def write_on_timestamp(path: str, data: dict):
    file_exists = os.path.isfile(path)

    with open(path, "w") as csvfile:
        # "timestamp",
        # "chain",
        # "token_in",
        # "token_out",
        # "pair_metadata",
        # "platform",
        # "amount_in",
        # "amount_out",
        headers = [
            "fromToken",
            "toToken",
            "chainId",
            "gasCostAmount",
            "amountIn",
            "amountOut",
        ]
        writer = csv.DictWriter(csvfile, delimiter=",", lineterminator="\n", fieldnames=headers)

        if not file_exists:
            writer.writeheader()

        writer.writerow(data)


def main():
    write_on_timestamp(os.path.join("data", "timestamp.csv"), {})


if __name__ == "__main__":
    main()
