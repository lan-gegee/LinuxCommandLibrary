# TAGLINE

实时监视网络带宽

# TLDR

显示**所有接口**

```bmon -a```

以**比特每秒**显示数据传输速率

```bmon -b```

指定要显示的**接口**

```bmon -p [interface_1,interface_2,interface_3,...]```

指定**速率计算间隔**（秒）

```bmon -R [2.0]```

# SYNOPSIS

**bmon** [_options_]

# DESCRIPTION

**bmon** 是一个带宽监视器和速率估算器，以可视化方式显示网络接口统计信息。它实时展示网络接口的吞吐量、每秒数据包数和错误率。

该工具既提供图形化 TUI 显示，也提供适合脚本和日志记录的文本输出选项。

# PARAMETERS

**-a, --show-all**
> 显示所有接口，包括没有流量的接口。

**-b, --use-bit**
> 以比特每秒而非字节显示速率。

**-p, --policy** _interfaces_
> 要显示的接口列表，以逗号分隔。

**-R, --rate-interval** _seconds_
> 速率计算间隔（默认：1.0）。

**-r, --read** _file_
> 从文件而不是实时数据读取输入。

**-o, --output** _format_
> 输出格式：ascii、curses、format、null。

**-i, --input** _module_
> 指定输入模块（如 netlink、proc、dummy）。

**-f, --configfile** _file_
> 从给定文件加载配置。

**-U, --unit** _unit_
> 强制使用特定单位显示速率（如 B、KiB、MiB）。

# INSTALL

```apt: sudo apt install bmon```

```dnf: sudo dnf install bmon```

```pacman: sudo pacman -S bmon```

```apk: sudo apk add bmon```

```zypper: sudo zypper install bmon```

```brew: brew install bmon```

```nix: nix profile install nixpkgs#bmon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[iftop](/man/iftop)(8), [nethogs](/man/nethogs)(8), [vnstat](/man/vnstat)(1), [nload](/man/nload)(1)
