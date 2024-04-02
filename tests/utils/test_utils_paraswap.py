import requests

from swap_comparator.utils.constant import ChainList, EtherscanMainnet


def test_ParaSwap_API():
    api_url = "https://apiv5.paraswap.io/prices"
    headers = {"accept": "application/json"}
    params = {
        "srcToken": EtherscanMainnet.WETH.token_address,
        "srcDecimals": EtherscanMainnet.WETH.decimals,
        "destToken": EtherscanMainnet.USDT.token_address,
        "destDecimals": EtherscanMainnet.USDT.decimals,
        "amount": 10**EtherscanMainnet.WETH.decimals,
        "side": "SELL",
        "network": ChainList.ETH.ID,
    }

    response = requests.get(api_url, headers=headers, params=params)

    assert response.status_code == 200, f"Error in Response: {response}"
