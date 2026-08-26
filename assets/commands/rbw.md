# TAGLINE

非官方的 Bitwarden CLI 密码管理器

# TLDR

**登录密码库**

```rbw login```

**解锁密码库**

```rbw unlock```

**获取密码**

```rbw get [entry-name]```

**获取完整条目（用户名、密码、备注）**

```rbw get --full [entry-name]```

**获取特定字段**

```rbw get --field username [entry-name]```

**获取 TOTP 验证码**

```rbw code [entry-name]```

**列出条目**

```rbw list```

**搜索条目**

```rbw search [pattern]```

**同步密码库**

```rbw sync```

**添加条目**

```rbw add [entry-name]```

**生成密码并保存**

```rbw generate [entry-name] [username]```

# SYNOPSIS

**rbw** _command_ [_options_] [_args_]

# PARAMETERS

**config**
> 获取或设置配置选项。

**register**
> 向 Bitwarden 服务器注册此设备。

**login**
> 登录 Bitwarden 服务器。

**unlock**
> 解锁本地密码库数据库。

**lock**
> 锁定密码库数据库。

**sync**
> 更新 Bitwarden 数据库的本地副本。

**get** _NAME_
> 显示给定条目的密码。

**search** _TERM_
> 在密码库中搜索条目。

**code** _NAME_
> 显示给定条目的 TOTP 验证器码。

**list**
> 列出所有条目。

**add** _NAME_
> 添加新条目。

**edit** _NAME_
> 修改已有条目。

**remove** _NAME_
> 删除条目。

**generate** _NAME_ _USER_
> 生成新密码并保存。

**history** _NAME_
> 查看条目的密码历史。

**stop-agent**
> 终止后台代理。

**--full**
> 输出用户名、密码和备注。

**--field** _FIELD_
> 输出特定字段。

**--folder** _FOLDER_
> 限定在特定文件夹内。

# DESCRIPTION

**rbw** 是一款非官方的 Bitwarden 命令行客户端，专为 Unix 风格的工作流设计，直接把密码输出到 stdout，方便与脚本、dmenu、rofi 等工具集成。它通过后台代理守护进程（**rbw-agent**）与 Bitwarden 服务器通信，该代理会在本地缓存解密后的密码库，以实现快速读取。

**get** 命令按条目名称检索密码，而 **--field** 标志可以访问用户名、TOTP 验证码或自定义备注等特定字段。**generate** 命令生成随机密码并将其直接存入密码库。使用 **rbw sync** 同步密码库可使本地缓存与服务器保持一致。

# CONFIGURATION

**~/.config/rbw/config.json**
> 客户端配置，指定 Bitwarden 服务器 URL、电子邮件地址、锁定超时时间，以及输入主密码时使用的 pinentry 程序。

**rbw-agent**
> 在内存中维护解密后密码库的后台守护进程。首次运行 rbw 命令时自动启动，并在设定的超时时间后加锁。

# CAVEATS

非官方客户端。部分 Bitwarden 功能不受支持。依赖 rbw-agent 守护进程。

# HISTORY

**rbw** 由 **Jesse Luehrs** 开发，是一款针对 Unix 工作流优化的 Bitwarden 命令行客户端。它使用后台代理（类似 ssh-agent 或 gpg-agent）在内存中持有解密密钥，相比功能完备更强调可脚本化和速度。

# INSTALL

```dnf: sudo dnf install rbw```

```pacman: sudo pacman -S rbw```

```apk: sudo apk add rbw```

```brew: brew install rbw```

```nix: nix profile install nixpkgs#rbw```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [bw](/man/bw)(1), [gopass](/man/gopass)(1)
