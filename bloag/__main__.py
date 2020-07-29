#!/usr/bin/env python3

import os
import sys

if __name__ == '__main__':
    sys.path.insert(1, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

    from bloag.bloag import main
    main()
