# TAGLINE

X11 动态菜单

# TLDR

从 **ls 输出**显示菜单

```ls | dmenu```

以**自定义选项**显示菜单

```echo -e "[red]\n[green]\n[blue]" | dmenu```

将选中项**保存**到文件

```echo -e "[red]\n[green]\n[blue]" | dmenu > [color.txt]```

在**指定显示器**上启动

```ls | dmenu -m [1]```

显示在屏幕**底部**

```ls | dmenu -b```

# SYNOPSIS

**dmenu** [_options_]

# DESCRIPTION

**dmenu** 是 X11 下的动态菜单工具。它从 stdin 读取选项，以水平菜单形式显示，并将选中的项输出到 stdout。

它常被用作应用启动器、文件选择器或平铺式窗口管理器中的通用选择界面。

# PARAMETERS

**-b**
> 显示在屏幕底部

**-m** _monitor_
> 显示在指定显示器上

**-l** _lines_
> 显示为 n 行的垂直列表

**-p** _prompt_
> 显示提示文本

**-fn** _font_
> 字体或字体模式

**-nb** _color_
> 普通状态背景色

**-nf** _color_
> 普通状态前景色

**-sb** _color_
> 选中状态背景色

**-sf** _color_
> 选中状态前景色

# CAVEATS

仅支持 X11（Wayland 请使用 bemenu）。选项必须以换行符分隔。属于 suckless 工具集。可通过补丁高度定制。

# INSTALL

```apt: sudo apt install suckless-tools```

```dnf: sudo dnf install dmenu```

```pacman: sudo pacman -S dmenu```

```apk: sudo apk add dmenu```

```zypper: sudo zypper install dmenu```

```brew: brew install dmenu```

```nix: nix profile install nixpkgs#dmenu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rofi](/man/rofi)(1), [bemenu](/man/bemenu)(1), [fzf](/man/fzf)(1)

# RESOURCES

```[Source code](https://git.suckless.org/dmenu/)```

```[Homepage](https://tools.suckless.org/dmenu/)```

<!-- verified: 2026-07-11 -->
