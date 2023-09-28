#!/bin/bash
# Display the body of 200 response
if [ "$(curl -sIL "$1" -X GET | head -1 | cut -d ' ' -f 2)" = '200' ]; then curl -s "$1"; fi
