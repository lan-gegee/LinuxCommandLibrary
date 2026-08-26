# TAGLINE

检测 Debian 安装器的系统架构

# TLDR

**检测**系统架构

```archdetect```

# SYNOPSIS

**archdetect** [**-g**]

# PARAMETERS

**-g**
> 猜测一个可能与本机兼容的通用子架构，对尚未被识别的新子架构很有用。

# DESCRIPTION

**archdetect** 以 Debian 安装器使用的格式显示当前机器的架构和子架构。架构与 dpkg 内置的架构一致，描述 CPU（以及可能的内核）类型。子架构用于区分启动方式不同的机器。

它主要供 Debian 安装器用于确定要安装哪个内核和哪些软件包。

# OUTPUT FORMAT

```
architecture/subarchitecture
```

示例：
- amd64/generic
- i386/686
- arm64/generic

# CAVEATS

仅适用于基于 Debian 的系统。输出格式面向安装器使用，不适合一般性的系统识别。并非所有发行版都提供该工具。

# HISTORY

**archdetect** 为 Debian 安装器而开发，用于在各安装介质间统一架构检测方式。

# SEE ALSO

[arch](/man/arch)(1), [uname](/man/uname)(1), [dpkg](/man/dpkg)(1)
