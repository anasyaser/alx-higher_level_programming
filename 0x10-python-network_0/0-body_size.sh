#!/usr/bin/bash
# Display the body size
curl -s "$1" | wc -c
