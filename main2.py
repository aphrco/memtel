# p1
import asyncio
from telethon.sync import TelegramClient
from telethon.tl.functions.channels import InviteToChannelRequest
from telethon.tl.types import InputPeerChannel
from telethon.errors.rpcerrorlist import UserNotParticipantError, PeerFloodError


API_ID = 51180  # Replace with your API ID
API_HASH = '79af93e441a3a9f35045a82c52c6d2e9'  # Replace with your API HASH

# User ID or username of the user you want to add
user_to_add = "https://t.me/mahnazhasani67"  # Replace with the user ID or username

DESTINATION_CHAT_ID = 'https://t.me/+ujsVuuAje6ZjYTY0'

async def add_user_to_channel():
    async with TelegramClient('session_name', API_ID, API_HASH) as client:
        try:
            # Resolve the user by ID or username
            user_entity = await client.get_input_entity(user_to_add)

            # Invite the user to the channel
            result = await client(InviteToChannelRequest(
                channel=DESTINATION_CHAT_ID,
                users=[user_entity]
            ))

            if result:
                print(f"User with ID or username {user_to_add} added to the channel successfully.")
            else:
                print(f"Failed to add user with ID or username {user_to_add} to the channel.")
        except UserNotParticipantError:
            print(f"User with ID or username {user_to_add} is not a participant in the channel.")
        except PeerFloodError:
            print("Adding users too fast. Slow down to avoid rate limiting.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

if __name__ == '__main__':
    asyncio.run(add_user_to_channel())


    #p2



import time
from telethon.sync import TelegramClient
from telethon.tl import functions, types
from telethon.errors import FloodWaitError

# مشخص کردن مشخصات اتصال
api_id = '51180'
api_hash = '79af93e441a3a9f35045a82c52c6d2e9'
phone_number = '+989150050301'

# اتصال به تلگرام
client = TelegramClient(phone_number, api_id, api_hash)


async def main():
    await client.start()

    # پرسش از کاربر تعداد کاربران مورد نظر و مدت زمان وقفه
    num_users = int(input("تعداد کاربران مورد نظر: "))
    delay_seconds = int(input("مدت زمان وقفه (ثانیه): "))

    # خواندن لیست کاربران از فایل listusername.txt
    with open('listusername.txt', 'r') as file:
        usernames = file.read().splitlines()

    # ایجاد گروه جدید یا انتقال به گروه موجود
    target_group = await client.get_input_entity('https://t.me/lokhtone')

    # افزودن کاربران به گروه
    for username in usernames[:num_users]:
        try:
            user = await client.get_entity(username)
            await client(functions.channels.InviteToChannelRequest(target_group, [user]))

            # ثبت نام کاربر در فایل enteghal.txt
            with open('enteghal.txt', 'a') as enteghal_file:
                enteghal_file.write(f'{username}\n')

            # حذف کاربر از فایل listusername.txt
            usernames.remove(username)
            with open('listusername.txt', 'w') as file:
                file.write('\n'.join(usernames))

        except FloodWaitError as e:
            # اگر وقفه داده شود، منتظر بمانید و دوباره تلاش کنید
            print(f'باید منتظر {e.seconds} ثانیه باشید.')
            time.sleep(e.seconds + 1)
            continue
        except Exception as e:
            # اگر مشکلی رخ دهد، این کاربر را به فایل masdod.txt منتقل کنید
            with open('masdod.txt', 'a') as masdod_file:
                masdod_file.write(f'{username}\n')
            usernames.remove(username)
            with open('listusername.txt', 'w') as file:
                file.write('\n'.join(usernames))
            continue

        # وقفه برای اجرای بعدی
        time.sleep(delay_seconds)

    await client.disconnect()


if __name__ == '__main__':
    import asyncio

    asyncio.run(main())
