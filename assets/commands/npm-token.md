# TAGLINE

管理认证令牌

# TLDR

**列出令牌**

```npm token list```

**创建令牌**

```npm token create```

**创建只读令牌**

```npm token create --read-only```

**创建 CI 令牌**

```npm token create --cidr=[192.168.1.0/24]```

**吊销令牌**

```npm token revoke [token-id]```

# SYNOPSIS

**npm** **token** [_command_] [_options_]

# PARAMETERS

_COMMAND_
> 令牌子命令。

**list**
> 显示所有令牌。

**create**
> 生成新令牌。

**revoke** _ID_
> 使令牌失效。

**--read-only**
> 只读令牌。

**--cidr** _RANGE_
> IP 限制。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm token** 用于管理认证令牌，可为 CI/CD 创建令牌。

该命令处理 API 令牌，支持限定范围的权限。

# CAVEATS

需要身份验证。令牌属于敏感信息，请妥善保管。

# HISTORY

npm token 为自动化访问 npm registry 提供**令牌管理**功能。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-login](/man/npm-login)(1), [npm-publish](/man/npm-publish)(1)
