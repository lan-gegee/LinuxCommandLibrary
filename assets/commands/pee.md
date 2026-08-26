# TAGLINE

将 stdin 复制给多个命令

# TLDR

**通过管道传给多个命令**

```echo "data" | pee [cmd1] [cmd2]```

**分流到多个进程**

```cat [file] | pee "wc -l" "wc -w"```

**边处理边保存**

```cat [log] | pee "grep error" "cat > copy.log"```

# SYNOPSIS

**pee** [_command_...]

# PARAMETERS

_COMMAND_
> 接收输入的命令。

每个命令都会收到一份 stdin 的副本。

# DESCRIPTION

**pee** 将 stdin 复制给多个命令。类似 tee，但面向的是进程。

该工具把输入复制给各个命令。属于 moreutils。

# CAVEATS

属于 moreutils。每个命令都获得完整输入。并行执行。

# HISTORY

pee 是 **moreutils** 的一部分，用于向多个进程进行管道传输。

# INSTALL

```apt: sudo apt install moreutils```

```dnf: sudo dnf install moreutils```

```pacman: sudo pacman -S moreutils```

```apk: sudo apk add moreutils```

```zypper: sudo zypper install moreutils```

```brew: brew install moreutils```

```nix: nix profile install nixpkgs#moreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tee](/man/tee)(1), [moreutils](/man/moreutils)(7)
