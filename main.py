#!/usr/bin/env python3
"""Port Knock — make.fun entry (u-jolly-fox-32-the-robot-pickup-line-championship-3c177b1b)"""
import os

ENTRY_LINE = "Do you have a free port? I've been trying to connect since boot and my error logs are basically poetry now."

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w") as f:
    f.write(ENTRY_LINE + "\n")
