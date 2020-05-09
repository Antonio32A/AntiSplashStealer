from .fakesplashes import FakeSplashes


def setup(bot):
    bot.add_cog(FakeSplashes(bot))
