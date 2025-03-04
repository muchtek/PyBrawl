import aiohttp
import asyncio
import sys
import json
from types import SimpleNamespace

class Brawl:
    BASE_URL = "https://api.brawlstars.com/v1"

    def __init__(self, token: str):
        self.token = token
        self.headers = {"Authorization": f"Bearer {self.token}"}
        self.session = None


    # -- Ensure Session is Active --
    async def __ensure_session(self):
        if self.session is None or self.session.closed:
            self.session = aiohttp.ClientSession(headers=self.headers)


    # -- Get Information Regarding a Player --
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

       
    # -- Get Information Regarding a Player's Recent Battles --
    async def battle_log(self, player_tag: str):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/players/%23{player_tag.strip('#')}/battlelog"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                player = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return player
            else:
                print(f"Error: {response.status}")
                return await response.text()


    # -- Get Information Regarding a Club --
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


    # -- Get Information Regarding Current Rotating Events --
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


    # -- Get Player Rankings --
    async def player_rankings(self, country_code: str = "global", limit: int = None):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/players"

        if(limit):
            url += f"?limit={limit}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()


    # -- Get Club Rankings --
    async def club_rankings(self, country_code: str = "global", limit: int = None):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/clubs"

        if(limit):
            url += f"?limit={limit}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()


    # -- Get Brawler Rankings --
    async def brawler_rankings(self, brawler_id: str, country_code: str = "global", limit: int = None):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/rankings/{country_code}/brawlers/{brawler_id}"  # Format player tag correctly

        if(limit):
            url += f"?limit={limit}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()


    # -- Get Brawlers as a List or Individuals --
    async def brawlers(self, brawler_id: str = None, limit: int = None):
        await self.__ensure_session()

        url = f"{self.BASE_URL}/brawlers"

        if(brawler_id):
            url = f"{self.BASE_URL}/brawlers/{brawler_id}"

        if(limit):
            url += f"?limit={limit}"

        async with self.session.get(url, headers=self.headers) as response:
            if response.status == 200:
                data = await response.json()
                ranks = json.loads(json.dumps(data), object_hook=lambda d: SimpleNamespace(**d))
                return ranks
            else:
                print(f"Error: {response.status}")
                return await response.text()
            

    # -- Close the Session --
    async def close(self):
        await self.session.close()
