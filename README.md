This is a simple CircuitPython library for getting crypto prices from CoinCap
It assumes integrated wifi, such as found on an ESP32-S3. It does not work with ESP32 Wi-Fi coprocessors (though it could with very minor modifications)

# To use
In the code below, you coudl substitute "bitcoin" with the name of any other cryptocurrency, as per CoinCap's naming conventions.
```
import coincap_prices
CPC = coincap_prices.CoincapPriceChecker()
price, delta = CPC.get_price("bitcoin")
print("price=", price)
print("delta=", delta)
```
