# TAGLINE

通过移除有害字符来净化文件名

# TLDR

**预览文件名变更**（安全模式，默认）

```notox [path/to/directory]```

**应用重命名**

```notox -d [path/to/directory]```

**以静默输出预览**

```notox -q [path/to/directory]```

**以 JSON 格式输出变更**

```notox --json [path/to/directory]```

# SYNOPSIS

**notox** [_options_] [_path_]

# PARAMETERS

**-d**, **--do**
> 执行重命名（默认仅预览）。

**-q**, **--quiet**
> 抑制详细输出。

**--json**
> 以 JSON 格式输出结果。

# DESCRIPTION

**notox** 是一个命令行工具，用于重命名目录中的文件，消除文件名中的问题字符，例如空格、特殊字符和非 ASCII 字符。默认情况下它以安全模式运行，只显示拟议的更改而不实际执行。

# CAVEATS

在应用之前总是会先预览变更。使用 **-d** 标志才会真正重命名文件。

# HISTORY

**notox** 由 **Its-Just-Nans** 创建，使用 **Rust** 编写。

# SEE ALSO

[detox](/man/detox)(1), [rename](/man/rename)(1)
