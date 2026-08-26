# TAGLINE

用于蓝牙管理的终端用户界面

# TLDR

**启动蓝牙 TUI**

```bluetui```

**使用自定义配置文件启动**

```bluetui -c [/path/to/config.toml]```

**显示帮助**

```bluetui -h```

# SYNOPSIS

**bluetui** [_options_]

# PARAMETERS

**-c** _path_
> 使用自定义配置文件。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# KEYBOARD COMMANDS

**Tab** 或 **l**
> 切换到下一个区块。

**Shift+Tab** 或 **h**
> 切换到上一个区块。

**j**/**k** 或 **Down**/**Up**
> 浏览设备列表。

**Space** 或 **Enter**
> 连接/断开设备或与设备配对。

**s**
> 开始/停止扫描。

**t**
> 切换适配器电源。

**q**
> 退出。

# DESCRIPTION

**bluetui** 是一个用于管理蓝牙设备的终端用户界面。它提供了一种交互方式来扫描设备、配对、连接和管理蓝牙连接，而无需直接使用命令行工具 bluetoothctl。

该 TUI 显示适配器信息、可用设备、已配对设备和连接状态。它支持设备配对/取消配对、重命名、电源管理和可发现性设置。

# CONFIGURATION

**~/.config/bluetui/config.toml**
> 用于自定义键绑定和行为的配置文件。

# CAVEATS

需要蓝牙守护进程（bluetoothd）正在运行。可能需要相应的权限才能访问蓝牙适配器。使用 Rust 编写，基于 Ratatui 框架。

# INSTALL

```pacman: sudo pacman -S bluetui```

```zypper: sudo zypper install bluetui```

```nix: nix profile install nixpkgs#bluetui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bluetoothctl](/man/bluetoothctl)(1)
