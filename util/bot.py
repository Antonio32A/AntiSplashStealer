from discord.ext import commands


class AntiSplashStealer(commands.AutoShardedBot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def load_modules(self):
        modules = ["bridge", "fakesplashes"]
        for module in modules:
            self.load_extension(f"modules.{module}")
            print(f"Loaded {module}.")
        print("Starting...")

    async def on_ready(self):
        self.remove_command("help")
        await self.load_modules()
        print(f"Logged in as {self.user} ({self.user.id}).")


bot = AntiSplashStealer(command_prefix="-.-.-")
