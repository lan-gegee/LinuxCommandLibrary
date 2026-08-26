# TAGLINE

打印当前有效用户名

# TLDR

**打印当前用户名**

```whoami```

# SYNOPSIS

**whoami** [**--help**] [**--version**]

# PARAMETERS

**--help**
> 显示帮助并退出

**--version**
> 显示版本并退出

# DESCRIPTION

**whoami** 打印与当前有效用户 ID 关联的用户名。它等价于 **id -un**。

在脚本中可以用它来确定正在运行脚本的用户，尤其是当脚本可能通过 sudo 运行或在使用 su 切换用户之后。

与显示 utmp 中登录名的 **who am i** 不同，**whoami** 显示的是有效用户 ID 的名称，在 sudo 或 su 之后两者可能不同。

# CAVEATS

执行 **sudo** 之后，whoami 显示的是目标用户（通常是 root），而不是原始用户。要获取原始登录名，请使用 **logname** 或 **who am i**。

该命令显示的是**有效**用户 ID。在 setuid 程序中，它可能与真实用户 ID 不同。

# INSTALL

```apt: sudo apt install coreutils```

```dnf: sudo dnf install coreutils```

```pacman: sudo pacman -S coreutils```

```apk: sudo apk add coreutils```

```zypper: sudo zypper install coreutils```

```brew: brew install coreutils```

```nix: nix profile install nixpkgs#coreutils```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[who](/man/who)(1), [id](/man/id)(1), [logname](/man/logname)(1), [users](/man/users)(1)
