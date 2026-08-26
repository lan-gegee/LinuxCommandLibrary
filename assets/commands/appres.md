# TAGLINE

显示 X 应用程序的资源配置

# TLDR

**按类名查看**应用程序的资源

```appres [XTerm]```

同时指定**类名与实例名**查看资源

```appres [XTerm] [xterm]```

通过过滤输出查看**特定资源**

```appres [Emacs] | grep [font]```

查看**特定 widget 路径**的资源

```appres [XTerm] [xterm] -xrm "*VT100*"```

# SYNOPSIS

**appres** [_class_ [_instance_]] [**-xrm** _resourcestring_]

# DESCRIPTION

**appres** 显示 X 应用程序的资源。它查询 X Resource Manager 数据库，并根据类名和实例名显示会应用到指定应用程序的资源。

这对于调试 X11 应用程序的外观和行为、了解哪些资源正在生效很有用。

# PARAMETERS

**class**
> 应用程序类名（通常首字母大写）

**instance**
> 应用程序实例名（通常为小写）

**-xrm** _resourcestring_
> 添加额外的资源字符串用于匹配

# CAVEATS

仅适用于使用 Xlib 资源的 X11 应用程序。现代工具包应用（GTK、Qt）可能不使用 X 资源。输出取决于 .Xresources 或 .Xdefaults 中定义的资源。

# HISTORY

**appres** 是标准的 X11 工具，自 **1989** 年 X11R4 发布以来一直是 X Window System 的一部分。

# INSTALL

```apt: sudo apt install x11-utils```

```dnf: sudo dnf install appres```

```zypper: sudo zypper install appres```

```nix: nix profile install nixpkgs#appres```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[xrdb](/man/xrdb)(1), [xprop](/man/xprop)(1)
