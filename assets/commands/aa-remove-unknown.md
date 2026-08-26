# TAGLINE

从内核中移除孤立的 AppArmor 配置文件

# TLDR

先执行**试运行**，查看哪些配置文件会被移除

```sudo aa-remove-unknown -n```

**移除**配置目录中已不存在对应文件的配置文件

```sudo aa-remove-unknown```

# SYNOPSIS

**aa-remove-unknown** [_-n_]

# DESCRIPTION

**aa-remove-unknown** 会移除那些已加载到内核中、但在配置目录（**/etc/apparmor.d**）里不再有对应文件的 AppArmor 配置文件。这有助于在软件包卸载或配置文件删除之后清理孤立的配置文件。

# PARAMETERS

**-n, --dry-run**
> 只显示哪些配置文件将被移除，而不实际移除

**-h, --help**
> 显示帮助信息

# CAVEATS

不带 **-n** 标志运行会立即从内核卸载孤立的配置文件。请先使用试运行确认将影响哪些配置文件。

# HISTORY

属于 Linux 系统上管理应用安全配置文件的 **AppArmor** 工具包。

# INSTALL

```apt: sudo apt install apparmor```

```pacman: sudo pacman -S apparmor```

```apk: sudo apk add apparmor-utils```

```zypper: sudo zypper install apparmor-utils```

```nix: nix profile install nixpkgs#apparmor-utils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aa-disable](/man/aa-disable)(8), [aa-enforce](/man/aa-enforce)(8), [aa-status](/man/aa-status)(8), [apparmor](/man/apparmor)(7)

# RESOURCES

```[Source code](https://gitlab.com/apparmor/apparmor)```

```[Homepage](https://apparmor.net/)```

```[Documentation](https://gitlab.com/apparmor/apparmor/-/wikis/home)```

<!-- verified: 2026-06-10 -->
