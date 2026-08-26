# TAGLINE

带彩色图表的磁盘使用量显示工具

# TLDR

**显示磁盘使用情况**并附彩色图表条

```dfc```

**显示所有文件系统**，包括伪文件系统和特殊文件系统

```dfc -a```

**以指定单位显示**（K、M、G、T、P、E、Z、Y）

```dfc -u [G]```

**只显示特定文件系统类型**

```dfc -t [ext4,btrfs]```

**以 CSV 格式导出**

```dfc -e csv```

**按文件系统名称排序输出**

```dfc -q [name]```

**显示已用空间**和挂载选项

```dfc -d -o```

**不使用颜色显示**

```dfc -c never```

# SYNOPSIS

**dfc** [_-abdfhilmMnosTvwW_] [_-c when_] [_-e format_] [_-p fsname_] [_-q sortby_] [_-t fstype_] [_-u unit_]

# PARAMETERS

**-a**
> 显示所有文件系统（不做任何省略）。

**-b**
> 不显示图表条。

**-c** _when_
> 颜色模式：always、auto 或 never。

**-d**
> 显示已用空间。

**-e** _format_
> 导出为指定格式：csv、html、json、tex 或 text。

**-f**
> 覆盖自动调整行为，强制显示信息。

**-h**
> 显示帮助。

**-i**
> 显示 inode 信息而不是磁盘空间。

**-l**
> 只显示本地文件系统。

**-m**
> 使用 SI 单位（以 1000 为底数而不是 1024）。

**-M**
> 不输出"挂载于"一列。

**-n**
> 不输出表头。

**-o**
> 显示挂载选项。

**-p** _fsname_
> 按文件系统名称过滤（加 - 前缀表示排除）。

**-q** _sortby_
> 排序依据：name、type 或 mount。

**-s**
> 汇总总使用量。

**-t** _fstype_
> 按文件系统类型过滤（逗号分隔，加 - 前缀表示排除）。

**-T**
> 显示文件系统类型。

**-u** _unit_
> 强制指定显示单位（h、b、k、m、g、t、p、e、z、y）。

**-w**
> 图表使用更宽的条形。

**-W**
> 宽路径名（避免挂载点被截断）。

# DESCRIPTION

**dfc**（disk free color）是增强版的 df 命令，以彩色条形图展示文件系统的磁盘空间使用情况。它比传统的 df 输出更直观、更易读。

图表条会根据使用率变色：通常绿色表示低占用，黄色表示中等，红色表示高占用。这种可视化方式让人一眼就能发现接近满载的文件系统。

输出可以通过选择列、排序和过滤进行大量定制。该工具支持 CSV、JSON、HTML 等多种导出格式，便于与其他工具或报表系统集成。按文件系统类型过滤则可聚焦特定存储类型。

配置选项可以写入 **~/.config/dfc/dfcrc** 或 **/etc/dfc.conf** 以保存偏好。颜色阈值和图表字符都可以在配置文件中自定义。

# CAVEATS

颜色需要支持色彩的终端。默认模式下过长的挂载点名可能被截断（用 -W 显示完整路径）。某些虚拟文件系统可能显示出意外的数值。图表宽度会自适应终端宽度。

# HISTORY

**dfc** 由 Robin Hahling 创建，作为传统 df 命令的彩色易用替代品。该项目专注于让磁盘空间监控更可视化、更易用。它用 C 语言编写，可在多数主流 Linux 发行版的软件仓库中获取。

# INSTALL

```apt: sudo apt install dfc```

```dnf: sudo dnf install dfc```

```pacman: sudo pacman -S dfc```

```apk: sudo apk add dfc```

```zypper: sudo zypper install dfc```

```brew: brew install dfc```

```nix: nix profile install nixpkgs#dfc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[df](/man/df)(1), [du](/man/du)(1), [ncdu](/man/ncdu)(1), [dust](/man/dust)(1), [duf](/man/duf)(1)

# RESOURCES

```[Source code](https://github.com/rolinh/dfc)```

<!-- verified: 2026-07-11 -->
