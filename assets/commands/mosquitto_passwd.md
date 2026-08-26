# TAGLINE

管理 Mosquitto MQTT 代理的密码文件

# TLDR

**创建包含用户的密码文件**

```mosquitto_passwd -c [passwordfile] [username]```

**向已有文件添加用户**

```mosquitto_passwd [passwordfile] [username]```

**删除用户**

```mosquitto_passwd -D [passwordfile] [username]```

**以批处理模式提供密码**

```mosquitto_passwd -b [passwordfile] [username] [password]```

# SYNOPSIS

**mosquitto_passwd** [_options_] _passwordfile_ [_username_]

# PARAMETERS

**-c**
> 创建新的密码文件。

**-D**
> 从文件中删除用户。

**-b**
> 批处理模式，密码直接写在命令行上。

**-U**
> 将明文文件升级为哈希格式。

# DESCRIPTION

**mosquitto_passwd** 用于管理 Mosquitto MQTT 代理的密码文件。它以安全哈希方式创建和修改密码条目，用于 MQTT 消息系统中的客户端身份验证。

# CAVEATS

在脚本中应避免使用 **-b** 选项，因为密码可能出现在进程列表中。请使用交互模式或从安全的来源管道输入。

# INSTALL

```apt: sudo apt install mosquitto```

```dnf: sudo dnf install mosquitto```

```pacman: sudo pacman -S mosquitto```

```apk: sudo apk add mosquitto```

```zypper: sudo zypper install mosquitto```

```brew: brew install mosquitto```

```nix: nix profile install nixpkgs#mosquitto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mosquitto](/man/mosquitto)(1), [mosquitto_sub](/man/mosquitto_sub)(1), [mosquitto_pub](/man/mosquitto_pub)(1)
