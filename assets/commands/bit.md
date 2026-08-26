# TAGLINE

带简化命令的现代 Git CLI 包装器

# TLDR

**将更改保存到当前分支**

```bit save```

**与远程同步**并推送更改

```bit sync```

**与指定分支同步**

```bit sync origin [master]```

**切换分支**（不存在则创建）

```bit switch [branch-name]```

带分支选择的**交互式 checkout**

```bit checkout```

以交互选择方式**添加文件**

```bit add```

**带消息提交**（标准 git）

```bit commit -m "[message]"```

# SYNOPSIS

**bit** [_command_] [_arguments_]

# DESCRIPTION

**bit** 是一个现代 Git CLI 包装器，提供简化的命令、智能默认值和交互式提示。它构建于 git 之上，与标准 git 命令保持完全兼容。

该工具将常见的 git 工作流简化为更简单的命令，同时提供建议、文件和分支的自动补全，以及自动 fetch/快进以减少合并冲突。

# SUBCOMMANDS

**save**
> 将更改保存到当前分支（智能提交，可选 amend）

**sync**
> 以 rebase 方式拉取并推送；可选择与其他分支同步

**switch**
> 切换分支，若分支不存在会提示创建

**checkout**
> 交互式分支/文件检出

**add**
> 交互式暂存文件

**pr**
> 以交互方式查看和检出 GitHub 拉取请求

**release**
> 更新标签并创建发布

**info**
> 显示 git 统计信息和配置

**update**
> 将 bit CLI 自身更新到最新版本

**complete**
> 生成 shell 补全

所有标准 **git** 命令也都可以通过 bit 使用。

# PARAMETERS

所有 git 参数均可用于 bit。常用的包括：

**-m** _message_
> 提交消息（配合 bit commit）

**-a**
> 暂存所有已修改的文件

**--amend**
> 修订上一次提交

**-r**
> 拉取时进行变基（rebase）

# CAVEATS

安装需要配置好 GOPATH 和 GOBIN 的 Go 环境。**save** 命令可能通过修订提交重写历史；在共享分支上使用需谨慎。Bit 是实验性软件，在边缘情况下可能出现意外行为。

# HISTORY

bit 由 **Chris Walz** 于 **2020 年**创建，是一项现代化 git CLI 体验的实验。它的目标是在为高级用户保留完整 git 兼容性的前提下，降低常见 git 操作的复杂度。

# INSTALL

```brew: brew install bit```

```nix: nix profile install nixpkgs#bit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [tig](/man/tig)(1), [lazygit](/man/lazygit)(1)

# RESOURCES

```[Source code](https://github.com/chriswalz/bit)```

<!-- verified: 2026-06-19 -->
