# TAGLINE

通过 systemd 以其他用户身份运行命令

# TLDR

以 **root** 身份运行命令

```run0 [command]```

以**指定用户**身份运行

```run0 -u [username] [command]```

以指定用户和**组**身份运行

```run0 -u [username] -g [group] [command]```

# SYNOPSIS

**run0** [**-u**|**--user** _user_] [**-g**|**--group** _group_] [_command_]

# PARAMETERS

**-u, --user _user_**
> 以指定用户身份运行

**-g, --group _group_**
> 以指定的组运行

**--no-ask-password**
> 不提示输入密码

**--machine _machine_**
> 在容器/虚拟机上执行

**-D, --chdir _path_**
> 运行前更改工作目录

**--setenv _NAME=VALUE_**
> 为被调用的进程设置环境变量

**--background _color_**
> 更改终端背景色调（设为空则禁用）

**--nice _N_**
> 以调整后的调度优先级运行命令

# DESCRIPTION

**run0** 在不作为 SUID 二进制文件的情况下提升权限。与 sudo 不同，它通过 polkit 进行认证，并通过 systemd 服务来启动命令，提供更好的安全隔离。

该工具被设计为 sudo 的更安全替代品，避免了 SUID 二进制文件带来的安全问题，同时保持大家熟悉的权限提升语义。

# CAVEATS

需要 systemd 256 及以上版本。认证通过 polkit 完成。环境变量的处理方式与 sudo 不同。部分 sudo 特性不可用。

# HISTORY

**run0** 由 Lennart Poettering 在 **systemd 256** 中引入，作为 sudo 的安全替代方案。它使用 polkit 进行认证并以服务方式执行命令，从而解决了与 SUID 相关的安全问题。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [pkexec](/man/pkexec)(1), [doas](/man/doas)(1), [systemd-run](/man/systemd-run)(1)
