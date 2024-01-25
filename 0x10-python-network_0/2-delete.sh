#!/bin/bash
# A script that sends DELETE request as first argument and displays the body of the response.
curl -sX DELETE "$1"
