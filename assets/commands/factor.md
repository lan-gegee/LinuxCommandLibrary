# TAGLINE

质因数分解工具

# TLDR

**分解一个数**

```factor [12]```

**分解多个数**

```factor [12] [100] [256]```

从 stdin 读取数字

```echo "[123456]" | factor```

交互式分解数字

```factor```

**分解一个大数**

```factor [9999999999999999999999]```

以指数记法显示质因数

```factor -h [1024]```

# SYNOPSIS

**factor** [_OPTION_] [_NUMBER_...]

# PARAMETERS

**-h**, **--exponents**
> 以 p^e 的形式输出因数，而不是把质数 p 重复 e 次。若指数 e 为 1 则省略。

**--help**
> 显示帮助信息并退出。

**--version**
> 显示版本信息并退出。

_NUMBER_
> 一个或多个要分解的整数。未给出时从 stdin 读取。

# DESCRIPTION

**factor** 对每个指定的整数进行质因数分解并输出结果。对每个输入数字，它先输出该数字，后跟冒号和按升序排列的质因数，重复的因数会重复列出。

例如，**factor 12** 输出 **12: 2 2 3**，因为 12 = 2 × 2 × 3。质数只返回其自身作为唯一因数。数字 1 没有质因数，只返回 **1:**。

不带参数调用时，factor 进入交互模式，从 stdin 逐行读取数字。这对分解大量数字或与管道结合使用很有用。

实现上对小因数使用试除法，对较大的数使用 Pollard's rho 算法。启用 GNU MP 支持构建的 GNU coreutils factor 可以处理任意大的数字，而某些实现则有大小限制。

常见用途包括数学探索、密码学教学、数论问题，以及验证素性（质数的因数只有它自身）。

# CAVEATS

非常大的数字分解耗时更长。某些实现对数字大小有限制。输入必须是正整数。零没有质因数分解。大半素数（两个大质数的乘积）的性能受基本数学规律的限制。

# HISTORY

**factor** 是一款经典 Unix 工具，**1971 年**随 Version 1 Unix 出自贝尔实验室。它一直是 Unix 及类 Unix 系统的一部分，现收录于 GNU coreutils。该命令是 Unix 早期较简单的数学工具之一，与之相伴的还有列出质数的 **primes**。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[primes](/man/primes)(6), [bc](/man/bc)(1), [dc](/man/dc)(1), [expr](/man/expr)(1)
