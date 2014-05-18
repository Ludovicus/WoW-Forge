#!/usr/bin/env python

import wf.schedule
import sys

if __name__ == "__main__":
    region = "US"

    if len(sys.argv) > 1:
        region = sys.argv[1]
        realms = sys.argv[2:]
    else:
        realms = None

    wf.schedule.Schedule_AH(region, realms)
