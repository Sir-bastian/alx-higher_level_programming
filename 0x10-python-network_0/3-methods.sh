#!/bin/bash
#A script that takes a URL and displays all HTTP methods the server will accept.
curl -sI "$1"
