# TAGLINE

动态链接器/加载器

# TLDR

**指定库路径运行**

```LD_LIBRARY_PATH=[/path/to/libs] [program]```

**预加载库**

```LD_PRELOAD=[/path/to/lib.so] [program]```

**调试加载过程**

```LD_DEBUG=libs [program]```

**显示搜索路径**

```ldconfig -p```

**更新库缓存**

```sudo ldconfig```

# SYNOPSIS

**ld.so** / **ld-linux.so** 是动态链接器

# PARAMETERS

**LD_LIBRARY_PATH**
> 额外的库目录。

**LD_PRELOAD**
> 优先加载的库。

**LD_DEBUG**
> 调试选项（libs、reloc、files）。

**LD_TRACE_LOADED_OBJECTS**
> 列出依赖（类似 ldd）。

# DESCRIPTION

**ld.so** 是动态链接器/加载器。它在运行时加载程序所需的共享库。

加载器负责解析符号并处理库依赖。其行为由环境变量控制。

# CAVEATS

通常不会被直接调用。LD_PRELOAD 存在安全风险。对 setuid 二进制文件会被忽略。

# HISTORY

ld.so 是 **glibc** 软件包的一部分，为 Linux 可执行文件实现动态链接。

# INSTALL

```apt: sudo apt install libc-bin```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ldd](/man/ldd)(1), [ldconfig](/man/ldconfig)(8), [ld](/man/ld)(1)
