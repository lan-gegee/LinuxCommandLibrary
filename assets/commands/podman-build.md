# TAGLINE

从 Containerfile 构建容器镜像

# TLDR

**从当前目录的 Containerfile 构建**

```podman build -t [image:tag] .```

**使用指定的 Containerfile 构建**

```podman build -f [Containerfile.dev] -t [image:tag] [path]```

**不使用缓存构建**

```podman build --no-cache -t [image:tag] [path]```

**使用构建参数构建**

```podman build --build-arg [KEY=value] -t [image:tag] [path]```

**在多阶段构建中构建特定阶段**

```podman build --target [stage_name] -t [image:tag] [path]```

**为特定平台构建**

```podman build --platform [linux/arm64] -t [image:tag] [path]```

# SYNOPSIS

**podman build** [_options_] _context_

# PARAMETERS

_CONTEXT_
> 构建上下文目录或 URL。

**-t**, **--tag** _NAME_
> 镜像名称和可选标签（name:tag）。

**-f**, **--file** _FILE_
> Containerfile 路径。使用 -f - 从 stdin 读取。

**--no-cache**
> 构建时不使用已有的缓存镜像。重建所有层。

**--build-arg** _ARG_
> KEY=value 格式的构建时变量。

**--pull**
> 即使本地已有副本也始终拉取基础镜像。接受 always、missing、never 或 true/false。

**--squash**
> 将所有新建的层压缩为单层。

**--target** _STAGE_
> 设置多阶段 Containerfile 中的目标构建阶段。

**--platform** _OS/ARCH_
> 设置所构建镜像的操作系统/架构（例如 linux/arm64、linux/amd64）。

**--layers**
> 在构建过程中缓存中间镜像（默认 true）。

**--format** _FORMAT_
> 镜像清单和元数据格式（oci 或 docker）。

**--label** _LABEL_
> 以 KEY=value 格式为镜像添加标签。

**-v**, **--volume** _SRC:DST[:OPT]_
> 在 RUN 指令执行期间将主机路径绑定挂载到容器中（不会持久化到镜像里）。

**--network** _MODE_
> 为 RUN 指令配置网络模式（例如 _host_、_none_、_bridge_）。

**--secret** _ID=src=PATH_
> 传递供 RUN 期间使用的机密文件或环境变量，不会存储在镜像中。

**--mount** _TYPE,...,_
> 为 RUN 命令附加文件系统挂载（如 **type=cache** 或 **type=secret**）。

**--env** _KEY=VAL_
> 在生成的镜像上设置环境变量。

**-m**, **--memory** _LIMIT_
> 限制构建期间 RUN 容器可用的内存。

**--security-opt** _OPTION_
> 应用安全选项（SELinux 标签、AppArmor 配置、seccomp 配置）。

# DESCRIPTION

**podman build** 根据指定构建上下文目录中的 Containerfile（或 Dockerfile）创建容器镜像。它兼容 Docker 的构建语法，支持多阶段构建、构建参数和层缓存。

底层实际使用 Buildah 执行镜像构建。默认输出符合 OCI 规范的容器镜像。

# CAVEATS

底层使用 Buildah。与 Docker build 高度兼容，但某些 Docker 特有功能可能表现不同。默认镜像格式为 OCI，这与 Docker 默认使用 Docker 格式不同。需要 Docker 兼容性时可使用 **--format docker**。

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

[podman](/man/podman)(1), [buildah](/man/buildah)(1), [docker-build](/man/docker-build)(1), [podman-run](/man/podman-run)(1)
