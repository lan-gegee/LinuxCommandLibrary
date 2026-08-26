# TAGLINE

生成指定范围内的素数

# TLDR

**生成范围内的素数**

```primes [start] [stop]```

**列出 100 以内的素数**

```primes 2 100```

**列出 1000 到 2000 之间的素数**

```primes 1000 2000```

# SYNOPSIS

**primes** [_start_] [_stop_]

# PARAMETERS

_START_
> 起始数字。

_STOP_
> 结束数字。

# DESCRIPTION

**primes** 生成并打印指定数值范围内的所有素数。给定起始值和结束值后，它每行输出一个素数，便于通过管道传给其他命令进行计数、过滤或进一步处理。

这个经典 BSD 工具在 macOS 上原生可用，在 Linux 上则作为 bsdgames 软件包的一部分提供。它使用高效的筛法算法，即使对于大范围也能快速生成素数。

# CAVEATS

BSD/macOS 工具。Linux 上属于 bsdgames。

# HISTORY

primes 是用于素数生成的经典 **BSD 工具**。

# INSTALL

```apt: sudo apt install libmath-prime-util-perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[factor](/man/factor)(1), [bc](/man/bc)(1)
