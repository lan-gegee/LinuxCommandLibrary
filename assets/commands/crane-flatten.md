# TAGLINE

将容器层压平为一层

# TLDR

**压平镜像并以新标签推送**

```crane flatten [image] -t [flattened:tag]```

**按摘要压平**（结果以摘要而非标签的形式推回源仓库）

```crane flatten [image@sha256:...]```

**压平多架构索引中的特定平台**

```crane flatten [image] --platform linux/amd64 -t [flattened:tag]```

# SYNOPSIS

**crane** **flatten** [_options_] _image_

# PARAMETERS

**-t**, **--tag** _tag_
> 应用于压平后镜像的标签。若省略，结果将以摘要形式推送到同一仓库，原始标签**不会**被覆盖。

**--platform** _os/arch_
> 压平多架构镜像时选择单一平台（例如 **linux/amd64**）。

**--insecure**
> 允许连接没有有效 TLS 证书的镜像仓库。

**-v**, **--verbose**
> 启用详细日志输出。

# DESCRIPTION

**crane flatten** 将容器镜像的所有层压平为单个层。这可以消除层开销，从而减小镜像体积并提升拉取速度。该命令从镜像仓库读取源镜像，构建一个新的清单，其文件系统是所有层合并后的结果，然后将新清单推回仓库。

# CAVEATS

压平会移除各层的历史记录，并可能影响构建缓存的复用。生成的镜像无法受益于镜像仓库中共享的基础层。若不指定 **-t**，**crane flatten** 不会覆盖源标签；它只会创建一个由摘要引用的新清单。

# INSTALL

```pacman: sudo pacman -S crane```

```apk: sudo apk add crane```

```zypper: sudo zypper install crane```

```brew: brew install crane```

```nix: nix profile install nixpkgs#crane```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[crane](/man/crane)(1), [crane-append](/man/crane-append)(1), [crane-mutate](/man/crane-mutate)(1), [crane-push](/man/crane-push)(1)

# SEE ALSO

[crane](/man/crane)(1), [crane-append](/man/crane-append)(1)
