# TAGLINE

验证容器镜像上的加密签名

# TLDR

使用默认 PGP 密钥环**验证**容器镜像

```apptainer verify [path/to/image.sif]```

使用**特定公钥**文件验证容器镜像

```apptainer verify --key [path/to/public.pem] [path/to/image.sif]```

使用**证书**文件验证容器镜像

```apptainer verify --certificate [path/to/certificate.pem] [path/to/image.sif]```

验证镜像中的**所有对象**

```apptainer verify -a [path/to/image.sif]```

验证镜像内的**特定对象组**

```apptainer verify -g [group_id] [path/to/image.sif]```

按 ID 验证镜像内的**特定对象**

```apptainer verify -i [object_id] [path/to/image.sif]```

以 **JSON 格式**输出验证结果

```apptainer verify -j [path/to/image.sif]```

仅使用密钥环中的**本地密钥**进行验证

```apptainer verify -l [path/to/image.sif]```

验证**旧式**（不安全的）签名

```apptainer verify --legacy-insecure [path/to/image.sif]```

# SYNOPSIS

**apptainer verify** [_options_] _image.sif_

# DESCRIPTION

**apptainer verify** 校验 SIF 容器镜像上的加密签名。这可以确认镜像未被篡改，并且是由受信任的一方签名的。

验证可以使用 PGP 公钥、X.509 证书或从密钥服务器获取的密钥。如果验证失败，命令会以非零状态退出。

# PARAMETERS

**--key** _file_
> 用于验证的公钥文件路径

**--certificate** _file_
> 用于验证的证书文件路径

**-a, --all**
> 验证 SIF 镜像中的所有对象

**-g, --group-id** _id_
> 只验证特定的对象组

**-i, --sif-id** _id_
> 按 ID 只验证特定对象

**-j, --json**
> 以 JSON 格式输出结果

**-l, --local**
> 仅用密钥环中的本地密钥验证

**-u, --url** _string_
> 指定密钥服务器的 URL

**--legacy-insecure**
> 启用对（不安全的）旧式签名的验证

**--certificate-intermediates** _file_
> 中间证书池的路径

**--certificate-roots** _file_
> 根证书池的路径

**--ocsp-verify**
> 启用证书的在线吊销检查

# CAVEATS

验证需要与签名密钥对应的公钥或证书。未签名的容器将无法通过验证。不应使用来自不受信任来源的密钥进行验证。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-sign](/man/apptainer-sign)(1), [gpg](/man/gpg)(1)
