import io
import discord
from discord.ext import commands
from discord_slash import cog_ext, SlashContext
from discord_slash.model import SlashCommandOptionType as OptionType

import elevenlabs

elevenlabs.set_api_key("bf0d9ebd4bd32f75006b23ead429d61c")

CHOICES = [
    discord.OptionChoice(name=voice.name, value=voice.voice_id) for voice in elevenlabs.voices()
    if voice.category != "premade"
][:25]

class Elevenlabs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @cog_ext.cog_slash(  # Use cog_ext.cog_slash for the decorator
        name="voice",
        description="Generate voice from text",
        options=[
            commands.Option(name="text", description="Text to convert to voice", type=3, required=True),
            commands.Option(name="voice", description="Voice selection", type=3, choices=CHOICES, required=True),
        ],
    )
    async def voice(self, ctx: SlashContext, text: str, voice: str):
        await ctx.defer()

        output = elevenlabs.generate(
            text=text,
            voice=elevenlabs.Voice(
                voice_id=voice,
                settings=elevenlabs.VoiceSettings(
                    stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True
                ),
            ),
            model="eleven_multilingual_v2",
        )

        await ctx.send(
            file=discord.File(io.BytesIO(output), filename="voice.mp3"),
            content=f"Generated voice for: {text}",
        )

def setup(bot):
    bot.add_cog(Elevenlabs(bot))
