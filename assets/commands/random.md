# TAGLINE

内核随机数生成器设备

# TLDR

**从 /dev/urandom 读取 16 个随机字节**

```head -c 16 /dev/urandom```

**生成随机十六进制字符串**

```head -c 16 /dev/urandom | xxd -p```

**生成随机 base64 字符串**

```head -c 32 /dev/urandom | base64```

**从 /dev/random 读取**（阻塞，高熵）

```dd if=/dev/random bs=1 count=32```

**检查熵池中的可用熵**

```cat /proc/sys/kernel/random/entropy_avail```

# SYNOPSIS

**/dev/random**

**/dev/urandom**

# DESCRIPTION

**/dev/random** 和 **/dev/urandom** 是特殊的字符设备文件，提供对 Linux 内核密码学安全随机数生成器的访问。它们将来自设备驱动、硬件中断和其他来源的环境噪声收集到熵池中。

**/dev/urandom**（unlimited random）是大多数应用的首选来源。它立即返回随机字节而不阻塞，使用从熵池重新播种的 CSPRNG。它适用于加密密钥、会话令牌和一般性随机数需求。

当熵池估计不足以满足请求的随机数量时，**/dev/random** 会阻塞。这在历史上被认为更安全，但在现代系统上很少有必要。它可能导致应用程序因等待熵而挂起。

在正常工作的系统上，两种设备提供的输出都适合密码学用途。

# CAVEATS

在熵源有限的系统（无头服务器、虚拟机）上，**/dev/random** 可能无限期阻塞。除非你对阻塞行为有特殊要求，否则请使用 **/dev/urandom**。

快速读取大量数据可能暂时耗尽熵池。如需批量生成随机数据，可考虑使用 **openssl rand**，它能更高效地使用相同的底层 CSPRNG。

虚拟机在启动时可能缺乏足够的熵源。可以考虑使用 **haveged** 或硬件随机数生成器（HRNG）来补充熵。

# HISTORY

/dev/random 接口由 Theodore Ts'o 于 1995 年在 **Linux 1.3.30** 中引入。其设计受到 PGP 随机数生成的启发，利用内核收集的熵提供密码学质量的随机数。/dev/random 与 /dev/urandom 的区别随内核版本不断演变，现代内核在完成初始播种后对二者的处理几乎相同。

# INSTALL

```aur: yay -S random```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dd](/man/dd)(1), [head](/man/head)(1), [openssl](/man/openssl)(1), [haveged](/man/haveged)(8), [getrandom](/man/getrandom)(2)
