# TAGLINE

显示 pacman 数据库中文件的信息，表明其所属软件包

# TLDR

显示关于**软件包文件**的信息

```pacfile [path/to/file_or_directory]```

将数据库中的值与文件系统进行**比较**

```pacfile [path/to/file_or_directory] --check```

显示**帮助**

```pacfile --help```

显示**版本**

```pacfile --version```

# SYNOPSIS

**pacfile** [_options_] _path_...

# PARAMETERS

**--check**
> 将数据库中的值与文件系统状态进行比较

**--package** _pkg_
> 将输出限制为指定软件包拥有的文件

**--config** _file_
> 使用备用的 pacman 配置文件

**--dbpath** _path_
> 使用备用的数据库路径

**--root** _path_
> 使用备用的安装根目录

**--help**
> 显示帮助信息

**--version**
> 显示版本信息

# DESCRIPTION

**pacfile** 显示 pacman 数据库中文件的信息，包括文件所属的软件包，并将存储的元数据与当前文件系统状态进行对比。它可以识别被修改的文件、缺失的文件以及归属信息。

该工具可用于排查文件归属冲突、验证文件完整性以及理解软件包之间的关系。它读取 pacman 的本地数据库以提供准确的归属信息。

# CAVEATS

仅显示 pacman 数据库所跟踪文件的信息。通过 pacman 以外方式安装的文件不会显示归属信息。对比检查可能会标记出预期内的修改（例如被编辑过的配置文件）。

# HISTORY

属于 **pacutils**，由 Andrew Gregory 开发的 pacman 工具集。提供了超出 pacman 内置查询选项范围的详细文件级查询能力。

# SEE ALSO

[pacman](/man/pacman)(8), [paccheck](/man/paccheck)(8), [pkgfile](/man/pkgfile)(1)
