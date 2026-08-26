# TAGLINE

创建软件包的 tarball

# TLDR

**将当前软件包打包**为 .tgz 归档

```bun pm pack```

**打包但不写入磁盘**（试运行）

```bun pm pack --dry-run```

**打包到指定目录**

```bun pm pack --destination [path/to/dir]```

**使用自定义文件名打包**

```bun pm pack --filename [package.tgz]```

**以最简输出打包**（只打印 tarball 名称）

```bun pm pack --quiet```

# SYNOPSIS

**bun** **pm** **pack** [**--dry-run**] [**--destination** _dir_] [**--filename** _name_] [**--ignore-scripts**] [**--gzip-level** _0-9_] [**--quiet**]

# PARAMETERS

**--dry-run**
> 执行所有任务，但不把 tarball 写入磁盘。

**--destination** _dir_
> 指定 tarball 的输出目录。不能与 **--filename** 同时使用。

**--filename** _name_
> 设置 tarball 的确切文件名。不能与 **--destination** 同时使用。

**--ignore-scripts**
> 跳过运行 prepack、postpack 和 prepare 脚本。

**--gzip-level** _0-9_
> 设置 gzip 压缩级别。默认为 **9**（最高压缩）。

**--quiet**
> 只输出 tarball 文件名，抑制详细输出。

# DESCRIPTION

**bun pm pack** 创建一个压缩的 .tgz 归档，其中包含所有将要发布到 npm 的文件，遵循与 npm pack 相同的包含与排除规则。这对于在运行 **bun publish** 之前检查将要发布的内容、测试本地软件包，或在没有软件仓库的情况下共享软件包很有用。

该命令在确定要包含哪些文件时会遵循 package.json 中的 **files** 字段、**.npmignore** 和 **.gitignore**。

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1), [bun-publish](/man/bun-publish)(1)
