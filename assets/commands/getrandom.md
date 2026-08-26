# TAGLINE

内核随机数生成器接口

# TLDR

**获取随机字节（shell）**

```head -c [16] /dev/urandom | xxd```

**获取随机字节（C 函数）**

```getrandom(buffer, length, flags)```

# SYNOPSIS

**#include <sys/random.h>**

**ssize_t getrandom(void** \*_buf_, **size_t** _buflen_, **unsigned int** _flags_**);**

# PARAMETERS

_buf_
> 接收随机字节的缓冲区。

_buflen_
> 要读取的字节数。

_flags_
> GRND_RANDOM（使用 /dev/random）或 GRND_NONBLOCK。

# DESCRIPTION

**getrandom()** 是一个 Linux 系统调用，用内核随机数生成器产生的随机字节填充缓冲区。它是程序中获取随机数据的推荐接口。

与读取 /dev/urandom 不同，getrandom() 在系统启动早期会阻塞，直到熵池初始化完成，从而保证强随机性。

# FLAGS

```
0             - Default, blocks until entropy available
GRND_RANDOM   - Use /dev/random pool (may block)
GRND_NONBLOCK - Don't block, return error instead
```

# SHELL ALTERNATIVES

```bash
# Read random bytes
dd if=/dev/urandom bs=16 count=1

# Generate random hex
openssl rand -hex 16

# Generate random base64
openssl rand -base64 16
```

# CAVEATS

这是系统调用而非命令。自 Linux 3.17 起可用。在更旧的系统上请从 /dev/urandom 读取。系统启动早期可能阻塞。

# HISTORY

getrandom() 系统调用由 Theodore Ts'o 于 **2014 年**加入 Linux 内核 **3.17**，目的是解决熵池初始化之前 /dev/urandom 返回弱随机数据的问题。

# SEE ALSO

[random](/man/random)(4), [openssl-rand](/man/openssl-rand)(1)
