# TAGLINE

列出可用内存的范围及其在线状态

# TLDR

列出**内存信息**

```lsmem```

列出**所有独立的内存块**

```lsmem --all```

以 **JSON** 输出

```lsmem --json```

以**字节**显示大小

```lsmem --bytes```

只显示**汇总信息**

```lsmem --summary=only```

选择特定的**输出列**

```lsmem --output [RANGE,SIZE,STATE,REMOVABLE]```

# SYNOPSIS

**lsmem** [_options_]

# DESCRIPTION

**lsmem** 列出可用内存的范围及其在线状态。所列内存块与 sysfs 中的内存块表示相对应。该命令还会显示内存块大小以及处于在线和离线状态的内存量。属于 **util-linux**。

# PARAMETERS

**-J, --json**
> 以 JSON 格式输出

**-b, --bytes**
> 以字节为单位打印大小

**-o, --output COLUMNS**
> 指定输出的列

**-a, --all**
> 显示所有内存块

**-n, --noheadings**
> 不显示列标题

**-r, --raw**
> 原始输出，无格式化

**--summary** [_WHEN_]
> 控制汇总输出：never、always、only。

**-S, --split** _LIST_
> 用于拆分内存块的列：STATE、REMOVABLE、NODE、ZONES 或 none。

**-s, --sysroot** _DIR_
> 为另一个 Linux 实例收集内存数据。

**-P, --pairs**
> 生成 key="value" 形式的输出，适合 Shell `eval` 使用。

**-h, --help**, **-V, --version**
> 显示帮助或版本信息。

# CAVEATS

仅在 Linux 上可用。需要挂载 sysfs。显示的是内核视角的内存，而非物理 DIMM 信息。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[free](/man/free)(1), [chmem](/man/chmem)(8), [dmidecode](/man/dmidecode)(8)
