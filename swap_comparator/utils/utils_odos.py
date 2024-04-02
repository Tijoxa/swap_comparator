import aiohttp
import asyncio
import datetime

from swap_comparator.utils.constant import RPSOdos, AmountCategory, Mainnet, ArbiscanMainnet, EtherscanMainnet, ChainList, Chain


async def run_odos(data: list[dict], timestamp: datetime.datetime):
    tasks = []

    for amount_stable_coin in AmountCategory.stable_coin:
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.USDC, ArbiscanMainnet.USDT, amount_stable_coin))

        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.USDT, amount_stable_coin))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.DAI, amount_stable_coin))

    for amount_WETH in AmountCategory.WETH:
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.USDC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.USDT, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ARBITRUM, ArbiscanMainnet.WETH, ArbiscanMainnet.ARB, amount_WETH))

        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.WBTC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.USDC, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.USDT, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.WSTETH, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.MKR, amount_WETH))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.WETH, EtherscanMainnet.PEPE, amount_WETH))

    for amount_WBTC in AmountCategory.WBTC:
        pass

    for task in tasks:
        await task
        await asyncio.sleep(1 / RPSOdos)


async def update_data(
    data: list[dict],
    timestamp: datetime.datetime,
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in_unit: float,
):
    to_add = await get_odos_price(
        chain=chain,
        token_in=token_in,
        token_out=token_out,
        amount_in=int(amount_in_unit * 10**token_in.decimals),
    )
    try:
        amount_out_unit = float(to_add["outAmounts"][0]) / 10**token_out.decimals
        elem = {
            "timestamp": timestamp,
            "platform": "Odos",
            "chainId": chain.ID,
            "fromToken": token_in.symbol,
            "toToken": token_out.symbol,
            "gasCost": "",
            "amountIn": amount_in_unit,
            "amountOut": amount_out_unit,
        }
        data.append(elem)
    except KeyError:
        print(f"KeyError on response {to_add}")


async def get_odos_price(
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in: int,
) -> dict:
    quote_url = "https://api.odos.xyz/sor/quote/v2"

    quote_request_body = {
        "chainId": chain.ID,
        "inputTokens": [
            {
                "tokenAddress": token_in.token_address,
                "amount": str(amount_in),
            }
        ],
        "outputTokens": [
            {
                "tokenAddress": token_out.token_address,
                "proportion": 1,
            }
        ],
        "slippageLimitPercent": 0.1,
        "userAddr": "0x0000000000000000000000000000000000000000",
        "referralCode": 0,
        "disableRFQs": True,
        "compact": True,
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.post(quote_url, headers={"Content-Type": "application/json"}, json=quote_request_body) as response:
                if response.status != 200:
                    print(
                        f"""Error {response.status} while fetching {quote_url}
The parameters were: {quote_request_body}
The response was: {await response.text()}
"""
                    )
                    return {}
                return await response.json()
        except asyncio.TimeoutError:
            print(f"Timeout error occurred while fetching {quote_url}")
