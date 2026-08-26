# TAGLINE

从 registry 拉取容器镜像

# TLDR

**从 Docker Hub 拉取镜像**

```podman pull [image:tag]```

**从特定 registry 拉取**

```podman pull [registry.example.com/image:tag]```

**拉取所有标签**

```podman pull --all-tags [image]```

**拉取特定平台的镜像**

```podman pull --platform [linux/arm64] [image]```

**不校验 TLS 拉取**

```podman pull --tls-verify=false [image]```

# SYNOPSIS

**podman** **pull** [_options_] _image_

# PARAMETERS

**--all-tags**
> 拉取所有带标签的镜像。

**--tls-verify** _bool_
> 校验 TLS 证书。

**--creds** _user:pass_
> registry 凭据。

**--quiet**
> 抑制输出。

**--arch** _arch_
> 覆盖要拉取镜像的架构。

**--os** _os_
> 覆盖要拉取镜像的操作系统。

**--platform** _os/arch_
> 指定用于选择镜像的平台（例如 linux/amd64）。与 --arch 和 --os 冲突。

**--variant** _variant_
> 覆盖架构变体（例如 arm/v7）。

**--retry** _count_
> 失败时的重试次数。

**--decryption-key** _key[:passphrase]_
> 用于解密加密镜像的密钥。

**--authfile** _path_
> 身份验证文件的路径。

# DESCRIPTION

**podman pull** 从 registry 下载容器镜像。支持 Docker Hub、Quay.io 和私有 registry。镜像存储在本地，供创建容器使用。

拉取策略默认为 **always**。其他策略包括：**missing**（仅在本地没有时拉取）、**never**（仅使用本地镜像）和 **newer**（当 registry 上的镜像更新时拉取）。

# INSTALL

```apt: sudo apt install podman```

```dnf: sudo dnf install podman```

```pacman: sudo pacman -S podman```

```apk: sudo apk add podman```

```zypper: sudo zypper install podman```

```brew: brew install podman```

```nix: nix profile install nixpkgs#podman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[podman](/man/podman)(1), [podman-image](/man/podman-image)(1), [podman-images](/man/podman-images)(1), [podman-run](/man/podman-run)(1)
