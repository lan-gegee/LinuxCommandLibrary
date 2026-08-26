# TAGLINE

向用户查询系统密码

# TLDR

用指定的提示语**查询**系统密码

```systemd-ask-password "[prompt]"```

为密码查询**指定**标识符

```systemd-ask-password --id [identifier] "[prompt]"```

**使用**内核密钥环的密钥名称作为缓存

```systemd-ask-password --keyname [key_name] "[prompt]"```

为查询**设置**自定义超时

```systemd-ask-password --timeout [seconds] "[prompt]"```

**强制**使用代理系统（绝不在 TTY 上询问）

```systemd-ask-password --no-tty "[prompt]"```

将密码**存入**内核密钥环而不显示

```systemd-ask-password --no-output --keyname [key_name] "[prompt]"```

将密码通过管道传给命令且不带末尾换行符

```systemd-ask-password -n | [command]```

# SYNOPSIS

**systemd-ask-password** [_options_] [_message_]

# PARAMETERS

**--id _identifier_**
> 密码查询的唯一标识符

**--keyname _name_**
> 用于缓存的内核密钥环密钥名称

**--timeout _seconds_**
> 密码输入的超时时间

**--no-tty**
> 绝不在当前 TTY 上查询密码

**--no-output**
> 不将密码打印到 stdout

**-n, --newline=no**
> 不打印末尾换行符

**--accept-cached**
> 接受来自密钥环的缓存密码

# DESCRIPTION

**systemd-ask-password** 向用户查询系统密码，并可选择将其缓存在内核密钥环中。它与 systemd 密码代理基础设施集成，用于启动时的密码提示。

该工具常用于磁盘加密口令，但也可用于任何需要安全密码输入并支持可选缓存的脚本。

# CAVEATS

内核密钥环中的缓存密码会在重启时清除。**--no-tty** 选项要求有正在运行的密码代理。属于 systemd 工具套件的一部分。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemd-tty-ask-password-agent](/man/systemd-tty-ask-password-agent)(1), [cryptsetup](/man/cryptsetup)(8)
