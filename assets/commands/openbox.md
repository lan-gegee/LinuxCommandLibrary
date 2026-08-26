# TAGLINE

轻量级、高度可配置的窗口管理器

# TLDR

**启动 Openbox**

```openbox```

**作为会话管理器启动**

```openbox-session```

**无需重启即重新加载配置**

```openbox --reconfigure```

**重启 Openbox**

```openbox --restart```

**退出 Openbox**

```openbox --exit```

**替换当前运行的窗口管理器**

```openbox --replace```

# SYNOPSIS

**openbox** [_options_]

# PARAMETERS

**--reconfigure**
> 重新加载配置。

**--restart**
> 重启 Openbox。

**--replace**
> 替换正在运行的窗口管理器。

**--exit**
> 退出正在运行的 Openbox 实例。

**--config-file** _file_
> 指定要使用的配置文件路径。

**--sm-disable**
> 不连接会话管理器。

**--startup** _cmd_
> 启动后运行指定命令。

**--debug**
> 显示调试输出。

**--debug-focus**
> 显示焦点处理的调试输出。

**--version**
> 显示版本并退出。

**--help**
> 显示命令行选项摘要并退出。

# DESCRIPTION

**Openbox** 是一个轻量级、高度可配置的窗口管理器。它以极低的资源占用、对标准的良好遵循以及通过 XML 配置实现的广泛自定义能力而闻名。

Openbox 可以独立运行，也可以作为 LXDE 等桌面环境的窗口管理器。

# CONFIGURATION FILES

```
~/.config/openbox/
├── rc.xml        # Main config
├── menu.xml      # Right-click menu
├── autostart     # Startup applications
└── environment   # Environment variables
```

# KEY BINDINGS EXAMPLE

```xml
<!-- rc.xml -->
<keybind key="A-Tab">
  <action name="NextWindow"/>
</keybind>
```

# CAVEATS

没有内置面板或任务栏。需要手动配置。搭配面板（tint2、polybar）使用可获得完整的桌面体验。

# HISTORY

Openbox 最初是 Blackbox 的一个分支，由 **Dana Jansens** 自 **2002 年**起重写，旨在提供一个现代且符合标准的窗口管理器。

# INSTALL

```apt: sudo apt install openbox```

```dnf: sudo dnf install openbox```

```pacman: sudo pacman -S openbox```

```apk: sudo apk add openbox```

```zypper: sudo zypper install openbox```

```nix: nix profile install nixpkgs#openbox```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[i3](/man/i3)(1), [polybar](/man/polybar)(1), [feh](/man/feh)(1), [nitrogen](/man/nitrogen)(1)
