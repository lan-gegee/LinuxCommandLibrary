# TAGLINE

从 Koji 构建系统输出标签信息

# TLDR

**输出某个标签的信息**

```koji taginfo [tag]```

**输出多个标签的信息**

```koji taginfo [tag1] [tag2]```

**显示帮助**

```koji taginfo --help```

# SYNOPSIS

**koji taginfo** [_options_] _tag_ [_tag_...]

# DESCRIPTION

**koji taginfo** 从 Koji 构建系统输出一个或多个标签的基本信息，包括标签 ID、权限、架构、锁定状态、继承链以及关联的构建目标。这可用于检查 Fedora、CentOS 及其他基于 RPM 的发行版构建系统中标签的配置方式。

# PARAMETERS

**tag**
> 要查询的标签名称（可指定多个）。

**--event=**_EVENT_
> 在指定事件处查询（用于历史状态）。

**--user=**_USER_
> 在与给定用户会话对应的事件处查询。

**--inherit**
> 显示该标签的继承信息。

**-h**, **--help**
> 显示帮助信息。

# INSTALL

```dnf: sudo dnf install koji```

```brew: brew install koji```

```nix: nix profile install nixpkgs#koji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[koji](/man/koji)(1), [koji-tag-build](/man/koji-tag-build)(1)
