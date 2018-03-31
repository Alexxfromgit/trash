#!/bin/bash
#
# >/dev/null redirects the command standard output to the null device, 
# which is a special device which discards the information written to it. 
# 2 >&1 redirects the standard error stream
# to the standard output stream (stderr = 2, stdout = 1).
#
exec 1> /dev/null 2>&1
