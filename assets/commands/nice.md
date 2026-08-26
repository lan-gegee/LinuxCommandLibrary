# TAGLINE

以调整后的调度优先级运行命令

# TLDR

**以较低优先级运行**

```nice [command]```

**以指定的 nice 值运行**

```nice -n [10] [command]```

**以最高优先级运行（root）**

```nice -n [-20] [command]```

**以最低优先级运行**

```nice -n [19] [command]```

**显示当前 nice 值**

```nice```

# SYNOPSIS

**nice** [_options_] [_command_]

# PARAMETERS

_COMMAND_
> 要运行的命令。

**-n**, **--adjustment=**_N_
> 把整数 _N_ 加到 nice 值上（默认 **10**）。负值会提高优先级。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息。

# DESCRIPTION

**nice** 以修改后的 CPU 调度 nice 值运行命令。nice 值越高，进程就越"友好"，获得的 CPU 时间越少（优先级越低）。

nice 值的范围是 **-20**（最高优先级）到 **19**（最低优先级）。不带命令时，nice 会把 Shell 当前的 nice 值打印到标准输出。给出命令但不带 **-n** 时，nice 默认应用 **+10** 的调整量。

# CAVEATS

负值需要 root 权限。默认调整量为 10。仅影响 CPU 调度。

# HISTORY

nice 是一条经典的 **Unix** 命令，自早期 Unix 起就用于控制进程的调度优先级。

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

[renice](/man/renice)(1), [ionice](/man/ionice)(1), [chrt](/man/chrt)(1)
