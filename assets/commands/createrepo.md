# TAGLINE

RPM 软件仓库元数据生成器

# TLDR

**初始化**一个基础的软件仓库

```createrepo [path/to/directory]```

以**排除项**和详细输出进行初始化

```createrepo -v -x [test_*.rpm] [path/to/directory]```

使用 **SHA1 校验和**并跳过符号链接

```createrepo -S -s sha1 [path/to/directory]```

# SYNOPSIS

**createrepo** [_options_] _directory_

# DESCRIPTION

**createrepo** 通过创建 yum/dnf 软件包管理器所需的元数据文件来初始化 RPM 软件仓库。它会扫描存放 RPM 软件包的目录，生成一个 repodata 子目录，其中包含描述可用软件包的 XML 元数据文件和 SQLite 数据库。

生成的元数据包括软件包名称、版本、依赖关系、文件列表和校验和。借助这些信息，yum/dnf 客户端能够查询软件包信息、解析依赖并直接从仓库安装软件，而无须下载每一个 RPM 文件。无论是搭建本地仓库、企业自定义软件包分发还是镜像站点，该工具都不可或缺。

# PARAMETERS

**-v, --verbose**
> 详细输出

**-x, --excludes** _pattern_
> 排除匹配模式的软件包

**-s, --checksum** _type_
> 校验和算法（sha1、sha256 等）

**-S, --skip-symlinks**
> 忽略符号链接

**-u, --baseurl** _url_
> 仓库的基础 URL

**--update**
> 更新已有仓库（速度更快）

# CAVEATS

在添加或删除软件包之后必须重新运行。对于大型仓库，--update 比完全重新生成更快。最初的 Python 版 createrepo 已被弃用；在现代发行版上，**createrepo** 命令由 **createrepo_c** 提供——这是用 C 重写的更快的实现，接受相同的核心选项。

# SEE ALSO

[yum](/man/yum)(8), [dnf](/man/dnf)(8), [rpm](/man/rpm)(8)

# RESOURCES

```[Source code](https://github.com/rpm-software-management/createrepo_c)```

<!-- verified: 2026-06-26 -->
