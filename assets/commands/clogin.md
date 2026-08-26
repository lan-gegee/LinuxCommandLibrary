# TAGLINE

自动登录 Cisco 网络设备

# TLDR

**登录一台 Cisco 设备**

```clogin [hostname]```

**以指定用户名登录**

```clogin -u [username] [hostname]```

**登录并执行文件中的命令**

```clogin -x [commands.txt] [hostname]```

**以 autoenable 模式登录**

```clogin -autoenable [hostname]```

**登录多台设备**

```clogin [host1] [host2] [host3]```

**使用指定的密码文件登录**

```clogin -f [/path/to/.cloginrc] [hostname]```

# SYNOPSIS

**clogin** [_options_] _hostname_ [_hostname_...]

# PARAMETERS

**-u** _username_
> 指定登录用户名。

**-p** _password_
> 指定密码（不安全，建议改用 .cloginrc）。

**-e** _enable_password_
> 指定 enable 密码。

**-autoenable**
> 自动进入 enable 模式。

**-c** _command_
> 登录后执行命令。

**-x** _cmdfile_
> 执行文件中的命令。

**-f** _rcfile_
> 使用替代的配置文件。

**-t** _timeout_
> 以秒为单位设置登录超时时间。

**-d**
> 启用调试输出。

**-v**
> 启用详细输出。

# DESCRIPTION

**clogin** 是 RANCID（Really Awesome New Cisco confIg Differ）的一部分，后者是一套网络设备配置管理系统。它提供到 Cisco 及兼容网络设备的自动登录，处理身份验证和 enable 模式切换。

该工具使用 Expect 脚本自动化交互式登录过程，支持多种身份验证方法和设备提示符。它可以跨多台设备执行命令或脚本，因此对网络自动化和配置备份非常有价值。

凭据通常存储在权限受限的 **.cloginrc** 中。该工具根据设备配置支持 SSH、telnet 等多种访问方式。

# CONFIGURATION

**~/.cloginrc**
> 存储设备凭据、身份验证方法和连接设置。必须设置为 chmod 600。

# CAVEATS

需要 Expect 和 Tcl。.cloginrc 文件包含敏感凭据；请用 **chmod 600** 保护。某些设备提示符未经定制可能无法识别。新的自动化项目可能更适合选用 Ansible 或 Netmiko 等现代替代方案。

# HISTORY

clogin 由 **Henry Kilmer** 等人于 **20 世纪 90 年代末**在 **Shrubbery Networks** 作为 **RANCID**（Really Awesome New Cisco confIg Differ）的一部分开发。RANCID 的目的是自动化网络设备的配置备份与变更追踪。该工具集已扩展至支持 Cisco 之外的众多厂商，其中 clogin 负责 Cisco 特定的设备。

# INSTALL

```apt: sudo apt install rancid```

```dnf: sudo dnf install rancid```

```apk: sudo apk add rancid```

```brew: brew install rancid```

```nix: nix profile install nixpkgs#rancid```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[expect](/man/expect)(1)
