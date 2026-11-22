
from pathlib import Path
import requests

webhook_url = Path(__file__).with_name(
    "discord_webhook.txt"
).read_text().strip()

message = "TEST: My Python UXI monitor is connected!"

response = requests.post(
    webhook_url,
    json={"content": message},
    timeout=10
)

print("Status code:", response.status_code)
response.raise_for_status()
