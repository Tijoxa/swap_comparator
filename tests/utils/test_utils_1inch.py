import requests

from swap_comparator.utils.constant import ID1inch, ChainList, ArbiscanMainnet


def test_1inch_API():
    method = "get"
    apiUrl = f"https://api.1inch.dev/swap/v6.0/{ChainList.ARBITRUM.ID}/quote"
    requestOptions = {
        "headers": {"Authorization": f"Bearer {ID1inch}"},
        "body": {},
        "params": {"src": ArbiscanMainnet.USDC.token_address, "dst": ArbiscanMainnet.USDT.token_address, "amount": 100},
    }

    headers = requestOptions.get("headers", {})
    body = requestOptions.get("body", {})
    params = requestOptions.get("params", {})

    response = requests.get(apiUrl, headers=headers, params=params)

    assert response.status_code == 200, f"Error in Response: {response.text}"
