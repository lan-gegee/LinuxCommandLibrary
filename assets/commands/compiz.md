# TAGLINE

带 3D 特效的复合窗口管理器

# TLDR

**启动 Compiz 窗口管理器**

```compiz```

**加载指定的插件启动**

```compiz --replace [cube] [rotate] [wobbly]```

**替换当前的窗口管理器**

```compiz --replace```

**以 OpenGL 回退模式启动**

```compiz --indirect-rendering```

**运行 Compiz 配置管理器**

```ccsm```

# SYNOPSIS

**compiz** [**--replace**] [_options_] [_plugins_]

# PARAMETERS

**--replace**
> 替换当前正在运行的窗口管理器。

**--indirect-rendering**
> 使用间接 OpenGL 渲染（为了兼容性）。

**--loose-binding**
> 使用松散纹理绑定。

**--sm-disable**
> 禁用会话管理。

**--no-fbo**
> 禁用帧缓冲对象。

**--display** _display_
> 要使用的 X display。

**--debug**
> 启用调试输出。

# CONFIGURATION

**~/.config/compiz-1/compizconfig/Default.ini**
> 用户级 Compiz 设置及已启用的插件。

**/etc/compizconfig/config**
> 系统级 Compiz 配置。

# POPULAR PLUGINS

**cube**: 桌面立方体特效
**rotate**: 旋转桌面立方体
**expo**: 类似 Expose 的工作区视图
**wobbly**: 果冻窗口特效
**scale**: 窗口选择器/缩放排列
**shift**: 窗口切换器特效
**animation**: 窗口打开/关闭动画
**wall**: 桌面墙面导航
**ring**: 环形窗口切换器

# DESCRIPTION

**Compiz** 是 X11 上的复合窗口管理器，使用 OpenGL 进行渲染，可实现透明、阴影、动画以及著名的桌面立方体等高级视觉效果。它采用插件架构，支持高度定制。

Compiz 替换标准窗口管理器（如 Metacity 或 Mutter），负责窗口装饰、定位和特效。**ccsm**（CompizConfig Settings Manager）提供了配置插件和特效的图形界面。

该窗口管理器可与桌面环境集成，尤其是 GNOME 和 KDE，在保持标准窗口管理功能的同时提供增强的视觉反馈。

# CAVEATS

需要支持 OpenGL 的显卡驱动程序。部分特效非常消耗资源，在旧硬件上可能影响性能。与某些应用程序可能存在兼容性问题，尤其是使用自定义渲染的程序。如今已在很大程度上被现代桌面环境内置的合成器取代。

# HISTORY

Compiz 由 Novell 的 **David Reveman** 创建，于 **2006 年**首次发布。它将此前只在 macOS 上才能见到的高级 3D 桌面特效带入 Linux。桌面立方体和果冻窗口成为 Linux 桌面的标志性特性。开发曾分裂为 Compiz 和 Compiz Fusion 两支，后来重新合并。随着 GNOME Shell 和 KWin 引入原生合成功能，人们对它的兴趣逐渐减退，但 Compiz 至今仍然可用。

# INSTALL

```apt: sudo apt install compiz-core```

```dnf: sudo dnf install compiz```

```zypper: sudo zypper install compiz```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mutter](/man/mutter)(1), [kwin](/man/kwin)(1), [openbox](/man/openbox)(1), [picom](/man/picom)(1)
