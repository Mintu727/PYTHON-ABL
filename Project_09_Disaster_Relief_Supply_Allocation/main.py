# Project 09: Disaster Relief Supply Allocation
areas = [("North Zone",80,2),("Coastal Zone",100,1),("Hill Zone",60,3),("River Zone",70,1)]
available_stock = 220
for i in range(len(areas)):
    best = i
    for j in range(i+1,len(areas)):
        if areas[j][2] < areas[best][2]: best = j
    areas[i],areas[best] = areas[best],areas[i]
remaining = available_stock; total_allocated = 0
print("DISASTER RELIEF ALLOCATION\nArea | Demand | Priority | Allocated | Shortage")
for name,demand,urgency in areas:
    allocation = demand if remaining >= demand else remaining
    remaining -= allocation; shortage = demand-allocation; total_allocated += allocation
    print(name,"|",demand,"|",urgency,"|",allocation,"|",shortage)
print("\nAvailable stock:",available_stock,"Total allocated:",total_allocated,"Remaining stock:",remaining)