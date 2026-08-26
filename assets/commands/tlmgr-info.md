# TAGLINE

显示 TeX Live 软件包信息

# TLDR

**显示软件包信息**

```tlmgr info [package]```

**列出所有软件包**

```tlmgr info --list```

**列出已安装的软件包**

```tlmgr info --only-installed```

**显示软件包的文件**

```tlmgr info --files [package]```

# SYNOPSIS

**tlmgr info** [_options_] [_package_...]

# PARAMETERS

**--list**
> 列出所有可用软件包。

**--only-installed**
> 仅显示已安装的软件包。

**--files**
> 显示软件包包含的文件。

**--data** _fields_
> 输出特定字段（name、category 等）。

**--json**
> 以 JSON 格式输出。

# DESCRIPTION

**tlmgr info** 显示 TeX Live 软件包的信息。包括描述、版本、大小和所含文件。TeX Live Manager 的组成部分。

# SEE ALSO

[tlmgr-search](/man/tlmgr-search)(1), [tlmgr](/man/tlmgr)(1)
