# TAGLINE

GNOME 下拉式终端，可快速呼出终端

# TLDR

**切换** Guake 的显示与隐藏

```F12```

切换**全屏**模式

```F11```

打开**新标签页**

```Ctrl+Shift+T```

**关闭**终端

```Super+X```

转到**上一个标签页**

```Ctrl+PageUp```

在浏览器中**搜索**选中文本

```Ctrl+Shift+L```

# SYNOPSIS

**guake** [_options_] [_path_]

# PARAMETERS

**-t**, **--toggle-visibility**
> 从命令行切换显示与隐藏。

**-n**, **--new-tab** _DIR_
> 添加新标签页，可选将工作目录设为 DIR。

**-s**, **--select-tab** _INDEX_
> 按索引选择标签页。

**-e**, **--execute-command** _CMD_
> 在新标签页中执行任意命令。

**-r**, **--rename-current-tab** _TITLE_
> 重命名当前标签页。TITLE 为 "-" 时重置为默认名称。

**-p**, **--preferences**
> 显示 Guake 首选项窗口。

**-f**, **--fullscreen**
> 将 Guake 置于全屏模式。

**--show**, **--hide**
> 强制显示或隐藏主窗口。

**-V**, **--version**
> 显示 Guake 版本号并退出。

**-q**, **--quit**
> 退出 Guake。

# DESCRIPTION

**guake** 是一款 GNOME 下拉式终端，按下热键（默认 F12）即可快速呼出终端。终端像平视显示器一样从屏幕顶部滑下，其灵感来自 Quake 游戏中的控制台。

特性包括多标签界面、透明度、自定义颜色，以及在切换操作间保持会话持久。终端常驻内存，可以即时呼出。

可以通过首选项对话框或 gsettings 进行配置。

# KEYBOARD SHORTCUTS

**F12** - 切换显示与隐藏
**F11** - 切换全屏
**Ctrl+Shift+T** - 新建标签页
**Ctrl+Shift+W** - 关闭标签页
**Ctrl+PageUp/PageDown** - 在标签页之间导航

# CAVEATS

在启用桌面合成时效果最佳。在某些窗口管理器上可能有问题。与使用 F12 的其他应用冲突。需要 GTK 和 VTE 库。

# HISTORY

guake 由 **Gabriel Falcão** 于 **2007 年**创建，最初托管在 SourceForge 上，其灵感来自 id Software 的 Quake 游戏中的下拉控制台以及 Yakuake（KDE）和 Tilda 等类似终端。此后项目迁移至 GitHub，由社区贡献者维护。

# INSTALL

```dnf: sudo dnf install guake```

```pacman: sudo pacman -S guake```

```zypper: sudo zypper install guake```

```nix: nix profile install nixpkgs#guake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yakuake](/man/yakuake)(1), [tilda](/man/tilda)(1), [gnome-terminal](/man/gnome-terminal)(1)

# RESOURCES

```[Homepage](https://guake.github.io/)```

```[Source code](https://github.com/Guake/guake)```

```[Documentation](https://guake.readthedocs.io/en/latest/)```

<!-- verified: 2026-07-17 -->
