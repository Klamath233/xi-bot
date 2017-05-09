import discord
import json
import asyncio

with open('alias.json', 'r') as alias_file:
    alias_dict = json.load(alias_file)
    
print(alias_dict)

async def exec_set_alias(client, channel, name, discriminator, alias):
    key = name + '#' + discriminator
    available_keys = [x.__str__() for x in client.get_all_members()]

    if key not in available_keys:
        await client.send_message(channel, 'Invalid member.')
        return

    # Set name:alias pair in in-memory storage.
    alias_dict[key] = alias;
    await client.send_message(channel, 'Success.')

    # Write it to FS stroage.
    with open('alias.json', 'w') as alias_file:
        json.dump(alias_dict, alias_file)


def get_alias(name, discriminator):
    concated_name = name + '#' + discriminator
    if concated_name in alias_dict:
        return alias_dict[concated_name]
    else:
        return name