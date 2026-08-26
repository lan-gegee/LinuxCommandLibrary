# TAGLINE

Great Internet Mersenne Prime Search 客户端

# TLDR

**启动 Prime95（交互模式）**

```mprime```

**运行压力测试（torture test）**

```mprime -t```

**运行指定类型的测试**

```mprime -t -W[1]```

**以守护进程方式运行**

```mprime -d```

**设置工作线程数**

```mprime -t -w[4]```

# SYNOPSIS

**mprime** [_options_]

# PARAMETERS

**-t**
> 压力测试模式。

**-d**
> 以守护进程方式运行。

**-w** _n_
> 工作进程数量。

**-W** _type_
> 压力测试类型。

**-m**
> 菜单模式。

**-v**
> 打印版本信息。

# DESCRIPTION

**mprime**（Linux 版 Prime95）是 Great Internet Mersenne Prime Search（GIMPS）的客户端。它搜索梅森素数，也可用于 CPU 压力测试和基准测试。

压力测试模式常用于检验系统稳定性，尤其是在超频之后。

# TORTURE TEST TYPES

```
1 - Small FFTs (tests L2 cache)
2 - In-place FFTs (tests RAM)
3 - Large FFTs (tests all)
4 - Blend (mixed test)
```

# CONFIGURATION

**~/primenet.ini**
> PrimeNet 服务器通信设置与账户配置。

**~/local.txt**
> 本地工作偏好与计算设置。

# CAVEATS

极度消耗 CPU。产生大量热量。不适合笔记本电脑。素数搜索可能需要 GIMPS 账户。

# HISTORY

Prime95/mprime 由 **George Woltman** 于 **1996 年**为 GIMPS 项目创建。它已发现多个打破纪录的梅森素数。

# INSTALL

```nix: nix profile install nixpkgs#mprime```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[stress](/man/stress)(1), [stress-ng](/man/stress-ng)(1)
