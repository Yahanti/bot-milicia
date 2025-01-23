import discord
import asyncio

# Configuração do client com permissões adequadas
intents = discord.Intents.default()
intents.message_content = True  # Permissão para acessar o conteúdo das mensagens
client = discord.Client(intents=intents)

# Função para atualizar a hierarquia (mensagem) a cada 1 hora
async def update_hierarchy():
    await client.wait_until_ready()
    while not client.is_closed():
        # Substitua pelo ID do canal onde a mensagem será atualizada
        channel = client.get_channel(1322481080476897280)  # Substitua pelo ID do canal
        if channel:
            # Enviando a mensagem atualizada ou substituindo uma mensagem existente
            await channel.send("Esta mensagem está sendo atualizada a cada 1 hora.")
        
        # Espera por 1 hora (3600 segundos)
        await asyncio.sleep(3600)

# Evento chamado quando o bot se conecta ao Discord
@client.event
async def on_ready():
    print(f'Bot {client.user} está conectado ao Discord!')
    # Inicia a tarefa de atualização de hierarquia (mensagem)
    client.loop.create_task(update_hierarchy())

# Substitua pelo seu token do bot
client.run('MTMzMTc4MDgzNDkzOTc2NDgxNw.GXAFEq.9U_WV2_VY9RGN8ZP3A5bBcLKbyXrscm9ch9a_I')
