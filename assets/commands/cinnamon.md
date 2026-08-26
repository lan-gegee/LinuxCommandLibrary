# TAGLINE

传统风格的 Linux 桌面环境

# TLDR

**启动 Cinnamon** 桌面（通常通过显示管理器）

```cinnamon```

用 Cinnamon **替换**当前窗口管理器

```cinnamon --replace```

**替换**窗口管理器且不连接会话管理器

```cinnamon --replace --sm-disable```

**显示版本**信息

```cinnamon --version```

# SYNOPSIS

**cinnamon** [**--replace**] [**--sm-disable**] [**-d** _DISPLAY_] [**--screen** _SCREEN_]

# DESCRIPTION

**Cinnamon** 是一个 Linux 桌面环境，在提供传统用户体验的同时具备现代特性。它包括 Muffin 窗口管理器、面板、应用程序菜单、桌面图标和完善的设置框架。

cinnamon 命令通常由 **cinnamon-session** 在通过显示管理器登录时调用。在现有会话中直接运行可能引起冲突。

Cinnamon 支持通过小程序（applet，面板部件）、桌件（desklet，桌面部件）、扩展和主题进行大量定制。

# PARAMETERS

**--replace**
> 替换当前正在运行的窗口管理器

**-d**, **--display** _DISPLAY_
> 要使用的 X display

**--screen** _SCREEN_
> 要使用的 X screen

**--sm-disable**
> 禁用与会话管理器的连接

**--sm-client-id** _ID_
> 指定会话管理 ID

**--sm-save-file** _FILE_
> 从已保存的会话文件初始化会话

**--sync**
> 以同步方式执行 X 调用

**--version**
> 打印版本后退出

# CAVEATS

不要在现有的 Cinnamon 会话中直接运行 cinnamon，因为这会与正在运行的桌面产生冲突。桌面通常由 **cinnamon-session** 通过显示管理器启动。

Cinnamon 不支持更换其他窗口管理器；Muffin 是其运行不可或缺的部分。

# HISTORY

**Cinnamon** 由 **Linux Mint** 团队自 **2011** 年开始开发，是 GNOME 3 的 GNOME Shell 的一个分支。它的诞生是为了在 GNOME 3 转向差异巨大的界面范式之后提供更传统的桌面体验。窗口管理器 Muffin 在 1.2 版（2012 年 1 月）中从 GNOME 的 Mutter 分支而来。

# INSTALL

```apt: sudo apt install cinnamon```

```dnf: sudo dnf install cinnamon```

```pacman: sudo pacman -S cinnamon```

```zypper: sudo zypper install cinnamon```

```nix: nix profile install nixpkgs#cinnamon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[muffin](/man/muffin)(1), [nemo](/man/nemo)(1), [cinnamon-launcher](/man/cinnamon-launcher)(1)
