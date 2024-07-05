import requests

from swap_comparator.constant import ID0xSwap, EtherscanMainnet


# TODO: test on Arbitrum
def test_0x_API():
    api_url = "https://api.0x.org/swap/v1/quote"
    requestOptions = {
        "headers": {"0x-api-key": ID0xSwap},
        "body": {},
        "params": {
            "sellToken": EtherscanMainnet.USDC.token_address,
            "buyToken": EtherscanMainnet.WETH.token_address,
            "sellAmount": 1 * 10**EtherscanMainnet.USDC.decimals,
        },
    }

    headers = requestOptions.get("headers", {})
    params = requestOptions.get("params", {})

    response = requests.get(api_url, headers=headers, params=params)

    assert response.status_code == 200, f"Error in Response: {response.text}"
