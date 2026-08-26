# TAGLINE

管理 GitHub CLI 认证与凭据

# TLDR

**登录 GitHub**

```gh auth login```

**登录指定主机**

```gh auth login --hostname [github.example.com]```

**检查认证状态**

```gh auth status```

**退出 GitHub 登录**

```gh auth logout```

**刷新认证**

```gh auth refresh```

# SYNOPSIS

**gh auth** _command_ [_options_]

# PARAMETERS

**login**
> 向某个 GitHub 主机进行身份验证。

**logout**
> 从某个 GitHub 主机退出登录。

**status**
> 查看认证状态。

**refresh**
> 刷新存储的凭据。

**token**
> 打印认证令牌。

**--hostname** _HOST_
> GitHub 主机名（适用于 Enterprise）。

**--web**
> 打开浏览器进行认证。

**--with-token**
> 从 stdin 读取令牌。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh auth** 管理 GitHub CLI 的认证。它处理 OAuth 设备流、个人访问令牌和 SSH 密钥认证，可跨多个 GitHub 主机使用。

该命令在系统密钥链可用时将凭据安全地存入其中，否则回退到加密文件存储。它支持同时使用 github.com 和 GitHub Enterprise Server 实例。

gh auth 是所有需要认证的 gh 操作的基础。

# CONFIGURATION

**~/.config/gh/hosts.yml**
> 存储每个 GitHub 实例的认证令牌和主机特定设置。

# CAVEATS

令牌作用域影响可用命令。Enterprise 实例可能需要 SSO 认证。凭据保存在密钥链或配置文件中。

# HISTORY

gh auth 是 **GitHub CLI** 的一部分，为交互式和脚本化场景设计了安全的认证流程。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-config](/man/gh-config)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_auth)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
