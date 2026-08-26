# TAGLINE

移除 Mageia Linux 中的软件仓库

# TLDR

**移除**一个介质

```sudo urpmi.removemedia [medium]```

移除**全部**介质

```sudo urpmi.removemedia -a```

用**模糊**匹配移除

```sudo urpmi.removemedia -y [keyword]```

# SYNOPSIS

**urpmi.removemedia** [_OPTIONS_] [_MEDIUM_...]

# PARAMETERS

**-a**
> 移除所有介质

**-y**
> 对介质名称进行模糊匹配

# DESCRIPTION

**urpmi.removemedia** 从 Mageia Linux 的配置中移除软件仓库（介质）。可以按确切的名称移除、按模糊匹配移除，也可以一次性全部移除。

在 Mageia 文档中，"medium"（介质）与"repository"（仓库）是同义词。

# CAVEATS

Mageia 专用。移除所有介质后将不再有任何软件源。需要 root 权限。

# SEE ALSO

[urpmi](/man/urpmi)(8), [urpmi.addmedia](/man/urpmi.addmedia)(8), [urpmi.update](/man/urpmi.update)(8)
