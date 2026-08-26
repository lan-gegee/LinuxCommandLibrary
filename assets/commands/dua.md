# TAGLINE

快速的并行磁盘用量分析器

# TLDR

**分析当前目录**

```dua```

**分析指定路径**

```dua [/path/to/directory]```

**交互模式**

```dua i```

**针对指定路径的交互模式**

```dua i [/path/to/directory]```

**显示表面大小**而非磁盘用量

```dua -A [/path/to/directory]```

**使用指定数量的线程**

```dua -t [4] [/path/to/directory]```

**以选定单位显示大小**

```dua -f [MB] [/path/to/directory]```

**不跨文件系统**，不越过挂载点

```dua -x [/path/to/directory]```

**显示版本**

```dua --version```

# SYNOPSIS

**dua** [_flags_] [_options_] [_subcommand_] [_input_...]

# COMMANDS

**i**, **interactive**
> 启动终端用户界面。

**a**, **aggregate**
> 汇总给定路径占用的空间。未给出子命令时这是默认行为。

**config edit** / **config show-default**
> 在 `$EDITOR` 中打开配置文件，或打印默认配置。

**completions** _SHELL_
> 生成 shell 补全脚本。

# PARAMETERS

**-A**, **--apparent-size**
> 显示表面大小而非磁盘用量。

**-t**, **--threads** _COUNT_
> 使用的线程数。**0** 表示每个逻辑处理器一个线程，也是 Linux 上的默认值；macOS 默认为 3，因为更多线程在那里反而明显变慢。设为 1 表示单线程。

**-f**, **--format** _FORMAT_
> 字节格式：`metric`、`binary`、`bytes`、`GB`、`GiB`、`MB`、`MiB`。默认为 binary，macOS 上则为 metric。

**-l**, **--count-hard-links**
> 硬链接文件每遇到一次就计数一次，而不是只计一次。

**-x**, **--stay-on-filesystem**
> 不跨越文件系统，也不遍历挂载点。

**-i**, **--ignore-dirs** _PATH_...
> 遍历时到达即跳过的绝对路径目录。Linux 上默认为 `/proc`、`/dev`、`/sys` 和 `/run`。作为输入路径显式传入的目录仍会被扫描。

**--stats**
> 将遍历统计信息打印到标准错误（aggregate 模式）。

**--no-sort** / **--no-total**
> 保持命令行给出的顺序而不按大小排序，或对多个输入省略总计行。

**-h**, **--help** / **-V**, **--version**
> 显示帮助，或版本信息。

# INTERACTIVE KEYS

**j**/**k** 或 **Down**/**Up**
> 在条目间导航。

**Enter** 或 **l**
> 进入目录。

**u** 或 **h**
> 返回上级目录。

**o**
> 在文件管理器中打开。

**d**
> 标记待删除。

**Space**
> 展开/收起。

**s**
> 按大小排序。

**r**
> 刷新。

**g**
> 跳转到顶部。

**G**
> 跳转到底部。

**Ctrl+c** 或 **q**
> 退出。

# DESCRIPTION

**dua**（Disk Usage Analyzer）是一个快速的磁盘空间分析器，带有可选的交互式界面。它扫描目录并显示大小。

默认模式显示各路径的汇总大小。交互模式（**dua i**）提供可导航的树状视图，便于探索磁盘占用情况。

并行遍历是 dua 快的原因：它能跑满 SSD，而不是一次走一个目录地遍历树，在大目录树上轻松胜过 `du`。在机械硬盘上这一优势基本消失，因为瓶颈在于寻道时间而非 CPU。

表面大小（**-A**）指文件内容本身的大小。不加该选项时，dua 报告的是磁盘上实际占用的空间——释放空间时你关心的正是这个：稀疏文件或高度压缩的 btrfs/ZFS 数据集占用的空间可能远小于其表面大小，而大量小文件占用的空间则可能大得多，因为每个文件都要向上取整到一个块。

在交互模式下，用 **d** 标记条目，确认后即被删除。从 TUI 中删除文件是 dua 相对 `du` 的真正卖点，而且在大型目录树上它刻意做到了比 `rm` 更快。

# CAVEATS

**TUI 中的删除是永久性的。** 文件不会进入回收站，也无法撤销，因此确认删除已标记的选择前值得停顿一下。

注意 **-l**/**--count-hard-links** 会*禁用*默认的去重：默认情况下硬链接的文件只计一次（通常这正是你想要的），而该标志会让每个链接都完整计入。

dua 和 `du` 给出的数字并不总是一致，但两者都没有错：它们在硬链接是否只计一次、是否跨越挂载点、报告的是表面大小还是磁盘占用这几方面存在差异。在下结论说谁在撒谎之前，先确保比较的是同类指标。

# HISTORY

dua 由 **Sebastian Thiel**（Byron）创建，他也编写了 gitoxide，dua 于 **2019 年**前后首次发布。它用 Rust 编写，属于重新审视经典 Unix 工具的那一代工具，前提假设是机器拥有多核和高速 SSD——而 `du` 设计时这两者都不成立。相比 `ncdu` 和 `dust`，它的独特之处在于删除是一等操作，而非事后补充。

# INSTALL

```apk: sudo apk add dua```

```nix: nix profile install nixpkgs#dua```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [ncdu](/man/ncdu)(1), [dust](/man/dust)(1), [gdu](/man/gdu)(1), [duf](/man/duf)(1)

# RESOURCES

```[Source code](https://github.com/Byron/dua-cli)```

<!-- verified: 2026-07-14 -->
