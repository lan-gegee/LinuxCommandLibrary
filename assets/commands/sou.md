# TAGLINE

交互式探索容器镜像层中的文件

# TLDR

**探索本地容器镜像**

```sou [nginx:latest]```

**探索远程容器镜像**

```sou [ghcr.io/user/image:latest]```

# SYNOPSIS

**sou** _image-name_

# DESCRIPTION

**sou** 是一款用于检查 Docker/OCI 容器镜像层的 TUI 工具。它让你浏览每一层内的文件系统、预览文件内容、查看镜像清单（manifest）和配置，并将文件导出到本地。其名称源自日语中表示"层"的词。

# KEYBINDINGS

**层视图**
> 使用方向键或 **hjkl** 导航。用 **yy** 复制层 ID，用 **/** 过滤层。

**文件视图**
> 浏览文件，用 **.** 切换隐藏文件显示，用 **x** 导出选中的文件。

**内容视图**
> 使用方向键或 **hjkl** 滚动查看文件内容。

# HISTORY

**sou** 由 **knqyf263** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#sou```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dive](/man/dive)(1), [docker](/man/docker)(1), [skopeo](/man/skopeo)(1), [crane](/man/crane)(1)
