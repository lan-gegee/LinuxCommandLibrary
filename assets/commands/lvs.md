# TAGLINE

显示逻辑卷的信息

# TLDR

**列出**逻辑卷

```sudo lvs```

**列出所有**卷，包括内部卷

```sudo lvs -a```

**详细**输出

```sudo lvs -v```

显示**指定的**字段

```sudo lvs -o lv_name,vg_name,lv_size```

向默认输出**追加**一个字段

```sudo lvs -o +lv_path```

**显示可用字段**

```sudo lvs -o help```

用于脚本化的**无表头**输出及自定义分隔符

```sudo lvs --noheadings --separator '|'```

按选择条件**过滤**逻辑卷

```sudo lvs -S 'lv_size>1g'```

**JSON 输出**

```sudo lvs --reportformat json```

# SYNOPSIS

**lvs** [_OPTIONS_] [_VolumeGroupName_|_LogicalVolume_...]

# DESCRIPTION

**lvs** 以可配置的表格格式显示逻辑卷的信息。它提供 LV 名称、大小、属性及相关卷组的快速概览。

# PARAMETERS

**-a**, **--all**
> 显示所有逻辑卷，包括内部卷。

**-v**, **--verbose**
> 提高详细程度并显示更多细节。最多可重复 4 次。

**-o**, **--options** _fields_
> 指定要显示的字段。前缀 `+` 表示追加，`-` 表示移除，`#` 表示压缩空字段。使用 `-o help` 可列出可用字段。

**-S**, **--select** _criteria_
> 过滤出符合选择条件的输出行。

**-O**, **--sort** _fields_
> 按指定字段排序输出。前缀 `-` 表示倒序。

**--noheadings**
> 抑制输出中的标题行。

**--nosuffix**
> 抑制输出中大小的单位后缀。

**--separator** _char_
> 使用指定字符作为字段分隔符。

**--aligned**
> 配合 --separator 使用，对齐输出的列。

**--nameprefixes**
> 为字段名添加 "LVM2_" 前缀，生成 field=value 形式的对。

**--segments**
> 在默认列中显示段信息。

**--rows**
> 将列显示为行。

**--units** _units_
> 以指定单位显示大小（b、s、k、m、g、t、p、e、h、H）。

**--reportformat** _format_
> 输出格式：`basic` 或 `json`。

# CAVEATS

部分字段需要在详细模式下才显示。默认输出面向人类可读性设计；脚本化请使用 `--separator` 和 `--noheadings`。需要 root 权限或属于相应的组。

# HISTORY

**lvs** 是 **LVM2**（Linux 逻辑卷管理器）的一部分，提供快速的卷列表功能。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [lvdisplay](/man/lvdisplay)(8), [lvcreate](/man/lvcreate)(8), [lvrename](/man/lvrename)(8), [pvs](/man/pvs)(8), [vgs](/man/vgs)(8)
