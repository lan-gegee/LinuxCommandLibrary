# TAGLINE

面向主干版本控制与堆叠提交的 Twigg 命令行工具

# TLDR

**显示**仓库状态 / 提交栈

```tw```

**在当前目录初始化** Twigg

```tw init```

**克隆**仓库

```tw clone [user/repo]```

**设置** CLI API 密钥

```tw key [tw_key_...]```

**创建提交**并附带标题

```tw commit "[title]"```

**推送**当前提交栈到服务器

```tw push```

**拉取**已提交到服务器的提交

```tw pull```

**简短状态**（冲突与工作树）

```tw st```

**变基**当前提交到新的父提交

```tw rebase [target]```

**显示版本**

```tw version```

# SYNOPSIS

**tw** [_command_] [_args_...]

# PARAMETERS

**init**
> 在当前目录初始化 Twigg 元数据。

**clone** _user/repo_
> 从 Twigg 服务器克隆仓库（需要时会提示输入 CLI 密钥）。

**key** _CLI_KEY_
> 存储来自用户设置的认证密钥（**tw_key_...**）。

**commit** _title_
> 将已跟踪的文件快照为一个带有给定标题的新本地提交。

**push**
> 推送当前提交及其尚未提交到服务器的父提交，直到遇到已在服务器上的提交为止。可能触发基于路径的 CI。

**pull** [_server_commit_]
> 拉取已提交的提交，或某个特定的待处理服务器提交（服务器 id 语法，如 **c/7**）。

**rebase** [_source_] _target_
> 将 _source_（默认：当前提交 **@**）变基到 _target_ 上。后代提交会自动随之变基。发生冲突时会产生带冲突标记的提交，用 amend 解决，而不是在中途终止整个栈。

**st**, **status**
> 工作树与冲突状态。

**amend**
> 在编辑之后（包括解决冲突后）创建当前提交的新版本。

**restore**, **load**, **server**, **ci-list**
> 恢复之前的提交版本；加载文件而不提交；设置服务器仓库 URL；列出当前提交将会触发的 CI 配置。完整选项见官方文档。

**-a**
> 在默认栈视图中显示所有提交版本 / 历史边（例如变基谱系）。

**version**, **-v**
> 打印 CLI 版本。

# DESCRIPTION

**tw** 是 **Twigg** 的命令行客户端。Twigg 是一个开源版本控制系统和软件 forge（并非 Git 的封装），专为封闭团队协作而构建。默认工作流是主干开发加小型堆叠提交：每个更改都是一个短生命周期的提交，被独立评审和提交，堆叠在父提交之上，而不是使用长期的功能分支。

该 CLI 管理一个本地提交图，包含本地 id（**#N**）、版本（**vM**）、服务器 id（**c/N**），以及当前提交（**@**）。日常工作流是：编辑 → **tw commit** → **tw push** 送审，**tw pull** 更新，需要重新堆叠时使用 **tw rebase**。层级化的 **OWNERS**、集成代码评审和按路径过滤的 CI/CD 都是服务器端的一等功能。

可从 **twigg.vc** 安装预编译的二进制文件（Linux、macOS Intel/Apple Silicon、Windows），或使用 Go 构建：从 monorepo 中执行 **cd tw && go install**。托管服务位于 **https://twigg.vc**；提供可选的 Git 镜像以保证互操作性。源代码与服务器组件采用 AGPL-3.0 许可证。

# CAVEATS

与 Git 命令不兼容同一工作树模型——Twigg 是独立的 VCS。认证使用生成的 CLI 密钥，默认不走 SSH。带冲突的变基会创建含冲突的提交，这些提交会阻塞部分操作，直到通过 **amend** 解决。自托管和本地构建需要完整的 monorepo 技术栈（Go；服务器还需要 node、docker/LXD 等，视情况而定）。首次发布时托管 forge 不支持公开仓库（Twigg 本身使用 GitHub 作为只读源镜像）。

# HISTORY

作为一个从零开发的 VCS 和 forge 而设计，强调大公司风格的主干式堆叠工作流。以 AGPL-3.0 许可证开源发布，文档位于 **twigg.vc/docs**。据报道已在该项目自身开发和合作公司的生产环境中使用。

# SEE ALSO

[git](/man/git)(1), [jj](/man/jj)(1), [hg](/man/hg)(1)

# RESOURCES

```[Source code](https://github.com/twigg-vc/monorepo)```

```[Homepage](https://twigg.vc)```

```[Documentation](https://twigg.vc/docs/v/2/)```

<!-- verified: 2026-07-24 -->
