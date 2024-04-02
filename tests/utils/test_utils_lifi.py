import requests

from swap_comparator.utils.constant import from_address_LiFi, ChainList, EtherscanMainnet


def test_LiFi_API():
    fromChain = ChainList.ETH.ID
    toChain = ChainList.ETH.ID
    fromToken = EtherscanMainnet.USDC.token_address
    toToken = EtherscanMainnet.USDT.token_address
    fromAddress = from_address_LiFi
    fromAmount = str(1 * 10**EtherscanMainnet.USDC.decimals)
    url = f"https://li.quest/v1/quote?fromChain={fromChain}&toChain={toChain}&fromToken={fromToken}&toToken={toToken}&fromAddress={fromAddress}&fromAmount={fromAmount}"

    headers = {"accept": "application/json"}

    response = requests.get(url, headers=headers)

    assert response.status_code == 200, f"Error in Response: {response.text}"
