# TAGLINE

在 Vulkan 和 OpenGL 上显示实时监控叠加层

# TLDR

以 **HUD 叠加层**运行应用程序

```mangohud [command]```

# SYNOPSIS

**mangohud** [_options_] _command_

# DESCRIPTION

**mangohud** 在 Vulkan 和 OpenGL 应用程序上显示实时监控叠加层，展示 FPS、帧时间、CPU/GPU 占用率、温度以及其他性能指标。

# KEYBOARD SHORTCUTS

**RightShift+F11**
> 更改叠加层位置

**RightShift+F10**
> 更改叠加层详细程度

**RightShift+F12**
> 切换叠加层可见性

# CONFIGURATION

配置文件：~/.config/MangoHud/MangoHud.conf

环境变量：
**MANGOHUD=1**：为应用程序启用
**MANGOHUD_CONFIG**：覆盖配置路径

# CAVEATS

需要 Vulkan 或 OpenGL 应用程序。可能会轻微影响性能。如需持久设置，请通过配置文件进行配置。

# INSTALL

```apt: sudo apt install mangohud```

```dnf: sudo dnf install mangohud```

```pacman: sudo pacman -S mangohud```

```apk: sudo apk add mangohud```

```zypper: sudo zypper install mangohud```

```nix: nix profile install nixpkgs#mangohud```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvidia-smi](/man/nvidia-smi)(1), [glxinfo](/man/glxinfo)(1)
