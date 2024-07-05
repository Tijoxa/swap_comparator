import pytest
import requests
from swap_comparator.constant import ID1inch, ChainList, ArbiscanMainnet


@pytest.mark.api
def test_1inch_API():
    api_url = f"https://api.1inch.dev/swap/v6.0/{ChainList.ARBITRUM.ID}/quote"
    requestOptions = {
        "headers": {"Authorization": f"Bearer {ID1inch}"},
        "body": {},
        "params": {
            "src": ArbiscanMainnet.USDC.token_address,
            "dst": ArbiscanMainnet.USDT.token_address,
            "amount": 100,
        },
    }

    headers = requestOptions.get("headers", {})
    params = requestOptions.get("params", {})

    response = requests.get(api_url, headers=headers, params=params)

    assert response.status_code == 200, f"Error in Response: {response.text}"
