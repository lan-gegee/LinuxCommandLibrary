# TAGLINE

克隆远程仓库

# TLDR

**克隆仓库**

```git clone [https://github.com/owner/repo.git]```

**克隆到指定目录**

```git clone [url] [directory]```

**浅克隆**

```git clone --depth 1 [url]```

**克隆特定分支**

```git clone --branch [branch] [url]```

**连同子模块一起克隆**

```git clone --recursive [url]```

# SYNOPSIS

**git clone** [_options_] _repository_ [_directory_]

# PARAMETERS

_REPOSITORY_
> 仓库 URL 或路径。

_DIRECTORY_
> 目标目录名。

**--depth** _N_
> 创建只含 N 个提交的浅克隆。

**--branch** _BRANCH_
> 克隆特定分支。

**--recursive**
> 初始化子模块。

**--bare**
> 创建裸仓库。

**--mirror**
> 创建镜像克隆。

**--single-branch**
> 只克隆一个分支。

**-o**, **--origin** _NAME_
> 用 NAME 作为上游远程名，替代 "origin"。

**-j**, **--jobs** _N_
> 并行克隆子模块，使用 N 个任务。

**--filter** _SPEC_
> 部分克隆：按需获取对象，例如 **--filter=blob:none**。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git clone** 创建远程仓库的完整副本，建立一个包含全部版本历史、分支和标签的本地工作目录。它会自动设置 origin 远程，并为远程分支配置跟踪分支。

该命令支持多种传输协议，包括 HTTPS（公共仓库的标准选择）、SSH（需要身份验证时的首选）和 git:// 协议（只读）。克隆时，Git 默认抓取所有提交、分支和标签，形成仓库历史的完整镜像。

浅克隆（--depth）适用于不需要完整历史的大型仓库，例如 CI/CD 环境或部署场景。由于只抓取最近的提交，它能显著减少下载时间和磁盘占用。不过浅克隆存在局限：变基或查看旧历史等操作可能失败，或需要额外抓取更多深度。

裸仓库（--bare）只包含 Git 数据而没有工作目录，适合服务器端托管或备份用途。镜像克隆（--mirror）与裸克隆类似，但还会复制包括远程引用在内的所有引用和配置，非常适合创建完整的仓库备份。

--recursive 选项会递归地初始化并更新所有 Git 子模块，这在处理依赖外部仓库的项目时必不可少。不加此选项时，克隆后子模块目录将是空的。

# CAVEATS

大型仓库可能耗时较长。浅克隆会限制部分操作。SSH 需要先配置密钥。

# HISTORY

git clone 是 **Git** 自最初发布就存在的基础命令，提供了定义 git 模型的分布式仓库复制能力。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-fetch](/man/git-fetch)(1), [git-remote](/man/git-remote)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-clone)```

<!-- verified: 2026-07-17 -->
