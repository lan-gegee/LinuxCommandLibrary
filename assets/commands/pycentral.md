# TAGLINE

已弃用的 Debian Python 模块管理器

# TLDR

**注册 Python 模块（已弃用）**

```pycentral [action] [package]```

# SYNOPSIS

**pycentral** _action_ [_options_]

# PARAMETERS

_ACTION_
> 要执行的操作。

# DESCRIPTION

**pycentral** 曾是 Debian 用于在多个 Python 解释器版本间管理 Python 模块安装的工具。它为包含 Python 代码的 Debian 软件包处理字节码编译和模块注册。

该工具已被弃用，由 **dh-python** 和 **pybuild** 取代，后者为基于 Debian 的系统提供了更现代、更易维护的 Python 打包方式。仍在使用 pycentral 的现有软件包应迁移到 dh-python。

# CAVEATS

已弃用。请改用 dh-python。

# HISTORY

pycentral 是用于 Python 模块管理的**已弃用 Debian** 工具。

# SEE ALSO

[pybuild](/man/pybuild)(1), [dh-python](/man/dh-python)(1)
