import requests

from swap_comparator.utils.constant import ChainList, EtherscanMainnet


def test_Odos_API():
    quote_url = "https://api.odos.xyz/sor/quote/v2"

    quote_request_body = {
        "chainId": ChainList.ETH.ID,
        "inputTokens": [
            {
                "tokenAddress": EtherscanMainnet.WETH.token_address,
                "amount": str(1 * 10**EtherscanMainnet.WETH.decimals),
            }
        ],
        "outputTokens": [
            {
                "tokenAddress": EtherscanMainnet.USDC.token_address,
                "proportion": 1,
            }
        ],
        "slippageLimitPercent": 0.1,
        "userAddr": "0x0000000000000000000000000000000000000000",
        "referralCode": 0,
        "disableRFQs": True,
        "compact": True,
    }

    response = requests.post(quote_url, headers={"Content-Type": "application/json"}, json=quote_request_body)

    assert response.status_code == 200, f"Error in Quote: {response.json()}"
