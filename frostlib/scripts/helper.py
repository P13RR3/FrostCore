import time
import __init__
import basescript
import random
maxdelay = 0.25
script = []

a = __init__.molten_core.boss_baron_geddon()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_garr()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_lucifron()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_magmadar()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_gehennas()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_golemagg()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_shazzrah()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_sulfuron_harbringer()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.mob_sulfuron_harbringer()
script.append(a)
time.sleep(0.01)
a = __init__.molten_core.boss_majordomo_executus()
script.append(a)
time.sleep(0.01)
a = __init__.zulgurub.boss_hakkar()
script.append(a)
time.sleep(0.01)
a = __init__.zulgurub.boss_arlokk()
script.append(a)
time.sleep(0.01)
a = __init__.zulgurub.boss_gahzranka()
script.append(a)
time.sleep(0.01)
a = __init__.zulgurub.boss_grilek()
script.append(a)
time.sleep(0.01)



random.shuffle(script)
while True:
    a_time = time.time()
    for x in script:
        try:
            x.update()
            
                        
        except:
            x.update()
            for i in range(20):
                print "ERROR in " + str(x)
            script.remove(x)
    b_time = time.time()
    print ">>>> " + str(b_time - a_time)
    time_diff = b_time - a_time
    if time_diff <= maxdelay:
        time.sleep(maxdelay - time_diff)
    


