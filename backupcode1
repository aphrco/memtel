import asyncio
from telethon.sync import TelegramClient
from telethon.tl import functions
from telethon.errors import FloodWaitError

 # api
api_id = 20741991
api_hash = '0cee2a8cecc6474b3827b82de03f5b8e'
phone_number = '+62 831 32344256'

client = TelegramClient(phone_number, api_id, api_hash)


async def main():
    await client.start()

    # input user total and time delay
    num_users = int(input("usere total add: "))
    delay_seconds = int(input("Input delay(s): "))
    target_group = await client.get_input_entity('https://t.me/+TW7h6AvzsIY4Y2I0')

    # list karbaran az  listusername.txt
    with open('listusername.txt', 'r') as file:
        usernames = file.read().splitlines()

     # add user
    for username in usernames[:num_users]:
        try:
            print(username)
            # delay
            user = await client.get_entity(username)
            await client(functions.channels.InviteToChannelRequest(target_group, [user]))
            # move enteghal.txt
            with open('enteghal.txt', 'a') as enteghal_file:
                enteghal_file.write(f'{username}\n')
                print("enteghal")

            # delete user  listusername.txt
            usernames.remove(username)
            with open('listusername.txt', 'w') as file:
                file.write('\n'.join(usernames))
                print("hazf")
            print(username)

        except FloodWaitError as e:
            print(f'you can wate {e.seconds} for run.')
            await asyncio.sleep(e.seconds + 1)
            continue
        except Exception as e:
            with open('errors.txt', 'a') as errors_file:
                errors_file.write(f'{username}: {str(e)}\n')
                with open('masdod.txt', 'a') as masdod_file:
                    masdod_file.write(f'{username}\n')
                usernames.remove(username)
                with open('listusername.txt', 'w') as file:
                    file.write('\n'.join(usernames))
                continue
            continue

    await client.disconnect()

if __name__ == '__main__':
    asyncio.run(main())
