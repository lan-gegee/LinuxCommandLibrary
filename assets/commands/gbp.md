# TAGLINE

Debian 软件包构建的 Git 集成工具

# TLDR

**将现有 Debian 源码包导入 Git**

```gbp import-dsc [path/to/package.dsc]```

**使用默认构建器构建软件包**

```gbp buildpackage -jauto -us -uc```

**在 pbuilder 环境中构建软件包**

```DIST=bullseye ARCH=amd64 gbp buildpackage -jauto -us -uc --git-builder=git-pbuilder```

**导入新的上游发行版**

```gbp import-orig --pristine-tar [path/to/package.tar.gz]```

**克隆带 gbp 分支跟踪的仓库**

```gbp clone [url]```

**根据 Git 提交生成 changelog 条目**

```gbp dch --auto```

**在 Git 中标记当前 Debian 发行版本**

```gbp tag```

**将打包分支和标签推送到远程**

```gbp push```

# SYNOPSIS

**gbp** _command_ [_options_]

# PARAMETERS

**buildpackage**
> 从 Git 仓库构建 Debian 源码包和二进制包。

**import-dsc**
> 将现有 Debian 源码包导入 Git 仓库。

**import-orig**
> 将新的上游源码 tarball 导入 Git 仓库。

**export-orig**
> 从 Git 仓库重新生成上游 tarball。

**clone**
> 克隆 Git 仓库并设置 gbp 跟踪分支。

**pull**
> 从远程更新仓库，感知打包分支的跟踪关系。

**push**
> 推送到远程仓库，感知打包分支的跟踪关系。

**dch**
> 根据 Git 提交历史生成 debian/changelog 条目。

**tag**
> 在 Git 仓库中为 Debian 发行版本打标签。

**pq**
> 将 debian/patches 作为 Git 主题分支管理（补丁队列）。

**create-remote-repo**
> 创建远程 Git 仓库并将本地仓库推送进去。

**import-dscs**
> 按版本排序，将多个 Debian 源码包导入 Git 仓库。

# CONFIGURATION

**debian/gbp.conf**
> 项目级设置，包括分支名、构建选项和 pristine-tar 配置。

**~/.gbp.conf**
> 用户级默认设置，作用于所有项目中的 gbp 行为。

# DESCRIPTION

**gbp**（git-buildpackage）将 Debian 软件包构建与 Git 版本控制集成在一起。它为上游源码、Debian 打包以及可选的原始 tarball 维护独立的 Git 分支，为软件包维护提供清晰的工作流。

典型工作流是：用 **gbp import-orig** 导入上游发行版，在 debian 分支上进行打包修改，再用 **gbp buildpackage** 构建。该工具负责合并上游变更并生成规范的 Debian 源码包。

gbp 支持通过 pbuilder、sbuild 或 cowbuilder 在干净环境中构建，实现可重现的构建。

# CAVEATS

需要同时理解 Git 分支和 Debian 打包。必须遵循分支命名约定（upstream、debian、pristine-tar）。复杂的合并场景可能需要手动干预。以 **--git-** 为前缀的选项由 gbp 自身处理；其他选项会透传给底层构建命令。

# HISTORY

git-buildpackage 由 Guido Gunther 创建，约于 **2007 年**首次发布。它已成为 Debian 开发者的标准工具，让他们既能享受 Git 分布式版本控制的优势，又能沿用 Debian 的打包体系。

# SEE ALSO

[debuild](/man/debuild)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1), [pbuilder](/man/pbuilder)(8), [sbuild](/man/sbuild)(1), [git](/man/git)(1)
