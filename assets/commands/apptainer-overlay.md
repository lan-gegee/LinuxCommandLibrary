# TAGLINE

为容器创建和管理可写的 overlay 文件系统。

# TLDR

向已有的 SIF 镜像**添加可写 overlay**

```apptainer overlay create -s [size] [path/to/image.sif]```

创建**独立的 EXT3** 可写 overlay 镜像

```apptainer overlay create -s [size] [path/to/overlay.img]```

创建**稀疏 overlay** 镜像

```apptainer overlay create -s [size] -S [path/to/overlay.img]```

创建供 **fakeroot** 使用的 overlay

```apptainer overlay create -f -s [size] [path/to/overlay.img]```

创建在布局中带**特定目录**的 overlay

```apptainer overlay create --create-dir [path/to/directory] [path/to/overlay.img]```

# SYNOPSIS

**apptainer overlay create** [_options_] _image_

# DESCRIPTION

**apptainer overlay** 管理 Apptainer 容器的 EXT3 可写 overlay 文件系统。Overlay 允许在不修改原始镜像的情况下，在不可变的 SIF 容器镜像之上进行持久化写入。

Overlay 可以直接嵌入 SIF 文件中，也可以创建为独立镜像文件并在运行时挂载。这样既能持久保存修改、日志和用户数据，又能保持容器的不可变性。

# PARAMETERS

**-s, --size** _size_
> EXT3 可写 overlay 的大小，单位 MiB（默认：64）。

**-S, --sparse**
> 创建稀疏文件而不是一次性分配全部磁盘空间。

**-f, --fakeroot**
> 使 overlay 布局可供以 --fakeroot 运行的 action 使用。

**--create-dir** _path_
> 作为 overlay 布局一部分创建的目录（可重复使用）。

# CAVEATS

Overlay 需要内核支持回环设备和 EXT3。稀疏 overlay 可节省磁盘空间，但在某些工作负载下可能导致性能问题。Overlay 大小在创建后不易更改。

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-build](/man/apptainer-build)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-shell](/man/apptainer-shell)(1), [apptainer-exec](/man/apptainer-exec)(1)

# RESOURCES

```[Source code](https://github.com/apptainer/apptainer)```

```[Homepage](https://apptainer.org)```

```[Documentation](https://apptainer.org/docs/)```

<!-- verified: 2026-06-11 -->
