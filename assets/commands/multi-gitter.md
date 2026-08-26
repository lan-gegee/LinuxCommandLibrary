# TAGLINE

跨大量 Git 仓库批量执行脚本化修改

# TLDR

**运行脚本**并在匹配的仓库上创建 PR

```multi-gitter run [./script.sh] --org [my-org] --branch [chore/update] --pr-title "[title]"```

**合并** multi-gitter 创建的开放 PR

```multi-gitter merge --org [my-org]```

查看此前各次运行的**状态**

```multi-gitter status --org [my-org]```

**关闭** PR

```multi-gitter close --org [my-org]```

# SYNOPSIS

**multi-gitter** *command* [*options*]

# DESCRIPTION

**multi-gitter** 会克隆许多仓库（按组织、用户或显式列表），在每个仓库中运行脚本、提交更改、推送分支并创建拉取请求。非常适合在整个仓库群中进行依赖版本升级、重命名或 CI 文件更新等操作。通过令牌支持 GitHub 和 GitLab。

# PARAMETERS

**run** *script*

> 在每个仓库中执行脚本；当文件发生变化时创建提交/PR。

**merge** / **close** / **status** / **print**

> 管理生成的拉取请求。

**--org** / **--user** / **--repo**

> 选择目标仓库。

**--branch** / **--pr-title** / **--pr-body**

> PR 元数据。

**--dry-run**

> 仅预览，不推送。

身份验证通过 **GITHUB_TOKEN** 或提供方相关标志完成——详见 **multi-gitter --help**。

# CAVEATS

脚本会以你的凭据运行；务必仔细审查脚本内容。速率限制和分支保护可能阻碍合并。克隆占用的磁盘空间会随组织规模增长。

# INSTALL

```brew: brew install multi-gitter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [gh](/man/gh)(1), [git-xargs](/man/git-xargs)(1)

# RESOURCES

```[Source code](https://github.com/lindell/multi-gitter)```

<!-- verified: 2026-07-19 -->
