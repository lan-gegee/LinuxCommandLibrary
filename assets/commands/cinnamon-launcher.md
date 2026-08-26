# TAGLINE

Cinnamon 内部的会话与应用启动器

# TLDR

**启动或重启 Cinnamon 会话**

```cinnamon-launcher```

# SYNOPSIS

**cinnamon-launcher**

# DESCRIPTION

**cinnamon-launcher** 是 Cinnamon 桌面环境的内部实用程序，用于启动或重启 Cinnamon 会话以及启动应用程序。

该命令处理 **.desktop** 文件，并为 Cinnamon Shell 处理应用程序启动事宜，管理环境变量、工作目录，确保应用在图形会话中正确启动。

它与 Cinnamon 的各组件深度集成，包括应用程序菜单、面板启动器和 Nemo 文件管理器，为整个桌面环境中启动进程提供一致的接口。

# CAVEATS

此工具主要供 Cinnamon 桌面环境内部使用，用户通常不会从命令行直接调用它。

# INSTALL

```apt: sudo apt install cinnamon```

```dnf: sudo dnf install cinnamon```

```pacman: sudo pacman -S cinnamon```

```zypper: sudo zypper install cinnamon```

```nix: nix profile install nixpkgs#cinnamon```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cinnamon](/man/cinnamon)(1)
