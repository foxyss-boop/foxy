from redbot.core.bot import Red
from .marttools import MartTools

__red_end_user_data_statement__ = (
    "This cog does not persistently store data or metadata about users."
)


def setup(bot: Red):
    cog = MartTools(bot)
    bot.add_cog(cog)
