# TAGLINE

以其他用户身份运行命令

# TLDR

以**其他用户**身份运行命令

```runuser [user] -c '[command]'```

以指定用户和**组**运行

```runuser [user] -g [group] -c '[command]'```

启动**登录 shell**

```runuser [user] -l```

使用**指定的 shell**

```runuser [user] -s /bin/bash```

**保留**环境变量

```runuser [user] -p -c '[command]'```

# SYNOPSIS

**runuser** [**-l**] [**-c** _command_] [**-g** _group_] [**-s** _shell_] [**-p**] _user_

# PARAMETERS

**-c, --command _command_**
> 要执行的命令

**-g, --group _group_**
> 指定组

**-l, --login**
> 启动登录 shell

**-s, --shell _shell_**
> 使用指定的 shell

**-p, --preserve-environment**
> 保留环境变量

**-w, --whitelist-environment**
> 保留特定的环境变量

# DESCRIPTION

**runuser** 以另一个用户的身份运行命令，无需密码认证。与 su 不同，它专为 root 在系统脚本和服务中使用而设计，适用于不适合交互式认证的场景。

该工具常用于 init 脚本和系统服务中，在执行命令前将权限降级到特定用户。

# CAVEATS

需要 root 才能运行。没有密码提示（不同于 su）。环境变量的处理取决于所用选项。登录 shell 会重置大部分环境。

# HISTORY

**runuser** 是 **util-linux** 的一部分，为 root 提供一种非交互地以其他用户身份运行命令的方式。由于其行为可预测，在脚本中比 su 更受青睐。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add runuser```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[su](/man/su)(1), [sudo](/man/sudo)(8), [runcon](/man/runcon)(1)
