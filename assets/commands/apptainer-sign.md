# TAGLINE

对 SIF 容器镜像进行加密签名

# TLDR

使用默认 PGP 密钥**签名**容器镜像

```apptainer sign [path/to/image.sif]```

使用**特定私钥**文件签名容器镜像

```apptainer sign --key [path/to/private.pem] [path/to/image.sif]```

使用**特定的 PGP 密钥索引**签名容器镜像

```apptainer sign -k [key_index] [path/to/image.sif]```

签名镜像内的**特定对象组**

```apptainer sign -g [group_id] [path/to/image.sif]```

按 ID 签名镜像内的**特定对象**

```apptainer sign -i [object_id] [path/to/image.sif]```

# SYNOPSIS

**apptainer sign** [_options_] _image.sif_

# DESCRIPTION

**apptainer sign** 为 SIF 容器镜像添加数字签名，从而可以验证镜像的完整性和真实性。签名可以使用 PGP 密钥或 X.509 证书。

为容器签名对于在共享容器镜像时建立信任、以及满足生产环境的安全要求至关重要。

# PARAMETERS

**--key** _file_
> 用于签名的私钥文件路径

**-k, --keyidx** _index_
> 要使用的密钥环中 PGP 密钥的索引

**-g, --group-id** _id_
> 只签名 SIF 内的特定对象组

**-i, --sif-id** _id_
> 按 ID 只签名 SIF 内的特定对象

# CAVEATS

签名前必须配置好 PGP 密钥对或 X.509 证书。私钥必须妥善保管；一旦泄露应立即吊销。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-verify](/man/apptainer-verify)(1), [apptainer-pull](/man/apptainer-pull)(1), [gpg](/man/gpg)(1)
