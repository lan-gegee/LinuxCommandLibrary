# TAGLINE

从文件系统 tar 包创建容器镜像

# TLDR

**将 tar 包导入为镜像**

```podman import [file.tar] [image:tag]```

**从 URL 导入**

```podman import [https://example.com/rootfs.tar] [image]```

**带修改导入**

```podman import --change "CMD [/bin/bash]" [file.tar] [image]```

# SYNOPSIS

**podman import** [_options_] _path_ [_reference_]

# PARAMETERS

_PATH_
> Tar 包路径或 URL。

_REFERENCE_
> 镜像名称和标签。

**--change** _INSTRUCTION_
> 应用 Dockerfile 指令。

**-m**, **--message** _MSG_
> 提交信息。

# DESCRIPTION

**podman import** 从文件系统 tar 包（或 URL）创建新的容器镜像。与 podman load（恢复先前保存的镜像及其所有层和元数据）不同，import 会从根文件系统归档创建扁平的单层镜像。

**--change** 选项允许对导入的镜像应用 Dockerfile 指令（如 CMD、ENTRYPOINT、ENV）。这通常配合 podman export 或其他生成根文件系统 tar 包的工具创建的归档使用。

# CAVEATS

创建单层镜像。没有构建历史。

# HISTORY

podman import 提供 **tar 包转镜像**的功能。

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

[podman](/man/podman)(1), [podman-export](/man/podman-export)(1), [podman-load](/man/podman-load)(1)
