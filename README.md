# PyBrawl API Wrapper

A simple asynchronous Python wrapper for the Brawl Stars API using `aiohttp`.

## Features
- Fetch player information.
- Retrieve battle logs.
- Get club details.
- View current event rotations.
- Get rankings for players, clubs, and brawlers.
- Retrieve a list of brawlers or specific brawler details.

## Installation
Ensure you have Python 3.7+ installed. Install required dependencies using:

```sh
pip install aiohttp
```

## Usage
### Initialize the Wrapper
```python
import asyncio
from brawl import Brawl

TOKEN = "your_api_token_here"
brawl = Brawl(TOKEN)
```

### Fetch Player Information
```python
async def main():
    player = await brawl.player("PLAYER_TAG")
    print(player.name, player.trophies)
    await brawl.close()

asyncio.run(main())
```

### Retrieve Battle Log
```python
async def main():
    battle_log = await brawl.battle_log("PLAYER_TAG")
    print(battle_log)
    await brawl.close()

asyncio.run(main())
```

### Fetch Club Information
```python
async def main():
    club = await brawl.club("CLUB_TAG")
    print(club.name, club.members)
    await brawl.close()

asyncio.run(main())
```

### Retrieve Current Events
```python
async def main():
    events = await brawl.events()
    print(events)
    await brawl.close()

asyncio.run(main())
```

### Fetch Player Rankings
```python
async def main():
    rankings = await brawl.player_rankings(country_code="us", limit=10)
    print(rankings)
    await brawl.close()

asyncio.run(main())
```

### Fetch Brawler List or Details
```python
async def main():
    brawlers = await brawl.brawlers()
    print(brawlers)
    await brawl.close()

asyncio.run(main())
```

## Closing the Session
To properly close the session:
```python
await brawl.close()
```

## License
This project is licensed under the MIT License.
