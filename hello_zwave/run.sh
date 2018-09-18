#!/bin/bash
set -e

cp /z-wave-graph.html /config/www

python3 zwave.py

