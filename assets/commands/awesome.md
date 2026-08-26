# TAGLINE

高度可配置的 X11 平铺窗口管理器

# TLDR

**启动 awesome** 窗口管理器

```awesome```

以指定的配置文件**启动**

```awesome -c [~/.config/awesome/rc.lua]```

**检查配置**中的错误

```awesome -k```

**检查指定配置文件**中的错误

```awesome -k -c [path/to/rc.lua]```

**显示版本**信息

```awesome -v```

**替换正在运行的窗口管理器**

```awesome --replace```

# SYNOPSIS

**awesome** [**-v** | **--version**] [**-h** | **--help**] [**-c** | **--config** _FILE_] [**-k** | **--check**] [**-s** | **--search** _DIR_] [**-a** | **--no-argb**] [**-r** | **--replace**]

# PARAMETERS

**-v**, **--version**
> 显示版本信息并退出

**-h**, **--help**
> 显示帮助信息并退出

**-c** _FILE_, **--config** _FILE_
> 使用指定的 Lua 配置文件代替默认配置

**-k**, **--check**
> 检查配置文件的语法并退出

**-s**, **--search** _DIR_
> 将目录添加到 Lua 库搜索路径

**-a**, **--no-argb**
> 禁用 ARGB 视觉效果（透明）

**-r**, **--replace**
> 替换已存在的窗口管理器

# DESCRIPTION

**awesome** 是一款高度可配置的 X11 平铺窗口管理器。它以平铺、浮动等多种布局管理窗口，为键盘驱动的工作流最大化屏幕空间利用率。

配置通过 Lua 编程语言编写在 **~/.config/awesome/rc.lua** 中完成，可深度自定义布局、按键绑定、组件和外观。默认配置提供了带有合理默认值、开箱即用的起点。

关键概念包括 tag（虚拟桌面）、layout（平铺算法）和 widget（状态栏组件）。Mod4 键（通常是 Windows/Super 键）是按键绑定的默认修饰键。

默认按键绑定包括：
- **Mod4 + Enter**：打开终端
- **Mod4 + r**：运行提示符
- **Mod4 + j/k**：聚焦下一个/上一个客户端
- **Mod4 + Shift + c**：关闭当前聚焦的客户端
- **Mod4 + Space**：循环切换布局
- **Mod4 + 1-9**：切换到对应 tag

该窗口管理器内置菜单、通知系统以及显示系统信息的状态栏。

# CONFIGURATION

**~/.config/awesome/rc.lua**
> 用 Lua 编写的主配置文件。控制布局、按键绑定、组件、主题以及窗口管理器的所有行为。

# CAVEATS

需要 X11；不支持 Wayland。rc.lua 中的配置错误会导致 awesome 回退到默认配置。某些功能需要合成器才能实现透明效果。对新手而言，Lua 配置的学习曲线可能较陡峭。

# HISTORY

**awesome** 由 **Julien Danjou** 创建，于 **2007** 年首次发布。它被设计为 dwm 的继任者，通过 Lua 脚本获得了更强的可扩展性。其名字是对"awesome（了不起）"而非仅仅"good（不错）"的俏皮呼应。项目仍在活跃开发中，重点是稳定性和可定制性。

# INSTALL

```apt: sudo apt install awesome```

```dnf: sudo dnf install awesome```

```pacman: sudo pacman -S awesome```

```apk: sudo apk add awesome```

```zypper: sudo zypper install awesome```

```nix: nix profile install nixpkgs#awesome```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[i3](/man/i3)(1), [dwm](/man/dwm)(1), [bspwm](/man/bspwm)(1), [lua](/man/lua)(1)
