import requests

from constant import MainnetAddress, ID1inch


def get_1inch_price(
    token_in: str,
    token_out: str,
    amount_in: float,
    method: str = "get",
    apiUrl: str = "https://api.1inch.dev/swap/v6.0/1/quote",
) -> dict:
    headers = {"Authorization": f"Bearer {ID1inch}"}
    body = {}
    params = {
        "src": token_in,
        "dst": token_out,
        "amount": amount_in,
    }

    response = requests.get(apiUrl, headers=headers, params=params)

    return response.json()


if __name__ == "__main__":
    get_1inch_price(
        token_in=MainnetAddress.WETH,
        token_out=MainnetAddress.WBTC,
        amount_in=1e18,
    )
