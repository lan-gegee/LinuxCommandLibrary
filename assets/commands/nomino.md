# TAGLINE

面向开发者的批量重命名工具

# TLDR

**使用正则表达式模式重命名文件**

```nomino -r "[regex]" "[output_pattern]"```

**预览更改而不实际重命名（测试模式）**

```nomino -t -r "[regex]" "[output_pattern]"```

**对文件排序并用递增编号重命名**

```nomino -s asc "[output_pattern]"```

**生成重命名映射的 JSON 文件**

```nomino -g [map.json] -r "[regex]" "[output_pattern]"```

**使用 JSON 映射文件进行重命名**

```nomino -m [map.json]```

**在指定目录中重命名**

```nomino -d [/path/to/dir] -r "[regex]" "[output_pattern]"```

# SYNOPSIS

**nomino** [_options_] [[_source_] _output_]...

# PARAMETERS

**-r**, **--regex** _PATTERN_
> 用于匹配文件名的正则表达式模式。

**-s**, **--sort** _ORDER_
> 按名称自然排序文件（asc 或 desc），并使用枚举器重命名。

**-m**, **--map** _PATH_
> 使用 JSON 映射文件来重命名文件。

**-g**, **--generate** _PATH_
> 重命名后保存一份 JSON 映射文件。

**-d**, **--dir** _PATH_
> 设置工作目录。

**-E**, **--no-extension**
> 在排序和正则模式下不保留文件扩展名。

**-k**, **--mkdir**
> 若输出路径的父目录缺失则递归创建。

**-p**, **--print**
> 将映射表打印到 stdout。

**-q**, **--quiet**
> 不将映射表打印到 stdout。

**-t**, **--test**
> 以测试模式运行，不实际重命名文件。

**-w**, **--overwrite**
> 覆盖输出文件。否则会在文件名前加上 '_'。

**--depth** _DEPTH_
> 覆盖正则模式下推断出的子目录深度。

**--max-depth** _DEPTH_
> 设置正则模式下的最大子目录深度。

# DESCRIPTION

**nomino** 是一款面向开发者的批量重命名工具。它支持基于正则表达式的模式匹配、自然排序、JSON 映射生成以及目录创建，用于记录和执行重命名操作。

在排序和正则模式下，文件扩展名默认会被保留，除非使用 **-E**。

# CAVEATS

执行前请务必用 **-t**（测试模式）预览更改。在排序和正则模式下，文件扩展名默认保留。若不使用 **-w**，已存在的输出文件不会被覆盖；而是会在文件名前加 '_'。

# HISTORY

**nomino** 由 **yaa110** 创建，使用 **Rust** 编写。

# INSTALL

```zypper: sudo zypper install nomino```

```brew: brew install nomino```

```nix: nix profile install nixpkgs#nomino```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mv](/man/mv)(1), [mmv](/man/mmv)(1)
