# TAGLINE

一组不属于任何其他类别的实用 Unix 工具合集

# TLDR

**Sponge：先吸收 stdin 再写入**

```cat [file] | grep [pattern] | sponge [file]```

**Ts：添加时间戳**

```[command] | ts '[%Y-%m-%d %H:%M:%S]'```

**Chronic：除非出错否则静默**

```chronic [command]```

**Pee：将输出分流到多个命令**

```echo "[data]" | pee 'wc -l' 'wc -c'```

**Vidir：用编辑器编辑目录**

```vidir [directory]```

**Parallel：并发地对每个参数运行命令**

```parallel -j [4] [cmd] -- [arg1] [arg2] [arg3]```

**Ifne：仅当 stdin 非空时才运行命令**

```[command] | ifne [other_command]```

**Errno：查询 errno 值**

```errno [ENOENT]```

# SYNOPSIS

**moreutils** - collection of Unix tools

# DESCRIPTION

**moreutils** 是一组不属于任何其他类别的实用 Unix 工具合集。每个工具都只做好一件事，并能与标准 Unix 管道集成。

核心工具包括 sponge、ts、chronic、vidir、parallel、ifdata 等。

# KEY UTILITIES

```
sponge   - Soak up stdin, then write to file
ts       - Prepend timestamps to lines
chronic  - Run a command quietly unless it fails
vidir    - Edit a directory listing in $EDITOR
parallel - Run multiple jobs concurrently
pee      - Tee stdin to multiple command pipelines
ifdata   - Query network interface info
combine  - Combine sets of lines from two files (and, or, not, xor)
ifne     - Run a command only if stdin is non-empty
errno    - Look up errno names and descriptions
mispipe  - Pipe two commands, returning the exit status of the first
isutf8   - Check if files are valid UTF-8
lckdo    - Run a command with a lock held
zrun     - Decompress arguments before running a command
```

# SPONGE EXAMPLE

```bash
# Edit file in place (normally fails)
sort file | sponge file
```

# CAVEATS

工具的可用性因软件包版本而异。某些工具与其他软件包存在冲突（如 parallel 与 GNU parallel）。

# HISTORY

moreutils 由 **Joey Hess** 自 **2006 年**起创建，旨在收集标准 Unix 中缺失的实用小工具。

# INSTALL

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[coreutils](/man/coreutils)(1), [parallel](/man/parallel)(1), [ts](/man/ts)(1), [sponge](/man/sponge)(1)
