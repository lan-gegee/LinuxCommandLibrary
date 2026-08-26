# TAGLINE

KDE Plasma 的停靠栏面板，可作为默认 Plasma 面板的替代品

# TLDR

**清除** QML 缓存

```latte-dock --clear-cache```

导入并加载**默认布局**

```latte-dock --default-layout```

加载**特定布局**

```latte-dock --layout [layout_name]```

从文件**导入**并加载布局

```latte-dock --import-layout [path/to/file]```

# SYNOPSIS

**latte-dock** [_options_]

# PARAMETERS

**--clear-cache**
> 清除 QML 缓存

**--default-layout**
> 导入并加载默认布局

**--layout** _NAME_
> 按名称加载特定布局

**--import-layout** _FILE_
> 从文件导入并加载布局

**--available-layouts**
> 列出可用布局

**--replace**
> 替换已经在运行的 Latte Dock 实例

# DESCRIPTION

**latte-dock** 是 KDE Plasma 的一个停靠栏面板，为默认 Plasma 面板提供了另一种选择。它提供类似 macOS 的停靠栏功能，配有动画、小部件（applet）和可自定义的布局。

可以保存多个布局并在它们之间切换，从而为不同的活动或工作流使用不同的配置。Latte 与 Plasma 的全局主题和部件相集成。

# CAVEATS

需要 KDE Plasma 桌面环境。Latte Dock 的开发已经正式结束。维护者宣布该项目不再处于活跃开发状态，预计与较新的 Plasma 版本（尤其是 Plasma 6）会存在兼容性问题。建议用户迁移到 Plasma 内置的面板功能。

# HISTORY

Latte Dock 最初是为了给 KDE Plasma 提供一个更精致的替代停靠栏而创建的，具有流畅的动画和灵活的自定义能力。它作为 macOS 风格的停靠栏替代品在 KDE 社区广受欢迎。后来该项目被其维护者正式停止维护。

# INSTALL

```aur: yay -S latte-dock```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[plasmashell](/man/plasmashell)(1)
