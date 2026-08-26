# TAGLINE

将基础操作系统切换为不同的容器镜像

# TLDR

将基础操作系统切换为**来自镜像仓库的容器镜像**

```sudo bootc switch [image]```

切换到新镜像并**立即重启**

```sudo bootc switch --apply [image]```

切换为**本地容器存储**中的镜像

```sudo bootc switch --transport containers-storage [image]```

切换为 **OCI 归档**中的镜像

```sudo bootc switch --transport oci-archive [path/to/image.tar]```

# SYNOPSIS

**bootc switch** [_options_] _image_

# DESCRIPTION

**bootc switch** 将基础操作系统更换为另一个容器镜像。这样可以在不同的操作系统变体或版本之间切换，同时保持事务性和可回滚的系统。

新镜像会被暂存，并在下次重启时生效。先前的部署会被保留，以便在需要时回滚。此操作类似于 `bootc upgrade`，但还会更改容器镜像引用。

# PARAMETERS

**--transport** _type_
> 镜像来源类型：registry（默认）、containers-storage、oci-archive。

**--apply**
> 暂存完成后立即重启进入新的目标镜像。目前总是执行完整重启；未来版本可能在没有内核变更排队时仅进行用户态重启。

**--soft-reboot** _mode_
> 与 --apply 配合使用时控制软重启行为。取值：auto（可用时使用软重启，否则回退到完整重启）、required（软重启不可用时失败）。

**--enforce-container-sigpolicy**
> 要求 /etc/containers/policy.json 包含强制镜像签名的默认策略。

**--retain**
> 保留对当前已启动镜像的引用。

**--quiet**
> 不显示进度输出。

# CAVEATS

切换到不兼容的镜像可能导致系统无法启动。请确保目标镜像与系统架构和配置兼容。需要 root 权限。

# INSTALL

```dnf: sudo dnf install bootc```

```nix: nix profile install nixpkgs#bootc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bootc](/man/bootc)(1), [podman](/man/podman)(1), [skopeo](/man/skopeo)(1), [rpm-ostree](/man/rpm-ostree)(1), [ostree](/man/ostree)(1)
