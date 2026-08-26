# TAGLINE

管理 X server 资源数据库

# TLDR

以交互模式**启动** xrdb

```xrdb```

从资源文件**加载**值

```xrdb -load [~/.Xresources]```

**查询**资源数据库并打印当前值

```xrdb -query```

# SYNOPSIS

**xrdb** [_options_] [_filename_]

# PARAMETERS

**-load**
> 从文件加载资源，替换现有值

**-merge**
> 将文件中的资源与现有值合并

**-query**
> 显示当前资源

**-remove**
> 移除所有资源

**-symbols**
> 打印预处理器符号

**-cpp _path_**
> 指定要使用的预处理器

**-nocpp**
> 不对输入做预处理

**-display _display_**
> 指定 X display

# DESCRIPTION

**xrdb**（X Resource DataBase）管理 X server 的资源数据库。X 资源用于配置 X 应用程序的外观和行为，包括颜色、字体和其他设置。

资源通常在 X 会话启动时从 **~/.Xresources** 或 **~/.Xdefaults** 加载。**-merge** 选项可在不移除现有资源的情况下添加新资源。

# CAVEATS

更改只影响新启动的应用程序。添加新设置时应使用 **-merge** 以保留现有设置。该文件默认由 cpp 处理，因此可以使用 #include 和 #define。属于 X.Org 工具集。

# HISTORY

**xrdb** 自 **20 世纪 80 年代中期**早期版本起就是 X Window System 的一部分，在现代桌面环境出现之前就提供了配置应用外观和行为的方式。

# INSTALL

```apt: sudo apt install x11-xserver-utils```

```dnf: sudo dnf install xrdb```

```apk: sudo apk add xrdb```

```zypper: sudo zypper install xrdb```

```brew: brew install xrdb```

```nix: nix profile install nixpkgs#xrdb```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xset](/man/xset)(1)
