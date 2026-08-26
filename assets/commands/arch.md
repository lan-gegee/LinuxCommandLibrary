# TAGLINE

打印机器硬件架构

# TLDR

**打印**机器架构

```arch```

# SYNOPSIS

**arch**

# DESCRIPTION

**arch** 打印机器硬件架构。在 Linux 上这是 GNU coreutils 命令，等同于 **uname -m**。除 **--help** 和 **--version** 外没有其他选项。

常见输出包括：
- **x86_64**: 64 位 Intel/AMD
- **aarch64** 或 **arm64**: 64 位 ARM
- **i686** 或 **i386**: 32 位 Intel
- **armv7l**: 32 位 ARM
- **ppc64le**: 64 位 PowerPC 小端序
- **riscv64**: 64 位 RISC-V

# CAVEATS

报告的值取决于内核 personality 而非实际芯片——在 **setarch** 下运行或处于 32 位 chroot 中时，64 位机器可能报告为 **i686**。macOS 上的系统 **arch** 二进制文件与此无关；它的作用是把进程切换到另一种架构，而不是打印架构。

# HISTORY

**arch** 自 BSD 时代起就在 Unix 系统上可用。在 Linux 上它是 coreutils 的一部分，是对 uname 的简单封装。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add uutils-coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[uname](/man/uname)(1), [setarch](/man/setarch)(8), [hostnamectl](/man/hostnamectl)(1)
