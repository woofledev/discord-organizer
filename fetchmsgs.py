# fetch all messages from a channel through the discord api
from config import message_fetcher
token, channelId, batch = message_fetcher.values()
print(f"will fetch {50 * batch} messages")


import json
import urllib.request as ur

out = []
def main(url = f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50", count=batch):
  if count == 0: return
  print(f"fetching: {url} (batches to go: {count})")
  req = ur.Request(url, headers={"Authorization": token, "User-Agent": "Mozilla 5.0"})
  try: 
    with ur.urlopen(req) as res:
      data = json.loads(res.read().decode())
      if data and len(data) > 0:
        out.append(data)
        return main(f"https://discord.com/api/v9/channels/{channelId}/messages?limit=50&before={data[-1]['id']}", count-1)
      else: return
  except Exception as e:
    print(f"ERROR: {e}")
    return

main()
open("msgs.json", "w").write(json.dumps(out))