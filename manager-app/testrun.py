import vulcan_chandle as vc
import asyncio

try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    loop = None

if loop  and loop.is_running():
    tsk = loop.create_task(vc.login())

else:
    result = asyncio.run(vc.login())



##asyncio.run(vc.login())
