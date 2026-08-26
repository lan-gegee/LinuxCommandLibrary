# TAGLINE

显示从 /proc/cpuinfo 收集的 CPU 架构信息

# TLDR

显示关于**所有 CPU** 的信息

```lscpu```

以**表格格式**显示信息

```lscpu -e```

只显示**在线 CPU** 的信息

```lscpu -e -b```

只显示**离线 CPU** 的信息

```lscpu -e -c```

显示 **CPU 缓存**的详细信息

```lscpu -C```

以 **JSON 格式**显示信息

```lscpu -J```

# SYNOPSIS

**lscpu** [_-e_] [_-b_] [_-c_] [_-C_] [_-J_] [_-p_]

# DESCRIPTION

**lscpu** 显示从 /proc/cpuinfo 和 sysfs 收集的 CPU 架构信息，包括 CPU 型号、核心数、线程数、缓存、NUMA 节点和 CPU 标志。

# PARAMETERS

**-e, --extended**
> 以扩展（表格）格式显示信息

**-b, --online**
> 只显示在线 CPU（配合 -e）

**-c, --offline**
> 只显示离线 CPU（配合 -e）

**-C, --caches**
> 显示 CPU 缓存的详细信息

**-J, --json**
> 以 JSON 格式输出

**-p, --parse**
> 优化输出以便解析

**-x, --hex**
> 对 CPU 集使用十六进制掩码

**-y, --physical**
> 打印物理 ID 而非逻辑 ID

**-s, --sysroot dir**
> 使用指定目录作为系统根目录

# CAVEATS

信息因架构和内核版本而异。某些字段可能并非在所有系统上都可用。

# HISTORY

属于 **util-linux** 软件包。提供了一种查看 CPU 信息的便捷方式，无需手动解析 /proc/cpuinfo。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add lscpu```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmidecode](/man/dmidecode)(8), [nproc](/man/nproc)(1)
