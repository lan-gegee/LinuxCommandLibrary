# TAGLINE

管理容器镜像仓库的身份验证

# TLDR

**登录镜像仓库**

```crane auth login [registry] -u [username] -p [password]```

**获取身份验证令牌**

```crane auth token [image]```

**登出镜像仓库**

```crane auth logout [registry]```

# SYNOPSIS

**crane** **auth** _subcommand_ [_options_]

# SUBCOMMANDS

**login**
> 向镜像仓库进行身份验证。

**logout**
> 移除镜像仓库的凭据。

**token**
> 获取镜像的身份验证令牌。

**get**
> 获取镜像仓库的凭据。

# PARAMETERS

**-u**, **--username** _user_
> 用于身份验证的用户名。

**-p**, **--password** _pass_
> 用于身份验证的密码。

**--password-stdin**
> 从 stdin 读取密码。

# DESCRIPTION

**crane auth** 管理容器镜像仓库的身份验证。它负责存储凭据，并为镜像仓库操作获取身份验证令牌。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [docker-login](/man/docker-login)(1)

# RESOURCES

```[Source code](https://github.com/google/go-containerregistry)```

```[Documentation](https://github.com/google/go-containerregistry/blob/main/cmd/crane/doc/crane.md)```

<!-- verified: 2026-06-23 -->
