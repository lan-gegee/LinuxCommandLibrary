# TAGLINE

GNU 核心 Unix 实用工具集

# TLDR

**列出 GNU coreutils 中的所有命令**

```coreutils --help```

**通过 multicall 二进制运行 coreutils 命令**

```coreutils [ls] -la```

**检查 coreutils 版本**

```coreutils --version```

**通过 coreutils 运行 cat**

```coreutils cat [file.txt]```

**通过 coreutils 运行 basename**

```coreutils basename [/path/to/file.txt]```

# SYNOPSIS

**coreutils** [_command_] [_arguments_]

# PARAMETERS

**--help**
> 列出 coreutils 软件包中所有可用的命令。

**--version**
> 显示 coreutils 的版本信息。

_COMMAND_
> 要执行的任意 coreutils 命令（ls、cat、cp、mv 等）。

# DESCRIPTION

**GNU Coreutils** 是一套基本的文件、shell 和文本处理实用工具，任何类 Unix 操作系统上都应该具备。**coreutils** 命令本身是一个 multicall 二进制文件，可以调用其中包含的任何实用程序。

该软件包包含文件操作（cp、mv、rm、ls、mkdir）、文本处理（cat、head、tail、sort、uniq、wc）、shell 工具（echo、printf、test、expr）和系统信息（uname、hostname、uptime、who）等基本命令。

在大多数 Linux 系统上，这些实用工具以独立二进制文件的形式安装在 /usr/bin 或 /bin 中。multicall 二进制文件适用于容器或嵌入式系统等精简环境——单个二进制即可提供全部功能，与 BusyBox 类似。

# INCLUDED COMMANDS

**文件操作**: cp, mv, rm, ln, mkdir, rmdir, touch, chmod, chown, ls, dir, vdir

**文本处理**: cat, head, tail, sort, uniq, wc, cut, paste, join, tr, fold

**Shell 工具**: echo, printf, test, expr, true, false, yes, seq, sleep

**系统信息**: uname, hostname, uptime, who, whoami, id, groups, date

# CAVEATS

GNU coreutils 与 BSD/macOS 实现之间的行为可能不同。某些选项是 GNU 扩展，在其他 Unix 系统上不可用。并非所有发行版都默认安装 multicall 二进制文件。

# HISTORY

GNU Coreutils 于 **2002** 年由三个 GNU 软件包合并而成：fileutils、shellutils 和 textutils。这些实用工具是 Richard Stallman 于 **1983** 年发起的 GNU 计划的一部分，旨在为专有 Unix 工具提供自由替代品。

# INSTALL

```apt: sudo apt install rust-coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ls](/man/ls)(1), [cp](/man/cp)(1), [mv](/man/mv)(1), [cat](/man/cat)(1), [busybox](/man/busybox)(1)

# RESOURCES

```[Source code](https://git.savannah.gnu.org/cgit/coreutils.git)```

```[Homepage](https://www.gnu.org/software/coreutils/)```

```[Documentation](https://www.gnu.org/software/coreutils/manual/)```

<!-- verified: 2026-06-23 -->
