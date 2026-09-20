from json import loads
from urllib.request import urlopen

URL = "https://api.opschugex.com/health"

with urlopen(URL, timeout=15) as response:
    assert response.status == 200, f"Unexpected HTTP status: {response.status}"
    payload = loads(response.read().decode("utf-8"))

assert payload.get("status") == "healthy", payload
assert payload.get("service") == "opschugex-api", payload
assert payload.get("database") == "connected", payload
assert payload.get("scheduler") == "running", payload

print("LIVE_API_EVIDENCE=PASS")
print("SERVICE=opschugex-api")
print("DATABASE=connected")
print("SCHEDULER=running")