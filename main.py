###  App to exporting grades from 'uonetplus.vulcan.net.pl' by Cocolak
###  For more read README.txt

def get_keystore():
    from vulcan import Keystore
    with open("!_reg/keystore.json") as f: keystore = Keystore.load(f)
    return keystore

def get_account():
    from vulcan import Account
    with open("!_reg/account.json") as f: account = Account.load(f)
    return account

async def register():
    from vulcan import Keystore, Account
    import os

    if not os.path.exists("!_reg"):
        os.makedirs("!_reg")

    keystore = await Keystore.create(device_model="Grades Export")
    with open("!_reg/keystore.json", "w") as f: f.write(keystore.as_json)

    r = True
    while r == True:
        token = input("Token: ").strip()
        symbol = input("Symbol: ").strip()
        pin = input("PIN: ").strip()

        try: account = await Account.register(keystore, token, symbol, pin)
        except: 
            print("\nNieprawidłowe dane, spróbuj ponownie. \n")
            continue

        r = False
    
    with open("!_reg/account.json", "w") as f: f.write(account.as_json)

async def login():
    from vulcan import Vulcan

    try: client = Vulcan(keystore=get_keystore(), account=get_account())
    except:
        print("No 'keystore.json' or 'account.json' file in the '!_reg' folder.")
        r = True
        while r == True:
            choice = input("Do you want register? (y/n) ").strip().lower()
            if choice == "" or choice[0] == "y":
                await register()
                r = False
                client = Vulcan(keystore=get_keystore(), account=get_account())
            elif choice[0] == "n":
                exit()
            else:
                continue
    
    return client

### Mode 'less' - exporting only the most important data
async def less():
    import pandas as pd
    import os

    client = await login()

    async with client:
        await client.select_student()
        
        grades = await client.data.get_grades()

        df = pd.DataFrame(columns=["date_created", 
                               "content", 
                               "value", 
                               "subject_code"])
        
        async for g in grades:
            df.loc[len(df.index)] = [g.date_created,            # date created
                                     g.content,                 # full grade e.g. 4+, 5-
                                     g.value,                   # grade value (float) e.g. 4.0, 5.0
                                     g.column.subject.code]     # short subject name e.g. pr.SK, wf, j. polski
        
        if not os.path.exists("!_data"):
            os.makedirs("!_data")

        df.to_csv("!_data/vulcan_grades.csv", encoding='utf-8') 
        print("Plik został zapisany w folderze '!_data'.")
        import time
        time.sleep(3)

### Mode 'more' = exporting more data
async def more(): 
    import pandas as pd
    import os

    client = await login()

    async with client:
        await client.select_student()
        
        grades = await client.data.get_grades()
        
        df = pd.DataFrame(columns=["period", 
                               "date_created", 
                               "content", 
                               "value", 
                               "grade_desc", 
                               "category", 
                               "subject", 
                               "subject_code", 
                               "teacher_fullname"])
        
        async for g in grades:
            df.loc[len(df.index)] = [g.column.period.number,    # period.number
                                     g.date_created,            # date created
                                     g.content,                 # full grade e.g. 4+, 5-
                                     g.value,                   # grade value (float) e.g. 4.0, 5.0
                                     g.column.name,             # grade description
                                     g.column.category.name,    # category e.g. Sprawdzian, Kartkówka
                                     g.column.subject.name,     # full subject name
                                     g.column.subject.code,     # short subject name e.g. pr.SK, wf, j. polski
                                     g.teacher_created.name + " " + g.teacher_created.surname]  # full teacher name (name + surname)
        
        if not os.path.exists("!_data"):
            os.makedirs("!_data")

        df.to_csv("!_data/vulcan_grades.csv", encoding='utf-8')
        print("Plik został zapisany w folderze '!_data'.")
        import time
        time.sleep(3)  

def info():
    print("""Tryb 'less' eksportuje:
    - datę stworzenia oceny,
    - pełną ocenę np. 4+, 5-,
    - wartość oceny (float) np. 4.0, 5.0,
    - skróconą nazwę przedmiotu.
    """)

    print("""Tryb 'more' eksportuje: 
    - numer semestru,
    - datę stworzenia oceny,
    - pełną ocenę np. 4+, 5-,
    - wartość oceny (float) np. 4.0, 5.0,
    - opis oceny,
    - kategorię np. Sprawdzian, Kartkówka,
    - pełną nazwę przedmiotu,
    - skróconą nazwę przedmiotu,
    - pełną nazwę nauczyciela (imię + nazwisko).
    """)

    input("Naciśnij dowolny klawisz, aby kontynuować...")

def blocking_function():
    print("Eksportowanie...")

async def run(m):
    import asyncio
    from concurrent.futures import ThreadPoolExecutor

    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()

    # Running the blocking function in a separate thread, allows you to start exporting "less" or "more", because consolemenu is like infinite loop and blocks thread.
    await loop.run_in_executor(executor, blocking_function)

    if m == "l": await less()
    elif m == "m": await more()

if __name__ == "__main__":
    import asyncio
    from consolemenu import ConsoleMenu
    from consolemenu.items import MenuItem, FunctionItem, ExitItem

    menu = ConsoleMenu("VULCAN GRADES IMPORT")
    menu_item = MenuItem("Menu Item")

    item_less = FunctionItem("less - tylko najważniejsze dane", function=lambda: asyncio.run(run("l")))
    item_more = FunctionItem("more - więcej danych", function=lambda: asyncio.run(run("m")))
    item_info = FunctionItem("info o imporcie", function=info)
    item_exit = ExitItem("wyjście")

    menu.append_item(item_less)
    menu.append_item(item_more)
    menu.append_item(item_info)
    menu.append_item(item_exit)
    menu.exit_item = item_exit

    menu.show()