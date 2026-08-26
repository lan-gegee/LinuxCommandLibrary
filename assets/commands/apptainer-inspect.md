# TAGLINE

显示容器镜像中的元数据。

# TLDR

显示镜像的**标签**（默认行为）

```apptainer inspect [path/to/image.sif]```

显示构建镜像所用的**定义文件**

```apptainer inspect -d [path/to/image.sif]```

显示镜像的 **runscript**

```apptainer inspect -r [path/to/image.sif]```

显示镜像的**环境变量**

```apptainer inspect -e [path/to/image.sif]```

显示镜像的 **startscript**

```apptainer inspect -s [path/to/image.sif]```

检查容器内的**特定应用**

```apptainer inspect --app [app_name] [path/to/image.sif]```

**列出容器中的所有应用**

```apptainer inspect --list-apps [path/to/image.sif]```

以 JSON 格式显示**所有可用数据**

```apptainer inspect --all [path/to/image.sif]```

# SYNOPSIS

**apptainer inspect** [_inspect options..._] _image_path_

# DESCRIPTION

**apptainer inspect** 显示嵌入在 Apptainer 容器镜像中的元数据，包括标签、构建容器所用的定义文件、runscript、环境设置以及所打包应用的信息。

这些元数据为了解容器的来源、可复现性和预期用途提供了有价值的信息。

# PARAMETERS

**-l, --labels**
> 显示镜像的标签（默认行为）

**-d, --deffile**
> 显示构建容器所用的定义文件

**-r, --runscript**
> 显示容器的 runscript

**-s, --startscript**
> 显示镜像的 startscript

**-t, --test**
> 显示镜像的测试脚本

**-e, --environment**
> 显示容器中设置的环境变量

**-H, --helpfile**
> 显示 runscript 的帮助文件（如存在）

**--app** _name_
> 检查容器内特定的 SCIF 应用

**--list-apps**
> 列出容器中安装的所有 SCIF 应用

**--all**
> 显示所有可用元数据（隐含 --json）

**-j, --json**
> 以 JSON 格式输出结果

# INSTALL

```dnf: sudo dnf install apptainer```

```pacman: sudo pacman -S apptainer```

```apk: sudo apk add apptainer```

```zypper: sudo zypper install apptainer```

```brew: brew install apptainer```

```nix: nix profile install nixpkgs#apptainer```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[apptainer](/man/apptainer)(1), [apptainer-build](/man/apptainer-build)(1), [apptainer-run](/man/apptainer-run)(1), [apptainer-exec](/man/apptainer-exec)(1)
