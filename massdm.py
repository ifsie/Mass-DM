import discord, colorama, os, requests, time
from colorama import Style, Fore

re = Style.RESET_ALL
r = Fore.RED
g = Fore.GREEN

os.system(f'cls & mode 120,35 & title Fuck Skids, Mass DM [Not Connected]')

heylol = (f'''

              {r}$$$$$${re}\                      {r}$${re}\                       {r}$${re}\       {r}$${re}\       {r}$${re}\           
             {r}$${re}  __{r}$${re}\                     {r}$${re} |                      {r}$${re} |      \__|      {r}$${re} |          
             {r}$${re} /  \__|{r}$${re}\   {r}$$\  {r}$$$$$$${re}\ {r}$${re} |  {r}$${re}\        {r}$$$$$$${re}\ {r}$${re} |  {r}$${re}\ {r}$${re}\  {r}$$$$$$${re} | {r}$$$$$$${re}\ 
             {r}$$$${re}\     {r}$${re} |  {r}$$ |{r}$${re}  _____|{r}$${re} | {r}$${re}  |      {r}$${re}  _____|{r}$${re} | {r}$${re}  |{r}$${re} |{r}$${re}  __{r}$${re} |{r}$${re}  _____|
             {r}$${re}  _|    {r}$${re} |  {r}$$ |{r}$${re} /      {r}$$$$$${re}  /       \{r}$$$$$${re}\  {r}$$$$$${re}  / {r}$${re} |{r}$${re} /  {r}$${re} |\{r}$$$$$${re}\  
             {r}$${re} |      {r}$${re} |  {r}$$ |{r}$${re} |      {r}$${re}  _{r}$${re}<         \____{r}$${re}\ {r}$${re}  _{r}$${re}<  {r}$${re} |{r}$${re} |  {r}$${re} | \____{r}$${re}\ 
             {r}$${re} |      \{r}$$$$$${re}  |\{r}$$$$$$${re}\ {r}$${re} | \{r}$${re}\       {r}$$$$$$${re}  |{r}$${re} | \{r}$${re}\ {r}$${re} |\{r}$$$$$$${re} |{r}$$$$$$${re}  |
             \__|       \______/  \_______|\__|  \__|      \_______/ \__|  \__|\__| \_______|\_______/ by ifs

''')                                                                                      
print(f'{heylol}                                             Status [{r}Not Connected{re}]')  

token = input(f'  ~$token{r}:{re} ')

head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)

if src.status_code == 200:
    pass
else:
    print('  ~$error Token was invalid')
    time.sleep(5)
    quit()


os.system('cls')

print(f'{heylol}                                             Status [{g}Connected{re}]')
print('')
message = input(f'  ~$message{r}:{re} ')
print('')
client = discord.Client()

@client.event
async def on_connect():
    times = 0
    for user in client.user.friends:
        try:
            await user.send(message)
            os.system(f'title Fuck Skids, Mass DM [Connected] [{user.id}] [{user.name}#{user.discriminator}]')
            print(f'  ~$sent Message was sent to [{r}{user.id}{re}] [{r}{user.name}{re}#{r}{user.discriminator}{re}]')
            times += 1
        except:
            print(f'  ~$error Message was failed to send to [{r}{user.id}{re}] [{r}{user.name}{re}#{r}{user.discriminator}{re}]')
    print(' ')
    print(f'  ~$success [{times}] Messages have been sent')
client.run(token, bot=False)