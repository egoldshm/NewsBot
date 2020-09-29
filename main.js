const BOT_TOKEN = "1121484069:AAFxBW8E__DOTcQ8n0qIufiKg2s_kuhppIo"
const { Telegraf } = require('telegraf')
const Keyboard = require('telegraf-keyboard');


const bot = new Telegraf(BOT_TOKEN)
bot.start((ctx) => 
{
ctx.reply('Welcome!');
})
bot.on('text', (ctx) => 
{
    const keyboad = new Keyboard()
    console.log(ctx.update)
    if(ctx.update.message.text == SEND_THE_LAST_NEWS)
    {
        ctx.replyWithAudio("./audio.mp3").catch((reason) => console.log("ERROR:" + reason));
    }
    else
    {
        ctx.reply(NOT_FOUND_MESSAGE,keyboad.add(SEND_THE_LAST_NEWS).draw())
    }
}
)
bot.launch()
