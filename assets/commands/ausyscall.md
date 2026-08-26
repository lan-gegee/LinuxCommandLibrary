# TAGLINE

在 Linux 系统调用名称与编号之间相互映射

# TLDR

按名称**查找系统调用的编号**

```ausyscall [openat]```

按编号**查找系统调用的名称**

```ausyscall [257]```

**导出当前架构的完整系统调用表**

```ausyscall --dump```

**导出特定架构的系统调用表**

```ausyscall [i386] --dump```

在特定架构上**查找系统调用**

```ausyscall [arm64] [connect]```

**要求精确匹配**（不做子串匹配）

```ausyscall --exact [open]```

# SYNOPSIS

**ausyscall** [_arch_] _name_|_number_ [**--exact**]

**ausyscall** [_arch_] **--dump**

# PARAMETERS

_ARCH_
> 目标架构：`b32` / `b64`（双架构快捷方式），或明确指定名称，如 `i386`、`x86_64`、`aarch64`/`arm64`、`arm`、`ppc`、`ppc64le`、`s390x`、`riscv64`。默认为当前运行内核的架构。

_NAME_
> 系统调用名称（如 `openat`、`execve`）。除非给定 `--exact`，否则采用子串匹配。

_NUMBER_
> 数字形式的系统调用编号。

**--dump**
> 列出所选架构的所有系统调用名称和编号。

**--exact**
> 要求名称精确匹配，而非子串匹配。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# DESCRIPTION

**ausyscall** 是 **Linux audit** 框架中的一个小型查询工具。它是将审计日志、`strace` 输出、`seccomp` 过滤器和 BPF 程序中出现的系统调用编号翻译成人类可读名称（或反向转换）的权威工具，适用于所有受支持的架构。

不同架构的系统调用编号并不相同 —— `openat` 在 x86_64 上是 257，而在 i386 上是 295 —— 因此在查看由另一台机器产生的日志时，务必传入正确的架构。

# CAVEATS

属于 **audit** 软件包（`audit-userspace`）。系统调用表在构建时被固化进来；较旧的 audit 版本可能缺少最新的系统调用。在多架构内核上，请使用 `b32`/`b64` 快捷方式选择正确的 ABI。

# HISTORY

**ausyscall** 随最初由 **Red Hat** 开发（主要贡献者为 **Steve Grubb**）的 Linux Audit 用户空间工具一同发布。它使用与 `auparse` 同存于 audit 源码树中的系统调用表。

# INSTALL

```apt: sudo apt install auditd```

```dnf: sudo dnf install audit```

```pacman: sudo pacman -S audit```

```apk: sudo apk add audit```

```zypper: sudo zypper install audit```

```nix: nix profile install nixpkgs#audit```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[auditctl](/man/auditctl)(8), [ausearch](/man/ausearch)(8), [aureport](/man/aureport)(8), [strace](/man/strace)(1)
