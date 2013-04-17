#!/bin/sh
ps -auxe | sort -k9 | awk '{print $9,$11}' | uniq | grep "chrome\|firefox"
