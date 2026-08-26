# TAGLINE

将容器镜像上传到远程注册表。

# TLDR

将容器推送到 **Container Library**

```apptainer push [path/to/image.sif] library://[user/collection/container]:[tag]```

将容器推送到 **OCI 注册表**

```apptainer push [path/to/image.sif] oras://[registry/namespace/image]:[tag]```

推送**未签名的容器**（跳过签名要求）

```apptainer push -U [path/to/image.sif] library://[user/collection/container]:[tag]```

使用**特定的认证文件**推送到 OCI 注册表

```apptainer push --authfile [path/to/auth.json] [path/to/image.sif] oras://[registry/namespace/image]:[tag]```

推送带**描述信息**的容器（仅限 library）

```apptainer push -D "[description]" [path/to/image.sif] library://[user/collection/container]:[tag]```

# SYNOPSIS

**apptainer push** [_options_] _image_ _URI_

# DESCRIPTION

**apptainer push** 将容器镜像上传到远程注册表，包括 Sylabs Container Library 和兼容 OCI 的注册表。这样可以与协作者共享容器，或将容器部署到生产环境。

大多数注册表都需要身份验证。推送前请使用 **apptainer remote login** 配置凭据。

# PARAMETERS

**-U, --allow-unsigned**
> 允许推送未签名的容器（默认情况下，推送到 library:// 需要有效签名）。

**-D, --description** _text_
> 为容器附加描述（仅限 library://）。

**--library** _url_
> 指定要推送到的 Container Library URL。

**--authfile** _path_
> 用于 OCI 注册表凭据（oras://）的 Docker 风格认证文件。

**--no-https**
> 对 docker://、oras:// 和 library:// URI 使用 HTTP 而不是 HTTPS。

# CAVEATS

推送到 Container Library 需要 Sylabs 账户和 API 令牌。视网络带宽而定，大型镜像的上传可能耗时较长。某些注册表可能会拒绝未签名的容器。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-pull](/man/apptainer-pull)(1), [apptainer-sign](/man/apptainer-sign)(1), [apptainer-delete](/man/apptainer-delete)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
