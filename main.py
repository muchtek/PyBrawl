import aiohttp
import asyncio
import sys
import json
from types import SimpleNamespace

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
     
API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjEzZDlkZjZhLWNkNDItNDlhZi1hZDAyLTNhM2Q0OWEwM2Y5MSIsImlhdCI6MTc0MDg4MTU5OCwic3ViIjoiZGV2ZWxvcGVyLzFlZDBjODNhLTg2NTYtZWFlZC03ZjhjLTc2Y2RjNWI0YWJjZCIsInNjb3BlcyI6WyJicmF3bHN0YXJzIl0sImxpbWl0cyI6W3sidGllciI6ImRldmVsb3Blci9zaWx2ZXIiLCJ0eXBlIjoidGhyb3R0bGluZyJ9LHsiY2lkcnMiOlsiNzUuNzAuNC45NCJdLCJ0eXBlIjoiY2xpZW50In1dfQ.8u0q3JjhR1duwVuS3FKYVPRJhqgMI1pNdOxhxiYuphpTQiSvWd02rxqBEJ5bCn7-P6z-o1QATWj5XPsZ5g7NAA"


class Brawl:
    BASE_URL = "https://api.brawlstars.com/v1"

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.session = None

    # -- Confirm Session is Active --
    async def __ensure_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(headers=self.headers)

    async def player(self, player_tag: str):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/players/%23{player_tag.strip('#')}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                player = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return player
            else:
                print(f"Error: {response.status}")
                return await response.text()
    
    async def club(self, club_tag: str):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/clubs/%23{club_tag.strip('#')}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                club = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return club
            else:
                print(f"Error: {response.status}")
                return await response.text()
    
    async def events(self):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/events/rotation"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                events = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return events
            else:
                print(f"Error: {response.status}")
                return await response.text()

    async def player_rankings(self, country_code: str = "global"):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/players"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()
    
    async def club_rankings(self, country_code: str = "global"):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/clubs"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()
            
    async def brawler_rankings(self, brawler_id: str, country_code: str = "global"):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/brawlers/{brawler_id}"  # Format player tag correctly

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()
            

    async def close(self):
        await self.session.close()




brawl = Brawl(API_KEY)

async def main():
    player_tag = "#8R9Y0QVQC"
    club_tag = "#2UYQ8J0LP"
    
    player_data = await brawl.player(player_tag)
    club_data = await brawl.club(club_tag)
    events = await brawl.events()

    print(player_data.name)
    print(club_data.members[0].name)
    print(events)
    await brawl.close()

# Run the async function
asyncio.run(main())