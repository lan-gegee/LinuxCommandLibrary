# TAGLINE

显示 DigitalOcean 账户信息

# TLDR

**显示账户信息**

```doctl account get```

**显示速率限制状态**

```doctl account ratelimit```

# SYNOPSIS

**doctl** **account** _command_

# SUBCOMMANDS

**get**
> 显示账户信息。

**ratelimit**
> 显示 API 速率限制状态。

# DESCRIPTION

**doctl account** 显示你的 DigitalOcean 账户信息，包括邮箱、UUID、状态和 API 速率限制。

该命令无需进入网页控制台即可快速查看账户详情。适合用来确认当前认证的是哪个账户，尤其是在管理多个上下文时。ratelimit 子命令有助于监控 API 用量，避免在自动化操作或密集脚本执行时超出速率限制。

# INSTALL

```dnf: sudo dnf install doctl```

```pacman: sudo pacman -S doctl```

```apk: sudo apk add doctl```

```brew: brew install doctl```

```nix: nix profile install nixpkgs#doctl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doctl](/man/doctl)(1), [doctl-auth](/man/doctl-auth)(1)

# RESOURCES

```[Source code](https://github.com/digitalocean/doctl)```

```[Documentation](https://docs.digitalocean.com/reference/doctl/)```

<!-- verified: 2026-07-11 -->
