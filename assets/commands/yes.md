# TAGLINE

反复输出一个字符串

# TLDR

**反复输出 'y'**（用于自动确认提示）

```yes | [command]```

**反复输出自定义字符串**

```yes "[custom text]"```

**对所有提示自动回答 'no'**

```yes n | [command]```

**只输出有限行数**

```yes | head -n [10]```

# SYNOPSIS

**yes** [_string_...]

# PARAMETERS

_string..._
> 要反复输出的一个或多个字符串，以空格连接（默认："y"）。

**--help**
> 显示帮助并退出。

**--version**
> 显示版本并退出。

# DESCRIPTION

**yes** 会反复输出一个字符串，直到被终止或管道关闭。默认情况下，它无休止地输出 "y" 加换行符。

它的主要用途是通过管道提供给需要确认的命令，自动对所有提示回答 "y"（或任何指定的响应）。对于没有原生批处理/静默模式的命令，这在脚本编写中很有用。

当接收方命令关闭其标准输入（即退出）时，yes 会因管道断裂而自动终止。

不通过管道使用时，yes 会无限运行，必须用 Ctrl+C 中断。

# EXAMPLES

```bash
# Auto-confirm all prompts
yes | apt upgrade

# Auto-answer 'no'
yes n | rm -i *.txt

# Generate test data
yes "test line" | head -1000 > test.txt

# Stress test (generates output as fast as possible)
yes > /dev/null
```

# CAVEATS

使用 yes 会绕过安全提示。在把 yes 通过管道传给破坏性命令之前，请确保你清楚自己在自动确认什么。

某些命令会检测到非交互式输入而拒绝运行或表现不同。可行时请优先使用命令自带的标志（如 **-y** 或 **--yes**）。

yes 以最高速度运行，在没有管道传输给有用目标时可能产生可观的 CPU 负载。发生写入错误时（例如管道断裂），yes 会以状态码 1 退出。

# HISTORY

**yes** 属于 **GNU coreutils**，由 **David MacKenzie** 编写。它源自 Unix System V，自项目早期起就是 coreutils 的一部分。

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

[true](/man/true)(1), [false](/man/false)(1), [head](/man/head)(1), [seq](/man/seq)(1), [timeout](/man/timeout)(1)
