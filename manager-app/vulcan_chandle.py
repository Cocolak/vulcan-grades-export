def get_keystore(path = "!_reg/Keystore.json"):
    from vulcan import Keystore
    with open(path) as f: keystore = Keystore.load(f)
    return keystore

def get_account(path = "!_reg/Account.json"):
    from vulcan import Account
    with open(path) as f: account = Account.load(f)
    return account

async def register(token, symbol, pin):
    from vulcan import Keystore, Account
    import os

    if not os.path.exists("!_reg"):
        os.makedirs("!_reg")
    
    keystore = await Keystore.create(device_model="Vulcan Manager")
    with open("!_reg/Keystore.json", "w") as f: f.write(keystore.as_json)
    
    try: account = await Account.register(keystore, token, symbol, pin)
    except: return False
    
    with open("!_reg/Account.json", "w") as f: f.write(account.as_json)

    return True

async def login(Keystore_path = "!_reg/Keystore.json", Account_path = "!_reg/Account.json"):
    from vulcan import Vulcan

    try: client = Vulcan(keystore=get_keystore(Keystore_path), account=get_account(Account_path))
    except:
        ## TODO Sprawdź czy można rozpoznać jaka jest przyczyna błędu w logowaniu
        return False, None

    return True, client


