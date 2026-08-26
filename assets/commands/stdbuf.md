# TAGLINE

调整命令的流缓冲

# TLDR

**stdout 按行缓冲**

```stdbuf -oL [command]```

**stdout 不缓冲**

```stdbuf -o0 [command]```

**stderr 不缓冲**

```stdbuf -e0 [command]```

**stdin 完全缓冲**

```stdbuf -i[1M] [command]```

**所有流都按行缓冲**

```stdbuf -oL -eL [command]```

**与 grep 组合使用**

```stdbuf -oL [command] | grep [pattern]```

# SYNOPSIS

**stdbuf** [_-i mode_] [_-o mode_] [_-e mode_] _command_ [_args_]

# PARAMETERS

**-i** _MODE_
> stdin 缓冲方式。

**-o** _MODE_
> stdout 缓冲方式。

**-e** _MODE_
> stderr 缓冲方式。

# MODES

**L** - 按行缓冲
**0** - 不缓冲
**SIZE** - 缓冲区大小（如 1K、1M）

# DESCRIPTION

**stdbuf** 以修改后的标准流缓冲方式运行命令。当程序检测到输出流向管道而非终端时，通常会从行缓冲切换为全缓冲，从而延迟输出。stdbuf 使用 LD_PRELOAD 拦截缓冲调用，覆盖这一行为。

三种模式分别是：行缓冲（**L**），每次换行后刷新；不缓冲（**0**），立即刷新；以及特定的缓冲区大小。当需要通过 **grep** 或 **awk** 等过滤器管道传输输出并获得实时结果，而不是等待缓冲区填满时，这尤其有用。

# CAVEATS

并非对所有程序有效。静态链接的程序不受影响。有些程序使用内部缓冲。

# HISTORY

**stdbuf** 是 GNU coreutils 的一部分。它使用 LD_PRELOAD 来拦截缓冲调用。

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

[unbuffer](/man/unbuffer)(1), [script](/man/script)(1), [tee](/man/tee)(1)
