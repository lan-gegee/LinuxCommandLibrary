# TAGLINE

创建系统用户和组

# TLDR

根据**所有配置文件**创建用户

```systemd-sysusers```

根据**指定文件**创建用户

```systemd-sysusers path/to/file.conf```

**试运行**（显示将要执行的操作）

```systemd-sysusers --dry-run```

显示所有**配置文件内容**

```systemd-sysusers --cat-config```

指定**根目录**

```systemd-sysusers --root=/mnt/system```

# SYNOPSIS

**systemd-sysusers** [_OPTIONS_...] [_CONFIGFILE_...]

# DESCRIPTION

**systemd-sysusers** 根据 /usr/lib/sysusers.d/ 和 /etc/sysusers.d/ 中的配置文件创建系统用户和组。它通常在系统启动或软件包安装期间被调用。

# PARAMETERS

**--dry-run**
> 打印将要执行的操作而不实际修改

**--cat-config**
> 显示所有配置文件的内容

**--root=PATH**
> 在备用的文件系统根目录上操作

**--image=PATH**
> 在磁盘镜像上操作

**--no-pager**
> 不将输出通过分页器显示

**-h, --help**
> 显示帮助消息

**--version**
> 显示版本信息

# CAVEATS

配置文件使用声明式格式来定义用户和组。由 systemd-sysusers 创建的用户通常是没有登录 Shell 的系统账户。已存在的用户不会被修改。

# HISTORY

**systemd-sysusers** 是 **systemd** 的一部分，实现声明式的系统用户/组创建，以确保各次安装之间的用户账户一致。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-tmpfiles](/man/systemd-tmpfiles)(8), [useradd](/man/useradd)(8)
