# Auto Attack
Meant to automate:
- skill rotation
- mana / hp
- ssa / might ring swap

Requiring you literally to only walk and wait until everything is dead.

# Installing
Make sure you have these installed before:
- git
- python 3.10.11 or higher

```
> git clone https://github.com/rafael-adcp/auto-attack.git
> cd auto-attack
> make install
```

# Client setup example
TODO:: add a screenshot here

# Configuration
Bot relies on `.json` files for configurations
- **general_config.json**: contains the general configuration for the bot, class agnostic things
- per class configuration file (so the bot knows which key to press for a given skill):
    - **rp_hotkey.json**: **royal paladin** hotkey bindings 
    - **ek_hotkey.json**: **elite knight** hotkey bindings
    - **ms_hotkey.json**: **master sorcerer** hotkey bindings

# Running
```
> make run
```
- Wait until bot is done fetching position of things (Step 1)
- Press **"f"** so the bot **starts** (Step 2)
- Enjoy
- When desired, one can:
    - press **"f"** to **pause / resume** the bot (this wont stop life / mana healing though)
    - press **"delete"** to **completely stop** the bot

TODO:: add a screenshot here
