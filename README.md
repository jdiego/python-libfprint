# Requirements

- Cython >= 0.27
- libfprint == 0.99.0

# Install

```
pip install git+git://github.com/jdiego/python-libfprint.git
```

# Usage

```python
import fprint

fprint.init()
devices = fprint.DiscoveredDevices()

if len(devices) > 0:
    dev = devices[0].open_device()
    print_data = dev.enroll_finger_loop()
    print_data = fprint.PrintData.from_data(print_data.data)
    result = dev.verify_finger_loop(print_data)
    assert result is True
    dev.close()
```

