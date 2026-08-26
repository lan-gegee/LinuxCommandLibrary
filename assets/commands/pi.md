# TAGLINE

计算并显示阿基米德常数 Pi 的十进制数字

# TLDR

显示 Pi 的 **100 位数字**

```pi```

显示**指定数量**的数字

```pi [1000]```

显示**参考文献**

```pi --bibliography```

显示**帮助**

```pi --help```

# SYNOPSIS

**pi** [_digits_] [**--bibliography**] [**--help**] [**--version**]

# PARAMETERS

**digits**
> 要计算的十进制位数（默认：100）

**--bibliography**
> 显示关于 Pi 计算的推荐阅读材料

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pi** 计算并显示阿基米德常数 Pi（π）的十进制数字。它使用高效算法将 Pi 计算到任意精度，仅受可用内存和时间的限制。

该工具可用于测试系统性能、生成 Pi 数字以供验证，或对这一数学常数进行教学探索。

# CAVEATS

非常大的位数需要大量计算时间和内存。结果每次运行都重新计算（不缓存）。在某些系统上是 GNU coreutils 的一部分。

# HISTORY

**pi** 的各种实现早已存在于不同的 Unix 系统中。借助 Chudnovsky 算法等专用算法，Pi 已被计算到数万亿位，不过命令行工具出于实用考虑通常只计算较少的位数。

# INSTALL

```apt: sudo apt install pi```

```dnf: sudo dnf install cln```

```pacman: sudo pacman -S cln```

```apk: sudo apk add cln```

```zypper: sudo zypper install cln```

```brew: brew install cln```

```nix: nix profile install nixpkgs#cln```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bc](/man/bc)(1), [dc](/man/dc)(1), [factor](/man/factor)(1)
