const = require("discord.js")
const = require("configuration/...config.json")

const => content(if message.content === 'unmute'{
  new => embed = ({
    .setTitle("Unmuted")
    .setAuthor(name="Successfully Unmuted", icon="images/author.png")
    .setDescription("{user.Mentioned()} Was Unmuted")
    .setFooter("Unmuted • If it was a mistake do /mute again")
    .removeRole("Muted", "muted", if usermentioned==is(true).remove)
    });
    self.remove(role==='Muted', 'muted')
      {
        system.remove.role()
        await update()
      };
    if user == unmuted = by(time):
    await message.say("Unmuted Because The Time Ran Out")
    else {
      if user == unmuted = by(author):
      await message.say("Unmuted by {format.author.mention()}")
      };
});
