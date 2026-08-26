# TAGLINE

显示进程的工作目录

# TLDR

打印进程的**当前工作目录**

```pwdx 1234```

打印**多个进程**的工作目录

```pwdx 1234 5678```

# SYNOPSIS

**pwdx** [_option_...] _pid_...

# DESCRIPTION

**pwdx** 报告进程的当前工作目录。它从 /proc/[pid]/cwd 读取该信息，并为每个指定的进程 ID 显示目录路径。

# PARAMETERS

**-V, --version**
> 输出版本信息并退出

**-h, --help**
> 输出帮助信息并退出

# CAVEATS

运行 pwdx 的用户必须能够访问该进程。对于其他用户拥有的进程，可能需要 root 权限才能访问其工作目录信息。

# HISTORY

**pwdx** 由 Nicholas Miell 于 2004 年创建，是 **procps-ng** 软件包的一部分。它类似于 SunOS 中同名的命令。

# INSTALL

```apt: sudo apt install procps```

```dnf: sudo dnf install procps-ng```

```pacman: sudo pacman -S procps-ng```

```apk: sudo apk add procps-ng```

```zypper: sudo zypper install procps```

```brew: brew install procps```

```nix: nix profile install nixpkgs#procps```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ps](/man/ps)(1), [pgrep](/man/pgrep)(1), [lsof](/man/lsof)(8), [readlink](/man/readlink)(1), [proc](/man/proc)(5)
