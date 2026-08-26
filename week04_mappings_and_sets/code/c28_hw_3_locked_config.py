##que 3 : Ek config dict banao, use MappingProxyType se lock karo, padhne ki koshish (chalega) aur badalne ki koshish (error padho).

from types import MappingProxyType

config = {"microsoft":"64 LPA","google":"54 LPA"}
locked = MappingProxyType(config)

print(locked)
locked["google"] = "59 LPA"