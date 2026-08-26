# TAGLINE

管理 conda 环境

# TLDR

**列出所有环境**

```conda env list```

**将当前环境导出到 YAML 文件**

```conda env export > [environment.yml]```

**仅导出显式安装的软件包**

```conda env export --from-history > [environment.yml]```

**根据 YAML 文件创建环境**

```conda env create -f [environment.yml]```

**根据文件以指定名称创建环境**

```conda env create -n [env_name] -f [environment.yml]```

**移除一个环境**

```conda env remove --name [env_name]```

**根据 YAML 文件更新环境**

```conda env update -f [environment.yml]```

# SYNOPSIS

**conda** **env** _subcommand_ [_options_]

# PARAMETERS

**list**
> 列出所有 conda 环境。

**create**
> 根据 YAML 规格文件创建环境。

**export**
> 将环境定义导出为 YAML。

**remove**
> 彻底移除一个环境。

**update**
> 根据 YAML 文件更新现有环境。

**config**
> 配置环境专属变量。

**-n** _NAME_, **--name** _NAME_
> 要操作的环境名称。

**-f** _FILE_, **--file** _FILE_
> 环境 YAML 文件的路径。

**--from-history**
> （export）只包含用户显式安装的软件包。

**--no-builds**
> （export）从导出的依赖中移除构建规格。

# DESCRIPTION

**conda env** 管理 conda 环境，包括根据规格文件创建、导出和移除环境。**environment.yml** 格式支持可复现的环境定义，可以包含 conda 软件包、pip 软件包和频道规格。

使用 **export --from-history** 可生成跨平台的环境文件，其中只列出显式请求的软件包，而不是所有已解析的依赖。

# CAVEATS

**--from-history** 旗标仅适用于结构化格式（YAML、JSON），不适用于 explicit 或 requirements 格式。除非在导出时使用了 **--from-history** 或 **--no-builds**，否则环境文件可能无法跨平台移植。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-create](/man/conda-create)(1), [conda-activate](/man/conda-activate)(1), [conda-install](/man/conda-install)(1), [conda-list](/man/conda-list)(1)
