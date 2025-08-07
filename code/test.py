import websocket, json, ssl

def on_open(ws):
    # ws.send(json.dumps({
    #     "event": "bts:subscribe",
    #     "data": {"channel": "live_trades_avaxeur"}
    # }))
    ws.send(json.dumps({
        "event": "bts:subscribe",
        "data": {"channel": "order_book_avaxeur"}
    }))

def on_message(ws, message):
    print("Received:", message)

def on_error(ws, error):
    print("Error:", error)

def on_close(ws):
    print("Connection closed")

ws = websocket.WebSocketApp("wss://ws.bitstamp.net",
                            on_open=on_open,
                            on_message=on_message,
                            on_error=on_error,
                            on_close=on_close)
ws.run_forever(sslopt={'cert_reqs': ssl.CERT_NONE})
