# TAGLINE

用于二进制漏洞利用的 Python 库

# TLDR

**以 pwntools 启动 Python**

```python -c "from pwn import *"```

**创建 pwntools 脚本**

```pwn template [binary] --host [host] --port [port]```

**检查二进制安全性**

```checksec [binary]```

**反汇编 shellcode**

```disasm [hexstring]```

# SYNOPSIS

**pwntools** Python library for exploit development

# DESCRIPTION

**pwntools** 是一个面向 Python 的 CTF 框架和漏洞利用开发库。它提供二进制漏洞利用、shellcode 生成和远程连接等实用功能。

# EXAMPLES

```python
from pwn import *

# Connect to remote
r = remote('host', 1337)

# Start local binary
p = process('./binary')

# Read/write
r.recvline()
r.sendline(b'payload')

# Pack integers
payload = p32(0xdeadbeef)  # 32-bit
payload = p64(0x41414141)  # 64-bit

# Create shellcode
shellcode = asm(shellcraft.sh())

# ROP chain
rop = ROP('./binary')
rop.call('system', ['/bin/sh'])
```

# CLI TOOLS

```bash
# Check binary protections
checksec ./binary

# Create exploit template
pwn template ./binary > exploit.py

# Assemble shellcode
pwn asm 'mov eax, 1; int 0x80'

# Disassemble
pwn disasm '6a68682f2f2f73'

# Cyclic pattern
pwn cyclic 100
pwn cyclic -l 0x61616164
```

# CAVEATS

Python 库（pip install pwntools）。需要理解漏洞利用知识。仅用于 CTF 和经授权的测试。

# HISTORY

pwntools 由 **Gallopsled** CTF 战队创建，已成为 CTF 漏洞利用开发的标准 Python 库。

# INSTALL

```brew: brew install pwntools```

```nix: nix profile install nixpkgs#pwntools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwn](/man/pwn)(1), [checksec](/man/checksec)(1), [gdb](/man/gdb)(1), [radare2](/man/radare2)(1), [ropper](/man/ropper)(1)
