# TAGLINE

创建隔离的 conda 环境

# TLDR

**创建带 Python 的新环境**

```conda create --name [env_name] python=[3.11]```

**创建含指定软件包的环境**

```conda create --name [env_name] [numpy] [pandas]```

**根据环境文件创建**

```conda create --name [env_name] --file [requirements.txt]```

**在指定路径创建环境**

```conda create --prefix [/path/to/env] python=[3.11]```

**克隆现有环境**

```conda create --name [new_env] --clone [existing_env]```

# SYNOPSIS

**conda** **create** [_options_] [_packages..._]

# PARAMETERS

**-n**, **--name** _name_
> 新环境的名称。

**-p**, **--prefix** _path_
> 环境位置的完整路径。

**--file** _file_
> 从文件读取软件包版本。

**--clone** _env_
> 克隆一个现有环境。

**-c**, **--channel** _channel_
> 搜索软件包时使用的附加频道。

**-y**, **--yes**
> 不请求确认。

# DESCRIPTION

**conda create** 用于初始化一个新的隔离 conda 环境，它是一个自包含的目录结构，包含特定的一组软件包及其依赖。环境是 conda 在同一系统上管理多个项目（其软件包需求可能相互冲突）的基本机制。

创建过程包括指定环境名称（或前缀路径）、所需的 Python 版本以及任何要安装的初始软件包。Conda 会执行依赖解析以确保所有指定的软件包及其依赖彼此兼容，然后将所需的软件包下载并安装到新的环境目录中。环境可以先以最少的软件包创建、之后再扩展，也可以预先指定完整的软件包集合。

--clone 选项提供了一种复制现有环境的方式，适合做实验或创建备份环境。--file 选项允许从文件读取软件包规格，从而实现可复现的环境创建。用 --prefix 创建的环境可以位于文件系统的任意位置，而具名环境（--name）则存放在 conda 默认的 envs 目录中。环境创建后，必须先激活，其中的软件包才会对 shell 可用。

# CAVEATS

环境名称不能包含空格。若要使用默认 envs 目录以外的位置，请使用 **--prefix**。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-activate](/man/conda-activate)(1), [conda-remove](/man/conda-remove)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/create.html)```

<!-- verified: 2026-06-22 -->
