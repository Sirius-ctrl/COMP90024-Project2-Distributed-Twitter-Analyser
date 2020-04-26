# !flask/bin/python
"""
Author:      XuLin Yang & Renjie Meng
Student id:  904904 & 877396
Date:        2020-4-24 01:09:38
Description: backend flask application
"""

import argparse
import sys

from app.resources import app


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-test', help='test the compilation of the application')
    parser.add_argument('-h', help='host address')
    parser.add_argument('-p', help='host port number')
    args = parser.parse_args()

    if args.test:
        print("Successfully compiled")
        sys.exit(0)

    app.run(debug=True, host='0.0.0.0')