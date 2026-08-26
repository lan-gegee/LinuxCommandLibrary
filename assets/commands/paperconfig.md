# TAGLINE

设置系统纸张尺寸

# TLDR

**设置默认纸张尺寸**

```paperconfig -p [a4]```

**设置为 letter 尺寸**

```paperconfig -p letter```

**交互式重新配置**（Debian/Ubuntu）

```dpkg-reconfigure libpaper1```

# SYNOPSIS

**paperconfig** [_options_]

# PARAMETERS

**-p** _PAPER_
> 设置纸张尺寸。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**paperconfig** 设置 libpaper 库所使用的系统级默认纸张尺寸（例如 a4、letter、legal）。查询 libpaper 的应用程序（如众多打印和 TeX 工具）会把该值用作默认值。

该工具会改写 **/etc/papersize**，写入所选的纸张名称。可用 **paperconf -a** 列出可用的纸张名称。

# CAVEATS

需要 root 权限。属于 libpaper。会影响打印相关的默认设置。

# HISTORY

paperconfig 是 **libpaper** 的组成部分，用于设置系统纸张尺寸。

# INSTALL

```apt: sudo apt install libpaper-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[paperconf](/man/paperconf)(1), [lp](/man/lp)(1)
