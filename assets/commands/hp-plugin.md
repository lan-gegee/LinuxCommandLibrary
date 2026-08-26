# TAGLINE

安装 HP 专有插件

# TLDR

**安装插件**

```sudo hp-plugin```

**交互式安装**

```sudo hp-plugin -i```

**自动安装**

```sudo hp-plugin -a```

**仅下载**

```hp-plugin -d```

# SYNOPSIS

**hp-plugin** [_options_]

# PARAMETERS

**-i**, **--interactive**
> 交互模式。

**-a**, **--auto**
> 自动模式。

**-d**, **--download-only**
> 只下载不安装。

**-p** _PATH_
> 插件文件路径。

**--force**
> 强制重新安装。

**--help**
> 显示帮助信息。

# DESCRIPTION

**hp-plugin** 安装 HP 专有插件。某些 HP 打印机需要这个二进制插件才能实现扫描等完整功能。

该工具会下载并安装插件包。必须以 root 身份运行，并且需要网络连接。

# CAVEATS

需要 root 权限。从 HP 服务器下载。某些国家/地区可能存在限制。

# HISTORY

hp-plugin 是 **HPLIP** 的一部分，用于安装特定 HP 设备所需的专有组件。

# INSTALL

```apt: sudo apt install hplip```

```dnf: sudo dnf install hplip```

```pacman: sudo pacman -S hplip```

```zypper: sudo zypper install hplip```

```nix: nix profile install nixpkgs#hplip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hp-setup](/man/hp-setup)(1), [hp-check](/man/hp-check)(1)
