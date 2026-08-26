# TAGLINE

用于软件包构建的模拟 root 环境

# TLDR

以 **fakeroot** 身份启动默认 shell

```fakeroot```

以 fakeroot 身份运行**命令**

```fakeroot -- [command] [command_arguments]```

运行命令并在退出时**保存**环境

```fakeroot -s [path/to/file] -- [command] [command_arguments]```

**加载**环境并运行命令

```fakeroot -i [path/to/file] -- [command] [command_arguments]```

保留真实属主而不伪装成 root

```fakeroot [-u|--unknown-is-real] -- [command] [command_arguments]```

显示**帮助**

```fakeroot [-h|--help]```

# SYNOPSIS

**fakeroot** [_options_] [_command_]

# PARAMETERS

**-s** _file_
> 退出时保存 fakeroot 环境。

**-i** _file_
> 从上一次会话加载 fakeroot 环境。

**-u**, **--unknown-is-real**
> 对未被 fakeroot 跟踪的文件保留其真实属主。

**-b** _fd_
> faked 库使用的文件描述符。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# DESCRIPTION

**fakeroot** 在一个对文件操作伪装出 root 权限的环境中运行命令。它拦截系统调用，使文件看起来由 root 所有，而实际上并无 root 权限。

该工具通过 LD_PRELOAD 拦截库调用，并维护一个虚假所有权和权限信息数据库。当程序创建文件时，fakeroot 将其记录为由 root 所有（uid 0、gid 0），而磁盘上的实际文件仍属于当前用户。

这常用于构建需要创建 root 属主文件的软件包（尤其是 Debian 的 .deb 包）。保存的环境（-s/-i）允许在多条命令和多个会话之间保留虚假的所有权信息。

# CAVEATS

并不提供真正的 root 权限。只伪造所有权信息。广泛用于 dpkg-buildpackage 等软件包构建系统。

# INSTALL

```dnf: sudo dnf install fakeroot```

```pacman: sudo pacman -S fakeroot```

```apk: sudo apk add fakeroot```

```zypper: sudo zypper install fakeroot```

```brew: brew install fakeroot```

```nix: nix profile install nixpkgs#fakeroot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [dpkg-buildpackage](/man/dpkg-buildpackage)(1)
