# TAGLINE

显示已安装软件包的元数据

# TLDR

**显示软件包信息**

```pip show [package]```

**显示多个软件包**

```pip show [package1] [package2]```

**显示并附带文件列表**

```pip show --files [package]```

# SYNOPSIS

**pip** **show** [_options_] _packages_...

# PARAMETERS

**-f**, **--files**
> 显示已安装的文件列表。

# DESCRIPTION

**pip show** 显示已安装软件包的元数据，包括名称、版本、简介、安装位置、依赖和要求。适用于检查软件包详情和依赖信息。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-list](/man/pip-list)(1), [pip-inspect](/man/pip-inspect)(1)
