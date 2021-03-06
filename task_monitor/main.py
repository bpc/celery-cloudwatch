__author__ = 'nathan.muir'

import sys
from lib import Options, TaskMonitor

if __name__ == '__main__':
    options = Options()
    args = options.parse()

    monitor = TaskMonitor(args)

    monitor.run()

