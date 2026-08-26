# TAGLINE

以指定的 SELinux 上下文运行命令

# TLDR

打印当前**安全上下文**

```runcon```

指定命令运行的**域**

```runcon -t domain_t command```

指定上下文**角色**

```runcon -r role_r command```

指定**完整上下文**

```runcon user_u:role_r:domain_t command```

# SYNOPSIS

**runcon** [_options_] [_context_] _command_ [_args_...]

# PARAMETERS

**-u**, **--user** _user_
> 指定 SELinux 用户身份。

**-r**, **--role** _role_
> 指定 SELinux 角色。

**-t**, **--type** _type_
> 指定 SELinux 域/类型（要求角色和用户保持不变）。

**-l**, **--range** _range_
> 指定 SELinux MLS/MCS 级别范围。

**--compute**
> 在修改前计算目标进程的安全上下文。

**--help**
> 显示帮助信息。

**--version**
> 输出版本信息。

# DESCRIPTION

**runcon** 在不同的 SELinux 安全上下文中运行程序。它允许以特定的 SELinux 用户、角色和类型标签执行命令。

这对于测试 SELinux 策略以及在受限上下文中运行程序很有用。

# CAVEATS

需要启用 SELinux。上下文切换必须获得 SELinux 策略允许。并非所有上下文切换都被允许。

# HISTORY

属于 **GNU Coreutils**，为命令执行提供 SELinux 上下文操作能力。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[secon](/man/secon)(1), [run_init](/man/run_init)(8), [chcon](/man/chcon)(1)
