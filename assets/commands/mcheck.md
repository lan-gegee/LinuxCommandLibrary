# TAGLINE

malloc 的堆一致性检查

# TLDR

**在 C 程序中启用堆检查**（在任何 malloc 之前调用）

```mcheck(NULL)```

**使用自定义错误处理器启用堆检查**

```mcheck([handler_func])```

**对每次分配都启用严格检查**

```mcheck_pedantic(NULL)```

**立即检查所有已分配块**

```mcheck_check_all()```

**显式检查指定的已分配块**

```mprobe([ptr])```

**链接 mcheck 以启用自动检查**

```cc [program.c] -lmcheck```

# SYNOPSIS

```c
#include <mcheck.h>

int mcheck(void (*abortfunc)(enum mcheck_status mstatus));
int mcheck_pedantic(void (*abortfunc)(enum mcheck_status mstatus));
void mcheck_check_all(void);
enum mcheck_status mprobe(void *ptr);
```

# PARAMETERS

**mcheck** _abortfunc_
> 为 malloc 安装调试钩子。传入 NULL 则使用默认处理器，它会打印消息并调用 abort()。必须在第一次 malloc() 之前调用。

**mcheck_pedantic** _abortfunc_
> 类似 mcheck()，但每次调用 malloc()、realloc() 或 free() 时都会对所有已分配块执行一致性检查。非常慢。

**mcheck_check_all**
> 触发对所有已分配块的即时一致性检查。仅在先调用过 mcheck() 时才有效。

**mprobe** _ptr_
> 显式检查 ptr 所指向的块的一致性。

# DESCRIPTION

**mcheck** 系列函数为 glibc 中的 **malloc**(3) 内存分配函数安装调试钩子。这些钩子会对堆执行一致性检查，检测常见错误，例如双重释放、破坏 malloc 记账数据的缓冲区越界以及使用已释放内存。

**mcheck()** 必须在第一次调用 malloc() 之前调用。将程序与 **-lmcheck** 链接会在首次分配前插入隐式的 mcheck(NULL) 调用，比修改源代码更方便。

**mprobe()** 函数返回一个指示块状态的状态值：**MCHECK_OK**（无不一致）、**MCHECK_HEAD**（块之前的内存被破坏）、**MCHECK_TAIL**（块之后的内存被破坏）或 **MCHECK_FREE**（块被释放了两次）。

# CAVEATS

**mcheck()** 必须在任何内存分配之前调用，否则返回 -1。这些函数是 glibc 特有的，不可移植。**MALLOC_CHECK_** 环境变量无需重新编译即可提供类似功能。**mcheck_pedantic()** 非常慢，只应用于针对性调试。在较新的 glibc 版本中已被弃用，推荐改用 **MALLOC_CHECK_** 和 valgrind 等工具。

# HISTORY

**mcheck** 函数是 **GNU C 库**（glibc）的一部分，源自早期 Unix 的 malloc 调试设施。它们在 glibc 手册的"Heap Consistency Checking"一节中有文档说明。

# INSTALL

```apt: sudo apt install mtools```

```dnf: sudo dnf install mtools```

```pacman: sudo pacman -S mtools```

```apk: sudo apk add mtools```

```zypper: sudo zypper install mtools```

```brew: brew install mtools```

```nix: nix profile install nixpkgs#mtools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[valgrind](/man/valgrind)(1)
