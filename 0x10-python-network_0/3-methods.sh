#!/bin/bash
# Grep allowed methods
curl -sIL "$1" -X OPTIONS | grep '^Allow:' | cut -d ' ' -f 2
