# TAGLINE

查找被覆盖的配置文件

# TLDR

显示**所有**被覆盖的配置文件

```systemd-delta```

只显示**特定类型**

```systemd-delta -t [masked|equivalent|redirected|overridden|extended|unchanged]```

显示特定**目录**中的覆盖情况

```systemd-delta [/etc|/run|/usr/lib]```

显示特定**类别**的覆盖情况

```systemd-delta [tmpfiles.d|sysctl.d|systemd/system]```

# SYNOPSIS

**systemd-delta** [_OPTIONS_] [_PREFIX_|_PREFIX/SUFFIX_|_SUFFIX_...]

# PARAMETERS

**-t, --type=** _TYPE_
> 按差异类型过滤（masked、equivalent、redirected、overridden、extended、unchanged）

**--diff=** _BOOL_
> 开关已修改文件的 diff 显示（默认：true）

**--no-pager**
> 不对输出分页

**-h, --help**
> 显示帮助

# DESCRIPTION

**systemd-delta** 识别并比较覆盖其他配置文件的配置文件。它有助于理解跨系统目录的配置优先级。

优先级层级中 `/etc/` 最高，`/run/` 其次，`/usr/lib/` 最低。在更高优先级的目录中放置同名文件即可覆盖原文件。带 `.d` 后缀的 drop-in 目录可以扩展配置文件。

# DIFFERENCE TYPES

**masked** - 高优先级位置的文件完全隐藏低优先级文件（符号链接到 /dev/null）

**equivalent** - 多个位置的内容完全相同

**redirected** - 符号链接指向别处

**overridden** - 高优先级位置的文件取代了低优先级文件

**extended** - drop-in 文件对原始文件进行了扩充

**unchanged** - 不存在覆盖

# CAVEATS

只显示 systemd 管理的配置类型（单元文件、tmpfiles.d、sysctl.d 等）的差异。不会分析任意配置文件。对于深度定制的系统，diff 输出可能非常冗长。

# HISTORY

**systemd-delta** 是 **systemd** 项目的一部分。当多个来源提供重叠配置时，弄清哪些配置实际生效是常见的管理难题，此命令正是为此而生。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemd-analyze](/man/systemd-analyze)(1)
