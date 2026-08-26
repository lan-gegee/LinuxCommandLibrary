# TAGLINE

在 Git 仓库之间转换并迁移代码

# TLDR

**执行迁移**（迁移逻辑定义在 Copybara 配置文件中）

```copybara migrate [copy.bara.sky]```

**校验** Copybara 配置而不实际应用更改

```copybara validate [copy.bara.sky]```

**查看**配置中的工作流及 origin/destination 详情

```copybara info [copy.bara.sky]```

**重新生成**一个未能干净应用的变更

```copybara regenerate [copy.bara.sky] [workflow] [change-id]```

# SYNOPSIS

**copybara** [_subcommand_] [_options_] _config-file_ [_workflow_] [_source-ref_]

# PARAMETERS

**migrate**
> 应用所配置的工作流：从 origin 拉取变更、运行转换，然后推送到 destination。未指定子命令时这是默认行为。

**validate**
> 解析并检查配置文件的错误，不触碰任何仓库。

**info**
> 打印关于工作流、origin、destination 以及最近迁移修订版的元数据。

**regenerate**
> 针对特定变更重新运行迁移，适用于发生合并冲突或应用失败之后。

**--force**
> 即使安全检查通常会阻止运行也继续执行。

**--init-history**
> 为新工作流在 destination 上初始化迁移历史。

**--dry-run**
> 在本地执行转换但不推送到 destination。

# DESCRIPTION

**copybara** 是一个用于**在仓库之间转换和迁移源代码**的工具。它可用于让公开镜像与内部代码库保持同步、把上游变更导入 fork，或者执行一次性的代码迁移，同时完成路径重写、元数据清理和作者映射。

工作流在 **Starlark** 配置文件中定义（通常命名为 **copy.bara.sky**）。每个工作流指定一个 **origin**（读取变更之处）、一个 **destination**（写入变更之处）、文件过滤器，以及一组 **transformations**（如 **core.move**、**core.replace** 和 **core.remove**）。Copybara 是**无状态**的：迁移进度以标签形式存储在 destination 仓库的提交信息中，因此多个用户可以安全地运行同一工作流。

该工具以 **Git** 作为主要 VCS，并对 **Mercurial** 提供实验性的只读支持。Origin 和 destination 可以指向 GitHub、Gerrit、本地路径、HTTP 端点以及其他可插拔后端。常见模式包括 squash 模式的公开镜像、把贡献者的 PR cherry-pick 到权威仓库，以及自动化的子树导入。

# CAVEATS

使用官方发布 JAR 时，Copybara 需要 **Java 21+**。配置错误往往只有在针对真实仓库运行时才会暴露；大规模迁移前请先运行 **validate**。转换功能强大但容易出细微差错——请先在一次性克隆上测试。Mercurial 及部分 destination 类型仍属实验性。

# HISTORY

该项目最初在 **Google** 内部开发，用于管理同步的公开与私有代码库，随后开源。它用声明式、可评审的 Starlark 配置模型取代了临时编写的镜像脚本，如今被 Google 内部广泛使用，也被外部项目用于向 GitHub 镜像代码。

# INSTALL

```nix: nix profile install nixpkgs#copybara```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-filter-repo](/man/git-filter-repo)(1)

# RESOURCES

```[Source code](https://github.com/google/copybara)```

```[Documentation](https://github.com/google/copybara/blob/master/docs/reference.md)```

<!-- verified: 2026-07-11 -->
