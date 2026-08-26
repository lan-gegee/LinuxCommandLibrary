# TAGLINE

PipeWire 的会话与策略管理器

# TLDR

用 systemd **启用**

```systemctl --user --now enable wireplumber```

手动**运行**

```wireplumber```

使用自定义**配置**文件

```wireplumber --config-file [path/to/file]```

显示**帮助**

```wireplumber --help```

显示**版本**

```wireplumber --version```

# SYNOPSIS

**wireplumber** [_OPTIONS_]

# PARAMETERS

**-c**, **--config-file** _FILE_
> 使用指定的主配置文件而不是 `wireplumber.conf`。

**-n**, **--name** _NAME_
> 使用自定义守护进程名称（便于运行多个实例）。

**-d**, **--debug** _LEVEL_
> 设置日志级别（如 `D` 表示调试、`I` 表示信息、`W` 表示警告、`E` 表示错误），或使用 GLib 风格的 域:级别 规格。

**-v**, **--verbose**
> 提高日志详细程度（等价于 `--debug=D`）。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# DESCRIPTION

**wireplumber** 是 PipeWire 的模块化会话/策略管理器。它为 PipeWire 多媒体框架处理设备路由、音频策略决策和会话管理。

该工具提供基于 GObject 的高层库，封装了 PipeWire 的 API 以便更轻松地集成。

# CAVEATS

需要 PipeWire 正在运行。在现代系统上通常由 systemd 管理。配置基于 Lua。

# INSTALL

```apt: sudo apt install wireplumber```

```dnf: sudo dnf install wireplumber```

```pacman: sudo pacman -S wireplumber```

```apk: sudo apk add wireplumber```

```zypper: sudo zypper install wireplumber```

```brew: brew install wireplumber```

```nix: nix profile install nixpkgs#wireplumber```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[wpctl](/man/wpctl)(1), [pipewire](/man/pipewire)(1), [pw-cli](/man/pw-cli)(1)
