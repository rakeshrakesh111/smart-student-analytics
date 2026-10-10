"""One-command launcher:  python run.py   (add --regen to rebuild raw data, --no-serve to skip the web server)"""
import argparse, functools, http.server, socketserver, sys, threading, webbrowser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "src"))
import generate_data, pipeline  # noqa: E402


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--regen", action="store_true", help="regenerate synthetic raw CSVs")
    ap.add_argument("--no-serve", action="store_true")
    ap.add_argument("--port", type=int, default=8000)
    args = ap.parse_args()

    if args.regen or not (ROOT / "data" / "raw" / "academic.csv").exists():
        generate_data.generate()
    pipeline.run()
    if args.no_serve:
        return
    handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(ROOT / "dashboard"))
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", args.port), handler) as srv:
        url = f"http://localhost:{args.port}"
        print(f"\nDashboard running at {url}  (Ctrl+C to stop)")
        threading.Timer(1, lambda: webbrowser.open(url)).start()
        try:
            srv.serve_forever()
        except KeyboardInterrupt:
            print("\nStopped.")


if __name__ == "__main__":
    main()
