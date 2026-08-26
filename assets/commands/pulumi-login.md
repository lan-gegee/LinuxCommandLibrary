# TAGLINE

向 Pulumi 状态后端进行身份验证

# TLDR

**登录 Pulumi Cloud**

```pulumi login```

**登录本地后端**

```pulumi login --local```

**登录指定的云**

```pulumi login [url]```

**登录 S3 后端**

```pulumi login s3://[bucket]```

# SYNOPSIS

**pulumi** **login** [_options_] [_url_]

# PARAMETERS

**--local**
> 使用本地文件后端。

**--cloud-url** _url_
> 指定后端 URL。

**-c**, **--cloud**
> 登录 Pulumi Cloud。

# DESCRIPTION

**pulumi login** 向 Pulumi 后端进行身份验证。支持 Pulumi Cloud、自托管后端以及云存储后端（S3、Azure Blob、GCS）。后端用于存储堆栈状态和历史记录。

# INSTALL

```pacman: sudo pacman -S pulumi```

```apk: sudo apk add pulumi```

```brew: brew install pulumi```

```nix: nix profile install nixpkgs#pulumi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pulumi](/man/pulumi)(1), [pulumi-logout](/man/pulumi-logout)(1), [pulumi-whoami](/man/pulumi-whoami)(1)
