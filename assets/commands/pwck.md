# TAGLINE

校验密码文件完整性与一致性

# TLDR

**检查密码文件完整性**

```pwck```

**检查指定文件**

```pwck [/etc/passwd] [/etc/shadow]```

**只读检查**

```pwck -r```

**静默模式**

```pwck -q```

# SYNOPSIS

**pwck** [_options_] [_passwd_] [_shadow_]

# PARAMETERS

_PASSWD_
> 密码文件路径。

_SHADOW_
> shadow 文件路径。

**-r**
> 只读模式。

**-q**
> 静默输出。

**-s**
> 按 UID 排序。

# DESCRIPTION

**pwck** 通过检查格式是否正确、字段值是否有效以及内部一致性，来验证 **/etc/passwd** 和 **/etc/shadow** 文件的完整性。它能检测出诸如用户名重复、UID/GID 无效、主目录缺失，以及密码文件与 shadow 文件之间条目不匹配等问题。

默认情况下 pwck 会提示删除无效条目，而 **-r** 选项以只读模式运行，可在不做出更改的情况下进行审计。该命令是 **shadow-utils** 的一部分，通常由管理员在手动编辑密码文件后运行，或作为系统健康检查的一部分。

# CAVEATS

访问 shadow 文件需要 root 权限。系统管理工具。

# HISTORY

pwck 是用于密码文件校验的 **shadow-utils** 工具。

# INSTALL

```apt: sudo apt install passwd```

```pacman: sudo pacman -S shadow```

```apk: sudo apk add shadow```

```zypper: sudo zypper install shadow```

```nix: nix profile install nixpkgs#shadow```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[grpck](/man/grpck)(8), [passwd](/man/passwd)(1)
