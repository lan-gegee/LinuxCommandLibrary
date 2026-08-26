# TAGLINE

初始化基本系统设置

# TLDR

**操作**指定目录而非主机系统

```sudo systemd-firstboot --root [path/to/root_directory]```

**设置**系统键盘布局

```sudo systemd-firstboot --keymap [keymap]```

**设置**系统主机名

```sudo systemd-firstboot --hostname [hostname]```

**设置** root 用户的密码

```sudo systemd-firstboot --root-password [password]```

**交互式提示**用户输入某项设置

```sudo systemd-firstboot --prompt [setting]```

即使文件已存在也**强制**写入配置

```sudo systemd-firstboot --force```

**移除**所有已有的首次启动配置文件

```sudo systemd-firstboot --reset```

**移除** root 用户的密码

```sudo systemd-firstboot --delete-root-password```

# SYNOPSIS

**systemd-firstboot** [_options_]

# PARAMETERS

**--root _path_**
> 在指定的根目录上操作

**--hostname _name_**
> 设置系统主机名

**--keymap _map_**
> 设置键盘布局

**--timezone _tz_**
> 设置系统时区

**--locale _locale_**
> 设置系统区域设置

**--root-password _password_**
> 设置 root 密码

**--root-shell _shell_**
> 设置 root 的登录 Shell

**--prompt**
> 交互式提示输入各项设置

**--force**
> 覆盖已有配置

**--reset**
> 移除所有首次启动配置文件

**--delete-root-password**
> 移除 root 密码

# DESCRIPTION

**systemd-firstboot** 在系统首次启动时或启动之前初始化基本系统设置。它通常用于准备操作系统镜像或系统安装。

该工具可以设置主机名、区域设置、时区、键盘布局和 root 密码。在没有选项的情况下于运行中的系统上执行时，它会交互式地提示未配置的设置项。

# CAVEATS

某些设置需要 **--force** 标志才能覆盖已有配置。在准备磁盘镜像时，**--root** 选项必不可少。密码应以安全的方式提供。本命令是 systemd 套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[localectl](/man/localectl)(1), [timedatectl](/man/timedatectl)(1), [hostnamectl](/man/hostnamectl)(1)
