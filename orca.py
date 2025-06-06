import requests
import winsound
import time

# API endpoint
url = "https://api.orca.so/v2/solana/pools/HxA6SKW5qA4o12fjVgTpXdq2YnZ5Zv1s7SB4FFomsyLM"
lower_price = 103489.257
upper_price = 108969.195

while True:
    try:
        # Step 1: Make the API call
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()

        # Step 2: Get the value of "price"
        price = float(data["data"]["price"])
        if price is None:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error: 'price' key not found in API response")
            time.sleep(60)  # Wait 1 minute before retrying
            continue

        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Current price: {price}")

        # Step 3: Check if price is below 100,000 or above 105,000
        if price < lower_price or price > upper_price:
            # Make a beeping noise (frequency: 1000 Hz, duration: 500 ms)
            winsound.Beep(1000, 500)
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Price is out of range! Beeping...")
        else:
            print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Price is within range.")

    except requests.exceptions.RequestException as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error making API call: {e}")
    except ValueError as e:
        print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] Error parsing JSON response: {e}")

    # Wait 1 minute before the next API call
    time.sleep(60)
