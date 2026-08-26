# TAGLINE

管理 issue 和 PR 标签

# TLDR

**列出当前仓库中的标签**

```gh label list```

**用搜索查询列出标签**

```gh label list --search "[bug]"```

**创建带颜色和描述的标签**

```gh label create [name] -c [color] -d "[description]"```

**编辑标签名称**

```gh label edit [name] --name [new_name]```

**编辑标签的颜色和描述**

```gh label edit [name] -c [ff0000] -d "[new description]"```

**删除标签**（需确认）

```gh label delete [name]```

**从另一个仓库克隆标签**

```gh label clone [owner/repo]```

**强制克隆标签**，覆盖已有标签

```gh label clone [owner/repo] --force```

# SYNOPSIS

**gh** **label** _command_ [_options_]

# SUBCOMMANDS

**list**
> 列出仓库中的标签。

**create**
> 创建新标签。

**edit**
> 编辑现有标签。

**delete**
> 删除标签。

**clone**
> 从另一个仓库克隆标签。

# PARAMETERS

**-c**, **--color** _color_
> 标签颜色，十六进制值（不带 # 前缀）。

**-d**, **--description** _text_
> 标签描述文本。

**--name** _name_
> 新标签名称（配合 edit 使用）。

**--force**
> 克隆时覆盖现有标签。

**--search** _query_
> 按搜索查询过滤标签。

**-L**, **--limit** _int_
> 最多列出的标签数量（默认 30）。

**--sort** _field_
> 排序依据：created、name（默认：created）。

**--order** _direction_
> 排序方向：asc、desc（默认：asc）。

**-w**, **--web**
> 在网页浏览器中打开标签页面。

**-R**, **--repo** _owner/repo_
> 选择其他仓库。

# DESCRIPTION

**gh label** 用于管理仓库标签，对 issue 和拉取请求进行分类与过滤。标签通过可自定义的颜色和描述提供直观的组织方式，帮助团队分诊工作并跟踪 issue 类型。

常见标签模式包括 bug/feature 分类、优先级、状态指示和领域标记。**clone** 命令可以从另一个仓库复制整套标签方案，适合在项目之间保持一致，或用于初始化新仓库。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-issue](/man/gh-issue)(1), [gh-pr](/man/gh-pr)(1)
