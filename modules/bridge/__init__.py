from .bridge import Bridge


def setup(bot):
    bot.add_cog(Bridge(bot))
