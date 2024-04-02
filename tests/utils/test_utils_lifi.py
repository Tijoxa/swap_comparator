import requests

from swap_comparator.utils.constant import from_address_LiFi, ChainList, EtherscanMainnet


def test_LiFi_API():
    api_url = "https://li.quest/v1/quote"
    headers = {"accept": "application/json"}
    params = {
        "fromChain": ChainList.ETH.ID,
        "toChain": ChainList.ETH.ID,
        "fromToken": EtherscanMainnet.USDC.token_address,
        "toToken": EtherscanMainnet.USDT.token_address,
        "fromAddress": from_address_LiFi,
        "fromAmount": str(1 * 10**EtherscanMainnet.USDC.decimals),
    }

    response = requests.get(api_url, headers=headers, params=params)

    assert response.status_code == 200, f"Error in Response: {response.text}"
