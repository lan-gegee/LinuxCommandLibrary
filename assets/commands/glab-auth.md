# TAGLINE

管理 GitLab CLI 的身份验证

# TLDR

登录 GitLab

```glab auth login```

通过管道从文件传入**令牌登录**

```glab auth login --stdin < [token.txt]```

登录到自托管实例

```glab auth login --hostname [gitlab.example.com]```

显示认证状态

```glab auth status```

设置 git 凭据助手

```glab auth git-credential```

登出

```glab auth logout```

# SYNOPSIS

**glab** **auth** _command_ [_options_]

# SUBCOMMANDS

**login**
> 以交互或非交互方式向 GitLab 实例进行身份验证。

**logout**
> 登出某个 GitLab 实例。

**status**
> 显示已知主机的认证状态。

**git-credential**
> 实现 GitLab 的 git 凭据助手，通常由 git 自身调用。

**configure-docker**
> 将 glab 配置为 Docker 的凭据助手。

# PARAMETERS

**-h**, **--hostname** _host_
> 要认证的 GitLab 主机（默认：gitlab.com）。

**-t**, **--token** _token_
> 认证令牌，可通过提示输入、`--stdin` 或 `$GITLAB_TOKEN` 提供。

**--stdin**
> 从标准输入读取令牌而非交互提示。

**--api-host** _host_
> API 主机（若与 Web 主机不同）。

**--api-protocol** _http|https_
> API 请求使用的协议。

**--git-protocol** _http|ssh_
> git 操作使用的协议。

**--use-keyring**
> 将凭据存储在系统密钥环中，而不是明文配置文件。

# DESCRIPTION

**glab auth** 管理 GitLab CLI 的身份验证。它处理使用个人访问令牌或 OAuth 登录 GitLab 实例的过程，并存储凭据供其他 glab 命令使用。

对于自托管的 GitLab 实例，请使用 `--hostname` 标志指定服务器地址。凭据存储在 glab 配置文件中（默认 `~/.config/glab-cli/config.yml`），或在 `--use-keyring` 下存入操作系统密钥环。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab](/man/glab)(1)

# RESOURCES

```[Documentation](https://docs.gitlab.com/cli/auth/)```

```[Source code](https://gitlab.com/gitlab-org/cli)```

<!-- verified: 2026-07-17 -->
