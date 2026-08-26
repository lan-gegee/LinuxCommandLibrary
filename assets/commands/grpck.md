# TAGLINE

校验组文件的完整性

# TLDR

**检查组文件完整性**

```sudo grpck```

**只读模式**

```sudo grpck -r```

**按 GID 排序**

```sudo grpck -s```

**检查指定文件**

```sudo grpck [/etc/group] [/etc/gshadow]```

# SYNOPSIS

**grpck** [_options_] [_group_] [_shadow_]

# PARAMETERS

_GROUP_
> 要检查的组文件（默认 /etc/group）。

_SHADOW_
> 影子组文件（默认 /etc/gshadow）。

**-r**
> 只读模式，仅报告。

**-s**
> 按 GID 对条目排序。

**-R** _DIR_
> chroot 目录。

**--help**
> 显示帮助信息。

# DESCRIPTION

**grpck** 校验组信息文件的完整性。它检查重复条目、有效的字段格式，以及 /etc/group 与 /etc/gshadow 之间的一致性。

以交互方式运行时，该工具可以自动修复某些问题。它对维护系统安全和组的正常功能至关重要。

# CAVEATS

需要 root 权限。交互式修复需要确认。修复前请先备份文件。

# HISTORY

grpck 作为 **shadow** 密码工具套件的一部分开发，用于 Unix/Linux 系统管理。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pwck](/man/pwck)(8), [groups](/man/groups)(1), [gpasswd](/man/gpasswd)(1)

# RESOURCES

```[Source code](https://github.com/shadow-maint/shadow)```

<!-- verified: 2026-07-17 -->
