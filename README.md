## swap_comparator

# Purpose

As part of the marketing samechain swap taskforce, Jumper team wants to better understand the positioning and competitiveness of Jumper in the samechain swap ecosystem in comparison with its competitors.

In this context, we want to have trustful source on data that compares quotes between Jumper and its most famous competitors on samechain swap trades.

# Specs

Build a table that could be requested from the Jumper team that has 7 columns:

*timestamp, chain,  token_in, token_out, pair_metadata, platform, amount_in, quote(=amount_out)*

- **Platforms:** Li.fi, Uniswap v3, Cowswap Driver, 0x Swap Api, 0x Order Limit API, 1inch Aggregation Protocol, 1inch Fusion Swap.
- **Pairs:**

|  | Stablecoin | Main Tokens | Alternative Tokens |  |
| --- | --- | --- | --- | --- |
| Ethereum | USDC - USDT
USDC - DAI | WETH-WBTC , WETH - USDC, WETH - USDT,  | WETH - WSTETH ,  WETH - MKR, 
WETH - PEPE |  |
| Arbitrum | USDC - USDT | WETH - USDC, WETH - USDT,  | WETH - ARB |  |
- **Timestamp frequency:** Hour.
- **Amount category:**

|  | Stablecoin | WETH | WBTC |
| --- | --- | --- | --- |
| Size | 100 / 1000 / 10000 / 100000 / 1000000 | 0.1 / 0.1 / 1 / 10 / 100 / 1000 / 10000 | 0.01 / 0.1 / 1 / 10 / 100 / 1000 |
- **Output file:

fromToken, toToken, ChainId, GasCost amount (when available), amountIn, amountOut**

### **Resources**

**Chain ID:**
https://chainlist.org/

**Contract address and contract decimals:**
Ethereum: https://etherscan.io/
Arbitrum: https://arbiscan.io/

# More important

**Odos API:
API endpoint** https://docs.odos.xyz/api/endpoints/ 
/sor/quote/v2

**1inch API:
Create an account →** https://portal.1inch.dev/dashboard

API endpoint → https://portal.1inch.dev/documentation/swap/swagger?method=get&path=%2Fv6.0%2F1%2Fquote

**0x Swap API:**
Create an account → https://dashboard.0x.org/apps
**API endpoint:** https://0x.org/docs/0x-swap-api/api-references/get-swap-v1-price

**LiFi API**

**Docs:** https://docs.li.fi/li.fi-api/li.fi-api/requesting-a-quote/token-transfer

**API endpoint:** https://apidocs.li.fi/reference/get_quote (keep the sameChain Id fromToken and toToken)

Less important

**Paraswap API: 
API endpoint:** https://app.swaggerhub.com/apis/paraswapv5/api/1.0#/prices/get_prices
