# TAGLINE

安全的命令行与 TUI 密码及 API 密钥管理器

# TLDR

**启动交互式 TUI**

```pass-cli```

**初始化一个新的密码库**

```pass-cli init```

**添加一条凭据**

```pass-cli add [name] --url [https://example.com]```

**读取一条凭据**

```pass-cli get [name]```

**生成随机密码**

```pass-cli generate --length [32]```

# SYNOPSIS

**pass-cli** [_command_] [_options_]

# PARAMETERS

**init**
> 初始化新的密码库。

**add** _NAME_
> 向密码库添加新凭据。

**get** _NAME_
> 按名称读取凭据。

**list**
> 显示所有已存储的凭据。

**update** _NAME_
> 修改现有凭据。

**delete** _NAME_
> 从密码库中删除凭据。

**generate**
> 创建随机密码。

**vault backup create**
> 手动创建密码库备份。

**doctor**
> 运行密码库健康检查。

# DESCRIPTION

**pass-cli** 是一款安全、跨平台的命令行密码与 API 密钥管理器。它使用 AES-256-GCM 加密将凭据存储在本地，同时提供非交互式 CLI 和交互式 TUI 两种模式。专为需要快速、脚本友好地访问凭据且不依赖云端的开发者设计。

# HISTORY

**pass-cli** 由 **arimxyer** 创建，使用 **Go** 编写。

# INSTALL

```dnf: sudo dnf install pass```

```pacman: sudo pacman -S pass```

```apk: sudo apk add pass```

```brew: brew install pass```

```nix: nix profile install nixpkgs#pass```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pass](/man/pass)(1), [passepartui](/man/passepartui)(1), [kure](/man/kure)(1), [gopass](/man/gopass)(1)
