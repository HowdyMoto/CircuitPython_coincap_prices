# CircuitPython_coincap_prices
Simple library for getting crypto prices from CoinCap

## To use
```
import coincap_prices
CPC = coincap_prices.CoincapPriceChecker()
price, delta = CPC.get_price("bitcoin")
print("price=", price)
print("delta=", delta)
```
