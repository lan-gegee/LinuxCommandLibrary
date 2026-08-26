# TAGLINE

管理 DigitalOcean CLI 的认证上下文

# TLDR

**初始化认证**

```doctl auth init```

**直接使用令牌初始化**

```doctl auth init --access-token [token]```

**列出认证上下文**

```doctl auth list```

**切换到指定上下文**

```doctl auth switch --context [context_name]```

**移除认证上下文**

```doctl auth remove --context [context_name]```

# SYNOPSIS

**doctl auth** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 操作：init、list、switch、remove。

**init**
> 使用令牌初始化认证。

**list**
> 列出认证上下文。

**switch** **--context** _NAME_
> 切换活动上下文。

**remove** **--context** _NAME_
> 移除上下文。

**--access-token** _TOKEN_
> API 访问令牌。

**--context** _NAME_
> 上下文名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**doctl auth** 管理 DigitalOcean CLI 的认证上下文。上下文允许为不同的账户、团队或环境保存多个 API 令牌。

init 命令会提示输入或直接接受 API 令牌，并将其安全存储。可以配置多个上下文并在其间切换，从而通过单个 CLI 安装管理多个 DigitalOcean 账户。

认证令牌从 DigitalOcean 控制面板获取，并按其作用范围提供相应的 API 访问权限。

# CAVEATS

令牌存储在本地。令牌的作用范围决定了可执行的操作。过期或被吊销的令牌需要重新认证。上下文是特定于机器的。

# HISTORY

doctl auth 是 **DigitalOcean** 开发的 **doctl** CLI 的一部分。多上下文支持让用户和组织能够高效地管理多个账户。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-compute-droplet](/man/doctl-compute-droplet)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/reference/auth/)```

<!-- verified: 2026-07-11 -->
