# TAGLINE

禁用命令的输出缓冲

# TLDR

**以无缓冲输出运行命令**

```unbuffer [command]```

**在管道中取消缓冲**

```[command1] | unbuffer -p [command2] | [command3]```

**在管道中取消 grep 的缓冲**

```tail -f [logfile] | unbuffer -p grep [pattern]```

**取消脚本的输出缓冲**

```unbuffer ./[script.sh] | tee [output.log]```

# SYNOPSIS

**unbuffer** [**-p**] _program_ [_args_]

# PARAMETERS

**-p**
> 管道模式：从 stdin 读取并传递给程序。

_program_
> 要以无缓冲输出运行的命令。

_args_
> 传递给程序的参数。

# DESCRIPTION

**unbuffer** 用于禁用在程序输出被重定向时发生的输出缓冲。许多程序在未连接终端时会缓冲其输出，这在管道中可能导致延迟或问题。

该工具的原理是将程序连接到伪终端（pty），使其表现得像在交互式运行一样。这会强制行缓冲或无缓冲输出，即使输出被重定向到文件或管道也是如此。

常见用例包括通过 grep 实时监视日志文件、捕获彩色输出，以及确保脚本中的实时输出。

unbuffer 是 Expect 软件包的一部分，使用 Expect 的 pty 处理能力。

# CAVEATS

默认不读取 stdin；管道模式请使用 -p。在带 -p 的管道模式下，unbuffer 遇到 EOF 时会立即退出。可能影响检测终端能力的程序。属于 expect 软件包，并非所有系统都默认安装。

# HISTORY

**unbuffer** 是 NIST 的 Don Libes 开发的 Expect 软件包的一部分。Expect 记载于《Exploring Expect: A Tcl-Based Toolkit for Automating Interactive Programs》（O'Reilly，1995）一书。该工具解决的是 Unix 管道中输出缓冲这一常见问题。

# INSTALL

```apt: sudo apt install expect```

```dnf: sudo dnf install expect```

```pacman: sudo pacman -S expect```

```apk: sudo apk add expect```

```zypper: sudo zypper install expect```

```brew: brew install expect```

```nix: nix profile install nixpkgs#expect```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[expect](/man/expect)(1), [stdbuf](/man/stdbuf)(1), [script](/man/script)(1), [tee](/man/tee)(1)
