# TAGLINE

改变程序执行时报告的架构

# TLDR

以 i686 架构身份**运行**命令

```setarch i686 [command]```

以 x86_64 架构**运行** shell

```setarch x86_64 [bash]```

**禁用**虚拟地址空间随机化

```setarch [linux32] -R [command]```

**列出**支持的架构

```setarch --list```

# SYNOPSIS

**setarch** [_arch_] [_options_] [_program_ [_arguments_]]

# PARAMETERS

**arch**
> 目标架构（i686、x86_64、linux32、linux64 等）

**-R, --addr-no-randomize**
> 禁用地址空间布局随机化（ASLR）。

**-F, --fdpic-funcptrs**
> 将用户空间函数指针视为指向函数描述符的指针。

**-Z, --mmap-page-zero**
> 为旧式程序开启 MMAP_PAGE_ZERO。

**-L, --addr-compat-layout**
> 使用旧式虚拟地址空间布局。

**-X, --read-implies-exec**
> 开启 READ_IMPLIES_EXEC。

**-B, --32bit**
> 开启 ADDR_LIMIT_32BIT。

**-I, --short-inode**
> 开启 SHORT_INODE。

**-S, --whole-seconds**
> 开启 WHOLE_SECONDS。

**-T, --sticky-timeouts**
> 开启 STICKY_TIMEOUTS。

**-3, --3gb**
> 使用 3GB 内存布局。

**--uname-2.6**
> 在 uname 中报告 2.6 内核版本。

**--list**
> 列出支持的架构并退出。

**-v, --verbose**
> 显示详细输出。

**-h, --help**
> 显示帮助。

# DESCRIPTION

**setarch** 改变程序执行环境中报告的架构。它会修改 **uname -m** 的输出，并可能影响依赖架构检测的程序行为。

该命令适用于在 64 位系统上运行 32 位应用、进行兼容性测试，以及调试那些因架构不同而表现不同的程序。**linux32** 和 **linux64** 符号链接是常见用法的快捷方式。

# CAVEATS

并不提供真正的架构模拟；底层 CPU 必须支持所请求的模式。禁用 ASLR（**-R**）会降低安全性，只应用于调试。属于 util-linux 软件包的一部分。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add setarch```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[linux32](/man/linux32)(8), [linux64](/man/linux64)(8), [uname](/man/uname)(1), [personality](/man/personality)(2)
