#!/bin/bash
# Grep allowed methods
curl -sIL "$1" -X OPTIONS | grep '^Allow:' | awk -F ": " '{print $2}'
