# TAGLINE

通过系统调用设置进程执行域

# TLDR

**调试时禁用 ASLR（经由 setarch）**

```setarch $(uname -m) -R [command]```

**在 64 位系统上运行 32 位二进制**

```linux32 [command]```

**运行 64 位二进制**

```linux64 [command]```

**设置旧式内存布局**

```setarch $(uname -m) -L [command]```

# SYNOPSIS

```c
#include <sys/personality.h>

int personality(unsigned long persona);
```

# PARAMETERS

**PER_LINUX**
> 标准 Linux 执行域。

**PER_LINUX32**
> 64 位内核上的 32 位执行模式。

**ADDR_NO_RANDOMIZE**
> 禁用地址空间布局随机化（ASLR）。

**MMAP_PAGE_ZERO**
> 映射零页（供 SVr4 二进制程序使用）。

**ADDR_COMPAT_LAYOUT**
> 使用旧式虚拟内存布局。

**READ_IMPLIES_EXEC**
> 可读映射变为可执行（PROT_READ 隐含 PROT_EXEC）。

**ADDR_LIMIT_32BIT**
> 将地址空间限制为 32 位。

**STICKY_TIMEOUTS**
> 在 select(2) 中采用 SVr4 风格的超时处理。

# DESCRIPTION

**personality**(2) 是一个 Linux 系统调用，用于设置进程的执行域，指示内核模拟其他 UNIX 变体的行为或切换兼容性标志。它主要通过 **setarch**、**linux32** 和 **linux64** 等包装命令间接调用。

常见用例包括：调试时禁用 ASLR 以获得可复现的内存地址、在 64 位内核下运行旧的 32 位二进制程序，以及为兼容旧系统而模拟早期 UNIX 的内存布局。

# CAVEATS

仅限 Linux。没有独立的 **personality** 命令行工具；请使用 **setarch**(8) 或其别名。禁用 ASLR 之类的安全特性会降低系统安全性，应仅限于调试场景使用。

# HISTORY

personality(2) 系统调用起源于早期的 Linux 1.2/2.x，目的是支持与 SCO、SVr4、Solaris 等 UNIX 系统的二进制兼容，那些系统的二进制程序当时可经 iBCS2 在 Linux 上运行。

# SEE ALSO

[setarch](/man/setarch)(8), [linux32](/man/linux32)(8), [linux64](/man/linux64)(8)
