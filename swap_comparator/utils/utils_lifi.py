import aiohttp
import asyncio
import datetime
import logging

import swap_comparator.log_config
from swap_comparator.constant import from_address_LiFi, RPSLiFi, AmountCategory, Mainnet, ArbiscanMainnet, EtherscanMainnet, ChainList, Chain


async def run_lifi(data: list[dict], timestamp: datetime.datetime):
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
        await asyncio.sleep(1 / RPSLiFi)


async def update_data(
    data: list[dict],
    timestamp: datetime.datetime,
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in_unit: float,
):
    to_add = await get_lifi_price(
        chain=chain,
        token_in=token_in,
        token_out=token_out,
        amount_in=int(amount_in_unit * 10**token_in.decimals),
    )
    try:
        amount_out_unit = float(to_add["estimate"]["toAmount"]) / 10**token_out.decimals
        elem = {
            "timestamp": timestamp,
            "platform": "LiFi",
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


async def get_lifi_price(
    chain: Chain,
    token_in: Mainnet,
    token_out: Mainnet,
    amount_in: int,
) -> dict:
    api_url = "https://li.quest/v1/quote"
    headers = {"accept": "application/json"}
    params = {
        "fromChain": chain.ID,
        "toChain": chain.ID,
        "fromToken": token_in.token_address,
        "toToken": token_out.token_address,
        "fromAddress": from_address_LiFi,
        "fromAmount": str(amount_in),
    }

    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(api_url, headers=headers, params=params) as response:
                if response.status != 200:
                    logging.error(
                        f"""Error {response.status} while fetching {api_url}
The parameters were: {params}
The response was: {await response.text()}"""
                    )
                    return {}
                return await response.json()
        except asyncio.TimeoutError:
            logging.error(f"Timeout error occurred while fetching {api_url}")
