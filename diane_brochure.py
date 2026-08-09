#!/usr/bin/env python3
"""
Diane Bathroom Brochure Launcher - DJM Project Pro's
Run:  python diane_brochure.py
"""

import http.server
import socketserver
import webbrowser
import os
import sys
import threading
import time

PORT = 8765
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "diane-brochure")


def check():
    needed = ["index.html", "optA.jpg", "optB.jpg", "optC.jpg",
              "optD.jpg", "optE.jpg", "optF.jpg"]
    missing = [f for f in needed if not os.path.isfile(os.path.join(DIR, f))]
    if missing:
        print("Missing files:")
        for m in missing:
            print(" ", m)
        sys.exit(1)


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIR, **kwargs)

    def log_message(self, format, *args):
        pass  # silence normal requests


def serve():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("Serving at http://localhost:%d" % PORT)
        print("Press Ctrl+C to stop")
        httpd.serve_forever()


def main():
    print("=" * 50)
    print("  DJM Project Pro's - Diane Bathroom Brochure")
    print("=" * 50)

    if not os.path.isdir(DIR):
        print("ERROR: diane-brochure folder not found next to this script.")
        sys.exit(1)

    check()

    t = threading.Thread(target=serve, daemon=True)
    t.start()
    time.sleep(0.5)

    url = "http://localhost:%d" % PORT
    print("Opening", url)
    webbrowser.open(url)

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nStopped.")
        sys.exit(0)


if __name__ == "__main__":
    main()
