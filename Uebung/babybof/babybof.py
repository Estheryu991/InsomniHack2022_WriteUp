from pwn import * 
import time 

pin = ""
while len(pin) < 8:
    max_time = 0 
    max_digit = 0 
    for i in range(10):
        p = process("./pin_checker")
        start = time.time()
        p.sendline(pin + str(i) + "0" * (7 - len(pin)))
        p.readall()
        duration = time.time() - start
        if duration > max_time: 
            max_time = duration
            max_digit = i 
    pin += str(max_digit)
    print(pin)

# File "solve.py", line 9, in <module>
#     p = process("./pin_checker")
#   File "/home/esthi/.local/lib/python3.8/site-packages/pwnlib/tubes/process.py", line 258, in __init__
#     executable_val, argv_val, env_val = self._validate(cwd, executable, argv, env)
#   File "/home/esthi/.local/lib/python3.8/site-packages/pwnlib/tubes/process.py", line 568, in _validate
#     self.error("%r does not exist"  % executable)
#   File "/home/esthi/.local/lib/python3.8/site-packages/pwnlib/log.py", line 424, in error
#     raise PwnlibException(message % args)
# pwnlib.exception.PwnlibException: './pin_checker' does not exist
