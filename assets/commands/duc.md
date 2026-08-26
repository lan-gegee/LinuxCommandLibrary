# TAGLINE

带可视化的索引式磁盘用量计算器

# TLDR

**为目录建立索引**

```duc index [/path/to/directory]```

**列出目录大小**

```duc ls [/path]```

**交互式终端 UI**

```duc ui [/path]```

**图形化旭日图视图**

```duc gui [/path]```

**显示数据库信息**及各路径的最后索引时间

```duc info```

**生成旭日图图片**

```duc graph -o [usage.png] [/path]```

**导出为 JSON**

```duc json [/path]```

# SYNOPSIS

**duc** _command_ [_options_] [_path_]

# SUBCOMMANDS

**index** _path_
> 扫描文件系统并把结果写入数据库。其他所有子命令读取的都是这个数据库。

**ls** [_path_]
> 列出目录大小，可选附带条形图。**-R** 递归，**-g** 绘制条形，**-d** 限制深度。

**ui** [_path_]
> 用于浏览索引的交互式 ncurses 界面。

**gui** [_path_]
> 带可点击旭日图的 X11 窗口。

**graph** [_path_]
> 将旭日图或矩形树图渲染为 PNG、SVG 或 PDF 文件。

**xml** / **json**
> 导出索引，供其他工具消费。

**cgi**
> 以 CGI 脚本的形式通过 HTTP 提供索引服务。

**info**
> 列出数据库中已索引的路径及其大小和各自的索引时间。

# PARAMETERS

**-d**, **--database** _FILE_
> 要使用的数据库。默认为 `~/.duc.db`，可通过 `DUC_DATABASE` 环境变量覆盖。

**-x**, **--one-file-system**
> 建索引时不跨越文件系统边界。

**-e**, **--exclude** _PATTERN_
> 建索引时跳过匹配模式的文件。

**--check-hard-links**
> 硬链接的文件只计一次。

**-p**, **--progress**
> 在长时间的索引过程中显示进度。

**-o**, **--output** _FILE_
> **graph** 的输出文件。

**-f**, **--format** _FORMAT_
> 图形输出格式：`png`、`svg`、`pdf` 或 `html`。

# DESCRIPTION

**duc**（Disk Usage Calculator）将文件系统使用情况索引进数据库，以便快速反复查询，并提供多种可视化界面。与每次运行都重新扫描文件系统的工具不同，duc 先做一次初始扫描建立索引，之后便可基于缓存数据即时查询和可视化。

工作流程分两个阶段：先用 **duc index** 扫描目录并构建数据库；再通过各种接口（ls、ui、gui、graph）查询数据库。这种方式对大型文件系统特别有效，因为在那种规模下反复全量扫描慢得无法接受。

duc 提供四种主要可视化模式：ls（命令行列表）、ui（交互式 ncurses 界面）、gui（带旭日图的图形化 X11 窗口）和 graph（生成静态图片）。图形模式以直观的方式呈现磁盘占用情况，一眼就能找出大目录。

数据库存储完整的尺寸信息，包括所有目录层级的文件数量和大小。多次文件系统扫描的结果可以共存于同一个数据库中，并且 duc 会记录每次扫描的时间。

正是这种设计使 duc 成为**大型**文件系统的合适工具。给多 TB 的文件服务器建索引用时很长，但只需做一次，通常由每晚的 cron 任务完成，之后任意次数的查询和可视化都是即时的。每次运行都重新扫描的 `ncdu` 和 `du` 在这种规模下就不实用了。

# CAVEATS

**索引是快照，不是实时视图。** duc 报告的一切都反映 `duc index` 上次运行时的文件系统状态，所以今天上午删除的文件在下次建索引之前仍会占据 duc 报告中的空间。这是该设计上的根本取舍，常见的应对办法就是定时任务。

没有增量索引：重建索引会从头开始重新扫描整棵树。

各界面的依赖彼此独立，发行版又常常把它们拆分到不同软件包中，因此未编译进 ncurses 支持时 `duc ui` 可能缺失，`duc gui` 则需要 X11 和 cairo。缺少这些组件的 duc 依然能正常建索引和列表，这让初次想用旭日图的人摸不着头脑。

# HISTORY

duc 由 **Ico Doornekamp** 编写，是他早期作品 `philesight` 的后继者，其全部立意就在于把扫描与查看分离。当文件系统大到需要以小时而非秒来衡量遍历时间时，这种区分就变得重要了——此时大家在笔记本上常用的那些交互式扫描器都不再可行，带索引的数据库成了唯一可行的方案。

# INSTALL

```apt: sudo apt install duc```

```dnf: sudo dnf install duc```

```zypper: sudo zypper install duc```

```brew: brew install duc```

```nix: nix profile install nixpkgs#duc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[du](/man/du)(1), [ncdu](/man/ncdu)(1), [dua](/man/dua)(1), [dust](/man/dust)(1), [baobab](/man/baobab)(1)

# RESOURCES

```[Source code](https://github.com/zevv/duc)```

```[Homepage](https://duc.zevv.nl)```

<!-- verified: 2026-07-14 -->
