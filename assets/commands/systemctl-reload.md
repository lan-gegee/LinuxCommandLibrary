# TAGLINE

重新加载服务配置而不重启

# TLDR

**重新加载**服务的配置

```systemctl reload nginx```

重新加载**多个**服务

```systemctl reload [unit1] [unit2]```

为**当前用户**重载一个服务

```systemctl reload pipewire --user```

# SYNOPSIS

**systemctl** [_OPTIONS_...] **reload** _PATTERN_...

# PARAMETERS

**--user**
> 重载用户服务管理器的单元而不是系统单元

**--no-block**
> 不等待操作完成

# DESCRIPTION

**systemctl reload** 要求服务在不停止的情况下重新加载其配置文件。这里重载的是服务应用程序自身的配置（如 nginx.conf 或 apache 的 httpd.conf），而不是 systemd 单元文件。

服务必须支持重载操作（通常通过 SIGHUP 信号实现）。如果服务不支持重载，该命令会失败。对于不支持重载的服务，请改用 **systemctl restart**。

# CAVEATS

并非所有服务都支持重载；请查阅相应服务的文档。此处重载的是**服务自身的**配置，而非 systemd 单元文件。要重载单元文件，请使用 **systemctl daemon-reload**。如果重载失败，服务会继续使用旧配置运行。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [systemctl-restart](/man/systemctl-restart)(1), [systemctl-daemon-reload](/man/systemctl-daemon-reload)(1)
