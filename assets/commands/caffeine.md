# TAGLINE

在全屏应用运行时阻止空闲休眠

# TLDR

启动 **caffeine 服务器**

```caffeine```

显示**帮助**

```caffeine -h```

显示**版本**

```caffeine -V```

# SYNOPSIS

**caffeine** [_options_]

# DESCRIPTION

**caffeine** 在全屏应用运行时防止桌面进入空闲状态。它会监测全屏窗口，并在此期间自动抑制屏幕保护程序和挂起。

与手动抑制不同，caffeine 会根据窗口状态自动工作。

# PARAMETERS

**-h, --help**
> 显示帮助信息

**-V, --version**
> 显示版本信息

# INSTALL

```zypper: sudo zypper install caffeine```

```nix: nix profile install nixpkgs#caffeine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[caffeinate](/man/caffeinate)(1), [caffeine-indicator](/man/caffeine-indicator)(1), [xset](/man/xset)(1)

# RESOURCES

```[Homepage](https://launchpad.net/caffeine)```

<!-- verified: 2026-06-22 -->
