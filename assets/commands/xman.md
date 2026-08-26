# TAGLINE

图形化手册页查看器

# TLDR

**启动** xman

```xman```

打开**文件**

```xman -helpfile [filename]```

显示**两个**窗格

```xman -bothshown```

# SYNOPSIS

**xman** [_OPTIONS_]

# PARAMETERS

**-helpfile** _FILE_
> 使用指定的帮助文件代替默认值

**-bothshown**
> 同时显示目录窗格和手册页窗格

**-notopbox**
> 启动时不显示带有三个按钮的顶部菜单框

**-geometry** _WxH+X+Y_
> 设置顶部菜单窗口的大小和位置

**-pagesize** _WxH+X+Y_
> 设置手册页窗口的大小和位置

# DESCRIPTION

**xman** 是 X Window System 的手册页浏览器。它为 man 页面提供图形界面，并以目录形式按章节列出可用的页面。初始窗口刻意做得很小，因此可以在整个登录会话期间保持运行。按下 Control-S 会打开一个提示框，用于指定要显示的手册页。

**MANPATH** 环境变量控制手册页的搜索路径。

# HISTORY

**xman** 是最早的 X11 工具之一，为基于终端的 man 命令提供了 GUI 替代方案。

# CAVEATS

仅支持 X11。与现代替代品相比界面陈旧。搜索能力有限。

# INSTALL

```apt: sudo apt install x11-apps```

```zypper: sudo zypper install xman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [info](/man/info)(1), [yelp](/man/yelp)(1)
