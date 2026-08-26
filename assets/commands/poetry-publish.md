# TAGLINE

将软件包发布到 PyPI 或其他仓库

# TLDR

**发布到 PyPI**

```poetry publish```

**构建并发布**

```poetry publish --build```

**发布到自定义仓库**

```poetry publish -r [repository]```

**试运行**

```poetry publish --dry-run```

# SYNOPSIS

**poetry publish** [_options_]

# PARAMETERS

**--build**
> 发布前构建软件包。

**-r**, **--repository** _NAME_
> 目标仓库（默认：pypi）。必须与通过 **poetry config** 配置的名称匹配。

**-u**, **--username** _USER_
> 仓库用户名。

**-p**, **--password** _PASS_
> 仓库密码。

**--cert** _CERT_
> 访问仓库所用的证书颁发机构。

**--client-cert** _CERT_
> 访问仓库所用的客户端证书。

**--dry-run**
> 模拟发布而不实际上传。

**--skip-existing**
> 忽略仓库中已存在文件导致的错误。

# DESCRIPTION

**poetry publish** 将已构建的发行包（wheel 和 sdist）上传到 PyPI 或自定义仓库。**--build** 标志可在发布前一步完成构建。

使用 **-r** 指定通过 **poetry config** 配置的其他仓库。身份验证可通过 **-u**/**-p** 标志、已配置的令牌或密钥环提供。**--dry-run** 标志模拟上传而不实际发布。

# CAVEATS

需要通过用户名/密码、API 令牌或系统密钥环进行身份验证。软件包须先构建好，或使用 **--build** 一步完成构建与发布。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-build](/man/poetry-build)(1), [poetry-config](/man/poetry-config)(1), [twine](/man/twine)(1)
