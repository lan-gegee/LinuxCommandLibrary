# TAGLINE

将一个变更拆分为多个变更

# TLDR

拆分当前变更

```jj split```

拆分特定修订

```jj split -r [rev]```

拆分特定文件

```jj split [file1] [file2]```

交互式拆分

```jj split -i```

# SYNOPSIS

**jj split** [_options_] [_paths_...]

# PARAMETERS

_PATHS_
> 要拆分到第一个变更中的文件。

**-r** _REV_
> 要拆分的修订。

**-i**, **--interactive**
> 交互式选择代码块（hunk）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj split** 将一个变更拆分为多个变更。它将修改分离成逻辑单元。

该命令支持交互式选择代码块。拆分出的变更共享原来的父修订。

# CAVEATS

jj 的子命令。从一个变创建两个变更。交互模式可用于精细控制。

# HISTORY

jj split 是 **Jujutsu** 的一部分，支持灵活的变更管理和历史改写。

# SEE ALSO

[jj](/man/jj)(1), [jj-squash](/man/jj-squash)(1), [jj-describe](/man/jj-describe)(1)
