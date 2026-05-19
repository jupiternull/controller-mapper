#!/usr/bin/env python3
import struct, sys

EVENT_FORMAT = "IhBB"
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

JS_EVENT_BUTTON = 0x01
JS_EVENT_AXIS   = 0x02
JS_EVENT_INIT   = 0x80

print("Press each button/stick direction on your N64 controller.")
print("Ctrl+C to quit.\n")

with open("/dev/input/js0", "rb") as f:
    while True:
        event = f.read(EVENT_SIZE)
        if not event:
            break
        time, value, type_, number = struct.unpack(EVENT_FORMAT, event)
        etype = type_ & ~JS_EVENT_INIT
        if etype == JS_EVENT_BUTTON and value == 1:
            print(f"BUTTON {number:2d} pressed")
        elif etype == JS_EVENT_AXIS and abs(value) > 10000:
            direction = "+" if value > 0 else "-"
            print(f"AXIS   {number:2d} {direction}  (value={value})")
