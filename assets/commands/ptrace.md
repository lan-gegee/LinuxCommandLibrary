# TAGLINE

用于进程跟踪与调试的系统调用

# TLDR

**跟踪系统调用**（通过 strace）

```strace [command]```

**附加到进程**

```strace -p [pid]```

**跟踪子进程**

```strace -f [command]```

**跟踪特定调用**

```strace -e [open,read,write] [command]```

# SYNOPSIS

**ptrace**(_request_, _pid_, _addr_, _data_)

# DESCRIPTION

**ptrace**（process trace）是一个 Linux 系统调用，允许一个进程（tracer）观察并控制另一个进程（tracee）的执行。它可以检查和修改 tracee 的内存、寄存器和信号传递。它是 **gdb** 等调试器以及 **strace** 和 **ltrace** 等系统调用跟踪工具所依赖的底层机制。tracee 必须调用 PTRACE_TRACEME 或通过 PTRACE_ATTACH/PTRACE_SEIZE 被附加。

# REQUESTS

```c
PTRACE_TRACEME    - Allow parent to trace this process
PTRACE_ATTACH     - Attach to a running process
PTRACE_SEIZE      - Attach without stopping the process
PTRACE_DETACH     - Detach from traced process
PTRACE_PEEKTEXT   - Read a word from text/code memory
PTRACE_PEEKDATA   - Read a word from data memory
PTRACE_POKETEXT   - Write a word to text/code memory
PTRACE_POKEDATA   - Write a word to data memory
PTRACE_GETREGS    - Get general-purpose registers
PTRACE_SETREGS    - Set general-purpose registers
PTRACE_CONT       - Continue execution
PTRACE_SINGLESTEP - Execute a single instruction then stop
PTRACE_SYSCALL    - Continue and stop at next syscall entry/exit
```

# EXAMPLE (C)

```c
#include <sys/ptrace.h>

// In child:
ptrace(PTRACE_TRACEME, 0, NULL, NULL);

// In parent:
ptrace(PTRACE_ATTACH, child_pid, NULL, NULL);
ptrace(PTRACE_CONT, child_pid, NULL, NULL);
```

# SECURITY

```bash
# Check ptrace scope
cat /proc/sys/kernel/yama/ptrace_scope

# Values:
# 0 - Classic ptrace permissions
# 1 - Restricted to descendants
# 2 - Admin only
# 3 - No ptrace allowed
```

# CAVEATS

Linux 专有系统调用（其他 Unix 系统有类似但不兼容的实现）。安全限制由 YAMA LSM 模块强制执行（/proc/sys/kernel/yama/ptrace_scope）。跟踪非子进程需要 CAP_SYS_PTRACE 或 root 权限。一个进程同一时间只能被一个 tracer 附加。反调试技术可通过检测 PTRACE_TRACEME 返回错误来发现 ptrace。

# HISTORY

ptrace 起源于 **Unix V7**（1979 年），并在 **Linux** 上为调试和跟踪目的得到大幅扩展。

# SEE ALSO

[strace](/man/strace)(1), [ltrace](/man/ltrace)(1), [gdb](/man/gdb)(1)
