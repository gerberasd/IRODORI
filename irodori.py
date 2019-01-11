import discord #おまじない

client = discord.Client() #おまじない

#            ___ ____   ___  ____   ___  ____  ___ 
#           |_ _|  _ \ / _ \|  _ \ / _ \|  _ \|_ _|
#            | || |_) | | | | | | | | | | |_) || | 
#            | ||  _ <| |_| | |_| | |_| |  _ < | | 
#           |___|_| \_\\___/|____/ \___/|_| \_\___|
#           Ver.0.0.1
#           

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('    _/_/_/  _/_/_/      _/_/    _/_/_/      _/_/    _/_/_/    _/_/_/   ')
    print('     _/    _/    _/  _/    _/  _/    _/  _/    _/  _/    _/    _/      ')
    print('    _/    _/_/_/    _/    _/  _/    _/  _/    _/  _/_/_/      _/       ')
    print('   _/    _/    _/  _/    _/  _/    _/  _/    _/  _/    _/    _/        ')
    print('_/_/_/  _/    _/    _/_/    _/_/_/      _/_/    _/    _/  _/_/_/       ')
    print('Ver.0.0.1')
    print('------')
    # 起動確認

@client.event
async def on_message(message):
    # 「!test」で始まる場合
    if message.content.startswith("!test2"):
        m = "HelloWorld!"
        # メッセージが送られてきたチャンネルへHelloWorld!と送信
        await client.send_message(message.channel, m)

client.run("トークン") #トークンを貼り付けて下さい
