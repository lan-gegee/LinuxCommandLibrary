# TAGLINE

基于 dmenu 的设备挂载/卸载界面

# TLDR

**启动**挂载/卸载菜单

```udiskie-dmenu```

用 **rofi** 代替 dmenu

```udiskie-dmenu --rofi```

只**挂载**设备

```udiskie-dmenu mount```

只**卸载**设备

```udiskie-dmenu unmount```

显示**帮助**

```udiskie-dmenu --help```

# SYNOPSIS

**udiskie-dmenu** [_OPTIONS_]

# PARAMETERS

**mount**
> 只显示可挂载的设备。

**unmount**
> 只显示可卸载（已挂载）的设备。

**--rofi**
> 使用 rofi 而不是 dmenu。

**--help**
> 显示帮助信息。

# DESCRIPTION

**udiskie-dmenu** 为 udiskie 提供基于 dmenu 或 rofi 的前端，以交互方式挂载和卸载设备。它会列出可用设备的菜单，方便快速选择。

该工具可与以 dmenu 或 rofi 作为主要启动界面的平铺式窗口管理器集成。

# CAVEATS

需要已安装 udiskie 以及 dmenu 或 rofi。可用设备取决于已连接的硬件和 udiskie 配置。

# INSTALL

```dnf: sudo dnf install udiskie```

```pacman: sudo pacman -S udiskie```

```apk: sudo apk add udiskie```

```zypper: sudo zypper install udiskie```

```nix: nix profile install nixpkgs#udiskie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[udiskie](/man/udiskie)(1), [udisksctl](/man/udisksctl)(1), [dmenu](/man/dmenu)(1), [rofi](/man/rofi)(1)
