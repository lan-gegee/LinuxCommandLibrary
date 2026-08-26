# TAGLINE

低层 conda 软件包实用工具（实验性）

# TLDR

**查找文件属于哪个 conda 软件包**

```conda package --which [path/to/file]```

**列出当前环境中所有未跟踪的文件**

```conda package --untracked```

**从当前环境移除所有未跟踪的文件**

```conda package --reset```

**创建软件包**并指定名称和版本

```conda package --pkg-name [mypackage] --pkg-version [1.0]```

**在具名环境中创建软件包**

```conda package --pkg-name [mypackage] -n [env_name]```

# SYNOPSIS

**conda** **package** [_options_]

# PARAMETERS

**-w**, **--which** _PATH_
> 给定一个文件路径，识别该文件来自哪个 conda 软件包。

**-u**, **--untracked**
> 显示所有未跟踪的文件并退出。

**-r**, **--reset**
> 移除所有未跟踪的文件并退出。

**--pkg-name** _PKG_NAME_
> 指定要创建的软件包的名称。

**--pkg-version** _PKG_VERSION_
> 指定要创建的软件包的版本。

**--pkg-build** _PKG_BUILD_
> 指定要创建的软件包的构建号。

**-n**, **--name** _name_
> 环境名称。

**-p**, **--prefix** _path_
> 环境位置（前缀）的完整路径。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda package** 是一款实验性的低层工具，用于创建 conda 软件包以及检查环境内的软件包内容。它可以识别某个文件属于哪个软件包、列出或移除未跟踪的文件，并根据当前环境状态创建简单的软件包。

# CAVEATS

该命令被标记为实验性，可能会更改或被移除。标准的软件包构建请改用 **conda-build**。若要共享环境，建议使用 **conda env export** 生成 environment.yml 文件。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-env](/man/conda-env)(1)
