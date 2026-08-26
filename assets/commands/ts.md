# TAGLINE

在命令输出行的行首添加时间戳

# TLDR

为命令输出**添加时间戳**

```[command] | ts```

**使用 ISO 8601 格式**的时间戳

```[command] | ts -i```

时间戳中**包含毫秒**

```[command] | ts -m```

**使用 UTC 时间**而非本地时间

```[command] | ts -u```

**显示程序启动以来**的累计时间

```[command] | ts -s```

**显示距上一行**经过的时间

```[command] | ts -i```

**自定义时间戳格式**

```[command] | ts '[%Y-%m-%d %H:%M:%S]'```

**将现有时间戳**转换为相对时间

```[command] | ts -r```

# SYNOPSIS

**ts** [**-imsu**] [**-r**] [_format_]

# PARAMETERS

**-i**
> 显示距上一个时间戳经过的时间

**-s**
> 显示程序启动以来经过的时间

**-m**
> 时间戳中包含毫秒

**-u**
> 使用 UTC 时间而非本地时间

**-r**
> 将输入中的现有时间戳转换为相对时间（例如 "15m5s ago"）

_format_
> 自定义 strftime 格式（默认："%b %d %H:%M:%S"）

# DESCRIPTION

**ts** 从标准输入读取每一行，在每行前添加时间戳后写入标准输出。它属于 **moreutils** 软件包，适用于日志记录、调试以及持续监控命令输出。

默认时间戳格式为 "**%b %d %H:%M:%S**"（例如 "Jan 22 14:30:45"）。自定义格式使用 strftime 转换说明符。扩展说明符 **%.S**、**%.s** 和 **%.T** 提供亚秒级精度。

**-s** 选项显示从 ts 启动开始的累计时间，适合测量总耗时。**-i** 选项显示各行之间的间隔，有助于找出管道中较慢的操作。

**-r** 选项将输入中的现有时间戳转换为人类可读的相对时间，支持多种常见的时间戳格式。

# EXAMPLES

**监控日志文件并添加时间戳**
```
tail -f /var/log/syslog | ts
```

**测量构建过程每行的耗时**
```
make 2>&1 | ts -i '[%H:%M:%S]'
```

**跟踪脚本总运行时长**
```
./long_script.sh | ts -s '%.T'
```

# CAVEATS

ts 依赖 **moreutils** 软件包，系统默认可能未安装。该命令会对输出做缓冲，与产出较慢的命令配合使用时可能造成轻微延迟。时间戳反映的是 ts 接收每行的时刻，而不是原始命令产生该行的时刻。

# HISTORY

**ts** 由 **Joey Hess** 编写，是 **moreutils** 工具集的一部分。moreutils 于 **2006** 年前后首次发布，旨在提供补充标准 coreutils 的额外工具，填补常见命令行工作流中的空白。

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

[date](/man/date)(1), [sponge](/man/sponge)(1), [chronic](/man/chronic)(1)
