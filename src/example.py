from brawl import Brawl
import sys
from dotenv import load_dotenv
import os
import json
import asyncio

if sys.platform == 'win32':
	asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
     

# Load environment variables from the .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")


brawl = Brawl(API_KEY)

async def main():
    player_tag = "#8R9Y0QVQC"
    club_tag = "#2UYQ8J0LP"
    
    player_data = await brawl.player(player_tag)
    club_data = await brawl.club(club_tag)
    events = await brawl.events()
    global_player_ranks = await brawl.player_rankings()
    NA_player_ranks = await brawl.player_rankings("NA", 0)
    brawlers = await brawl.brawlers()

    print(player_data.name)
    print(club_data.members[0].name)
    # print(global_player_ranks)
    # print(NA_player_ranks)
    print(brawlers)
    await brawl.close()

# Run the async function
asyncio.run(main())