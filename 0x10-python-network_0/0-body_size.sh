#!/bin/bash
# A script that takes in a URL,and dsplay the size of the body of the response.
curl -sl "$1" | wc -c
