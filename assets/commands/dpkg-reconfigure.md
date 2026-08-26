# TAGLINE

重新配置已安装的 Debian 软件包

# TLDR

**重新配置**软件包

```dpkg-reconfigure [package1] [package2]```

重新配置**控制台字体**设置

```dpkg-reconfigure console-setup```

重新配置**时区**

```dpkg-reconfigure tzdata```

# SYNOPSIS

**dpkg-reconfigure** [_options_] _packages_

# DESCRIPTION

**dpkg-reconfigure** 在基于 Debian 的系统上重新配置已安装的软件包。它会再次运行软件包的安装后配置脚本，呈现与初次安装时相同的提问，让你可以修改之前配置过的选项。

该工具通过 debconf 系统管理配置问题和答案。对于那些难以手动修改的系统设置——如 locale、键盘布局、时区和显示管理器配置——它尤其有用。

不同的前端（dialog、readline、noninteractive）控制问题的呈现方式，使其既适合交互式终端会话，也适合自动化脚本。

# PARAMETERS

**-f, --frontend** _frontend_
> 使用指定的前端（dialog、readline、noninteractive）

**-p, --priority** _priority_
> 问题优先级（low、medium、high、critical）

**-a, --all**
> 重新配置所有软件包

**--default-priority**
> 使用默认优先级

# CAVEATS

仅适用于 Debian/Ubuntu。并非所有软件包都支持重新配置。某些重新配置操作需要 root 权限。

# INSTALL

```apt: sudo apt install dpkg```

```dnf: sudo dnf install dpkg```

```pacman: sudo pacman -S dpkg```

```apk: sudo apk add dpkg```

```zypper: sudo zypper install dpkg```

```brew: brew install dpkg```

```nix: nix profile install nixpkgs#dpkg```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dpkg](/man/dpkg)(1)
