#################################################
# Procesamiento síncrono                        #
#################################################

def main():
    print(f"main -> Hola.......")
    print(f"main -> ......adiós")
    
print(f"Inicio Sync")
main()
print(f"Fin sync")
print()

#################################################
# Procesamiento asíncrono                       #
#################################################

import asyncio

async def main():
    print(f"async main -> Hola.......")
    await asyncio.gather(func1(), func2(), func3())
    print(f"async main -> ......adiós")
    
async def func1():
    print(f"async func1 -> Hola.......")
    await asyncio.sleep(5)
    print(f"async func1 -> ......adiós")
    
async def func2():
    print(f"async func2 -> Hola.......")
    for i in range(11):
        print (f"async func2 -> {i}")
        await asyncio.sleep(0.6)
    print(f"async func2 -> ......adiós")
    
async def func3():
    print(f"async func2 -> Hola.......")
    for i in range(11):
        print (f"async func3 -> {i}")
        await asyncio.sleep(0.2)
    print(f"async func2 -> ......adiós")

print(f"Inicio Sync")
asyncio.run(main()) #el hilo principal siempre es síncrono
print(f"Fin sync")
print()