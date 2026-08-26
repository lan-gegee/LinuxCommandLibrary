# TAGLINE

输入设备事件监视与拦截器

# TLDR

以**配置**文件启动

```udevmon -c [path/to/config.yaml]```

# SYNOPSIS

**udevmon** [_OPTIONS_]

# PARAMETERS

**-c** _FILE_
> 使用指定的配置文件

# DESCRIPTION

**udevmon** 拦截并监视输入设备以启动任务。它根据配置文件过滤或修改输入事件，配置文件通常位于 /etc/interception/udevmon.d/*.yaml。

该工具是 Interception Tools 套件的一部分，支持在底层进行高级的键盘和鼠标事件处理，例如按键重映射。

# CAVEATS

需要 root 权限。配置文件必须是合法的 YAML。属于 Interception Tools 项目。运行不当可能会干扰输入设备。

# INSTALL

```apt: sudo apt install interception-tools```

```pacman: sudo pacman -S interception-tools```

```nix: nix profile install nixpkgs#interception-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uinput](/man/uinput)(1)
