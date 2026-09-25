import argparse
import json
import time
from datetime import datetime, timezone
from pathlib import Path
from urllib.request import Request, urlopen

URL = "https://api.opschugex.com/health"


def verify():
    started = time.perf_counter()
    request = Request(URL, headers={"User-Agent": "OpsChugex-Evidence/1.0"})
    with urlopen(request, timeout=15) as response:
        status_code = response.status
        payload = json.loads(response.read().decode("utf-8"))
    latency_ms = round((time.perf_counter() - started) * 1000, 2)

    assert status_code == 200, f"Unexpected HTTP status: {status_code}"
    assert payload.get("status") == "healthy", payload
    assert payload.get("service") == "opschugex-api", payload
    assert payload.get("database") == "connected", payload
    assert payload.get("scheduler") == "running", payload

    return {
        "evidence_id": "OCX-LIVE-001",
        "classification": "verified-live-service-check",
        "checked_at_utc": datetime.now(timezone.utc).isoformat(),
        "endpoint": "api.opschugex.com/health",
        "http_status": status_code,
        "latency_ms": latency_ms,
        "service": payload["service"],
        "service_status": payload["status"],
        "database": payload["database"],
        "scheduler": payload["scheduler"],
        "result": "PASS",
        "limitations": "Time-bound health verification; not an uptime guarantee or customer outcome."
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", help="Optional JSON evidence output path")
    args = parser.parse_args()
    evidence = verify()
    if args.output:
        Path(args.output).write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    for key in ("result", "checked_at_utc", "http_status", "latency_ms", "service", "database", "scheduler"):
        print(f"{key.upper()}={evidence[key]}")
