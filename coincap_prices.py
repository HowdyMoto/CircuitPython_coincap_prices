import os
import adafruit_connection_manager
import wifi
import adafruit_requests

class CoincapPriceChecker:

    URL = "http://api.coincap.io/v2/assets/"
    BTC_URL = "http://api.coincap.io/v2/assets/bitcoin"
    ETH_URL = "http://api.coincap.io/v2/assets/ethereum"
    XMR_URL = "http://api.coincap.io/v2/assets/monero"

    def __init__(self):

        # Get WiFi details, ensure these are setup in settings.toml
        ssid = os.getenv("CIRCUITPY_WIFI_SSID")
        password = os.getenv("CIRCUITPY_WIFI_PASSWORD")

        rssi = wifi.radio.ap_info.rssi

        print(f"\nConnecting to {ssid}...")
        try:
            # Connect to the Wi-Fi network
            wifi.radio.connect(ssid, password)
        except OSError as e:
            print(f"❌ OSError: {e}")
        print("✅ Wifi connected!")

        # Initalize Wifi, Socket Pool, Request Session
        self.pool = adafruit_connection_manager.get_radio_socketpool(wifi.radio)
        self.ssl_context = adafruit_connection_manager.get_radio_ssl_context(wifi.radio)
        self.requests = adafruit_requests.Session(self.pool, self.ssl_context)

    def get_price(self, coin_name):
        try:
            response = self.requests.get(self.URL + coin_name)
            if response.status_code == 200:
                response_json = response.json()

                price = float(response_json["data"]["priceUsd"])
                price_delta = float(response_json["data"]["changePercent24Hr"])    # get the percentage change, which can be many decimal places

                print("Price =", f"{price:.2f}"
)
                print("Delta =", price_delta)

                return price, price_delta
            else:
                print("status code is not 200")
                return 0, 0

        except (ValueError, RuntimeError) as e:
            print("Error: ", e)

    def get_btc_price(self):
        return self.get_price("bitcoin")
