import aiohttp
import asyncio
import datetime
import logging

import swap_comparator.log_config
from swap_comparator.constant import ID0xSwap, RPS0xSwap, AmountCategory, Mainnet, ArbiscanMainnet, EtherscanMainnet, ChainList, Chain


async def run_0x(data: list[dict], timestamp: datetime.datetime):
    tasks = []

    for amount_stable_coin in AmountCategory.stable_coin:
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.USDT, amount_stable_coin))
        tasks.append(update_data(data, timestamp, ChainList.ETH, EtherscanMainnet.USDC, EtherscanMainnet.DAI, amount_stable_coin))

    for amount_WETH in AmountCategory.WETH:
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
        await asyncio.sleep(1 / RPS0xSwap)


async def update_data(
    data: list[dict],
    timestamp: datetime.datetime,
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in_unit: float,
):
    to_add = await get_0x_price(
        token_in=token_in,
        token_out=token_out,
        amount_in=int(amount_in_unit * 10**token_in.decimals),
    )
    try:
        amount_out_unit = float(to_add["grossBuyAmount"]) / 10**token_out.decimals
        elem = {
            "timestamp": timestamp,
            "platform": "0xSwap",
            "chainId": chain.ID,
            "fromToken": token_in.symbol,
            "toToken": token_out.symbol,
            "gasCost": "",
            "amountIn": amount_in_unit,
            "amountOut": amount_out_unit,
        }
        data.append(elem)
    except KeyError:
        logging.error(f"KeyError on response {to_add}")


async def get_0x_price(
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in: int,
) -> dict:
    api_url = "https://api.0x.org/swap/v1/quote"
    requestOptions = {
        "headers": {"0x-api-key": ID0xSwap},
        "body": {},
        "params": {
            "sellToken": token_in.token_address,
            "buyToken": token_out.token_address,
            "sellAmount": amount_in,
        },
    }

    headers = requestOptions.get("headers", {})
    params = requestOptions.get("params", {})

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, headers=headers, params=params) as response:
                if response.status != 200:
                    logging.error(f"""Error {response.status} while fetching {api_url}
The parameters were: {params}
The response was: {await response.text()}""")
                    return {}
                return await response.json()
        except asyncio.TimeoutError:
            logging.error(f"Timeout error occurred while fetching {api_url}")
