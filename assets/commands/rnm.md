# TAGLINE

按模式批量重命名文件

# TLDR

**在文件名中搜索并替换**

```rnm -ss [old] -rs [new] [directory]```

使用**字面**字符串（不用正则）

```rnm -ssf [old] -rs [new] [files]```

添加**自动递增**索引

```rnm -i 1 -inc 1 -rs [_] [files]```

从**名称列表**文件重命名

```rnm -ns/f [names.txt] [files]```

仅重命名**文件**（不含目录）

```rnm -fo -ss [pattern] -rs [replacement] [files]```

按**修改时间**排序

```rnm -s/mt -ss [pattern] -rs [replacement] [files]```

**模拟**而不实际更改

```rnm -sim -ss [pattern] -rs [replacement] [files]```

**撤销**上一次操作

```rnm -u```

# SYNOPSIS

**rnm** [**-ss** _pattern_] [**-rs** _replacement_] [**-sim**] [**-fo**] [_files_...]

# PARAMETERS

**-ss _pattern_**
> 搜索字符串/正则表达式。

**-ssf _string_**
> 固定（字面）搜索字符串。

**-rs _replacement_**
> 替换字符串。

**-i _start_**
> 编号起始索引。

**-inc _step_**
> 索引递增值。

**-ns/f _file_**
> 名称列表文件。

**-fo**
> 仅文件（忽略目录）。

**-sim**
> 模拟模式（试运行）。

**-u**
> 撤销上一次操作。

**-s/mt**
> 按修改时间排序。

# DESCRIPTION

**rnm** 是一款功能强大的批量重命名工具，支持正则表达式、编号和名称列表文件。它可以基于模式重命名文件、添加顺序编号，或使用预定义的名称列表。

该工具包含用于预览更改的模拟模式和用于撤销误操作的撤销功能。它能以细粒度控制处理复杂的重命名场景。

# CAVEATS

默认为正则模式；字面字符串请用 -ssf。撤销只对最近一次操作有效。处理重要文件前先用 -sim 测试。

# HISTORY

**rnm** 由 **Md Jahidul Hamid**（neurobin）创建，是一个功能全面的批量重命名解决方案，补足了较简单的 rename 工具所缺少的特性。

# INSTALL

```nix: nix profile install nixpkgs#rnm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mmv](/man/mmv)(1), [prename](/man/prename)(1)
