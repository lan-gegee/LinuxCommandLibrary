# TAGLINE

跟踪源码安装并创建软件包

# TLDR

以**默认设置**创建并安装软件包

```sudo checkinstall -y```

只创建软件包但**不安装**

```sudo checkinstall --install=no```

创建**不含文档的**软件包

```sudo checkinstall --nodoc```

创建软件包并**设置名称**

```sudo checkinstall --pkgname [package]```

指定软件包的**保存位置**

```sudo checkinstall --pakdir [path/to/directory]```

# SYNOPSIS

**checkinstall** [_options_] [_install command_]

# DESCRIPTION

**checkinstall** 跟踪软件从源码安装的过程，并生成一个可由系统原生软件包管理器（deb、rpm 或 Slackware tgz）管理的二进制包。

它不直接运行 `make install`，而是监视安装过程中创建了哪些文件并将它们打包。这样就能干净地卸载和管理本地编译的软件。

# PARAMETERS

**-y, --default**
> 以非交互方式接受所有默认值

**--install=**_yes|no_
> 创建后是否安装该软件包

**--nodoc**
> 不在软件包中包含文档

**--pkgname** _name_
> 设置软件包名称

**--pakdir** _path_
> 保存所创建软件包的目录

**-D**
> 创建 Debian 软件包

**-R**
> 创建 RPM 软件包

**-S**
> 创建 Slackware 软件包

**--type** _TYPE_
> 选择打包系统：slackware、debian 或 rpm

**--pkgversion** _VERSION_
> 设置软件包版本号

**--pkgrelease** _RELEASE_
> 设置软件包发行号

**--requires** _DEPS_
> 指定该软件包所需的依赖

**--gzman**
> 压缩软件包内找到的所有 man page

**--exclude** _PATH_
> 将文件或目录排除出软件包

**--include** _FILE_
> 强制包含给定文件中列出的文件/目录

**--inspect**
> 在创建软件包之前检查其文件列表

# CAVEATS

大多数有用的操作必须以 root 身份运行。生成的软件包可能不如发行版官方软件包完善。某些安装过程可能会在被跟踪目录之外创建文件。

# HISTORY

**checkinstall** 的诞生是为了解决管理从源码安装的软件这一难题。它在传统的源码编译与现代软件包管理系统之间架起了一座桥梁。

# INSTALL

```apt: sudo apt install checkinstall```

```nix: nix profile install nixpkgs#checkinstall```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [dpkg](/man/dpkg)(1), [rpm](/man/rpm)(8), [apt](/man/apt)(8), [fakeroot](/man/fakeroot)(1)
