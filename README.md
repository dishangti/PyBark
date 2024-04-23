# PyBark
Push important notifications to iOS devices using Bark app and Python3.

### Example
Push an AES-256-CBC encrypted message to your iPhone:

`./iPhone/server.txt` is your server link, and the default is
```
https://api.day.app
```

`./iPhone/device.txt` is your device key which can be found on the link of your Bark App. For example, if the __Body Text__ in your app reads `https://api.day.app/xxxxxxxxxxxxxxxxxxxxxx/Body Text`, your device key is `xxxxxxxxxxxxxxxxxxxxxx`, and you should write
```
xxxxxxxxxxxxxxxxxxxxxx
```

`./iPhone/aes.txt` is your AES encryption key (first line) and IV (second line). In CBC mode, key length should be 16 bytes (128 bits), 24 bytes (192 bits), or 32 bytes (256 bits), and IV should be 16 bytes. Here we use AES-256-CBC cipher, so it may be
```
]QR6q9FZ!?^o2h*KQ5m}6f]j:roX>f5A
!tr.)~5ke+rhe)8W
```

`./example.py` is the example code to use PyBark
```python
from pybark import PyBark
bk = PyBark('./iPhone', True)
bk.send('Hello World!')
```
