# TAGLINE

动态平铺窗口管理器

# TLDR

**启动 dwm**（通过 xinitrc）

```exec dwm```

**设置 dwm 状态栏**文本

```xsetroot -name "[status text]"```

**原地重启 dwm**

```kill -HUP $(pidof dwm)```

# SYNOPSIS

**dwm**

# DESCRIPTION

**dwm**（dynamic window manager）是一个极简的 X11 平铺窗口管理器。它以平铺、独占（monocle）和浮动布局管理窗口，操作以键盘驱动且资源占用极少。

窗口按标签组织（类似于工作区）。主/堆栈布局会将主窗口突出显示，其余窗口在其旁边堆叠。配置需要编辑 C 源码并重新编译。

dwm 设计得极其小巧（少于 2000 行代码）而快速，遵循 suckless 的简洁高效哲学。

# DEFAULT KEYBINDINGS

**Mod1-Shift-Enter** - 打开终端
**Mod1-p** - 启动 dmenu
**Mod1-j** / **Mod1-k** - 聚焦下一个/上一个窗口
**Mod1-h** / **Mod1-l** - 调整主区域大小
**Mod1-Enter** - 将聚焦窗口提升为主窗口
**Mod1-t** - 平铺布局
**Mod1-f** - 浮动布局
**Mod1-m** - 独占布局
**Mod1-Shift-c** - 关闭聚焦窗口
**Mod1-Shift-q** - 退出 dwm
**Mod1-[1-9]** - 切换到标签 1-9
**Mod1-Shift-[1-9]** - 将窗口移到标签 1-9

# CONFIGURATION

**config.h**
> 源码级配置文件，必须编辑并重新编译才能更改键绑定、颜色、布局、状态栏设置、规则和行为。Mod1 默认为 Alt 键。

# CAVEATS

配置需要重新编译。键盘快捷键有一定学习曲线。没有内置配置文件。与浮动窗口管理器相比鼠标支持有限。

# HISTORY

dwm 由以 **Anselm R. Garbe** 为首的 **suckless.org** 社区创建，于 **2006 年**前后发布。它为许多其他平铺窗口管理器确立了模板，也奠定了 suckless 软件哲学。

# INSTALL

```apk: sudo apk add dwm```

```brew: brew install dwm```

```nix: nix profile install nixpkgs#dwm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmenu](/man/dmenu)(1), [st](/man/st)(1), [i3](/man/i3)(1), [awesome](/man/awesome)(1)
