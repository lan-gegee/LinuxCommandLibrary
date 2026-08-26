# TAGLINE

在命令行管理 GitHub issues

# TLDR

**列出打开状态的 issues**

```hub issue```

**按标签列出 issues**

```hub issue -l [bug]```

**创建新 issue**（会打开编辑器）

```hub issue create```

**带标题和正文创建**

```hub issue create -m "[title]" -m "[body]"```

**查看特定 issue**

```hub issue show [123]```

**列出指派给某人的 issues**

```hub issue -a [username]```

# SYNOPSIS

**hub issue** [_-a_ _assignee_] [_-c_ _creator_] [_-@_ _user_] [_-s_ _state_] [_-f_ _format_] [_-M_ _milestone_] [_-l_ _labels_] [_-L_ _limit_]

**hub issue show** [_-f_ _format_] _number_

**hub issue create** [**-o**] [**-m** _message_ | **-F** _file_] [**--edit**] [**-a** _users_] [**-M** _milestone_] [**-l** _labels_]

**hub issue transfer** _number_ _repository_

# SUBCOMMANDS

**list**
> 列出当前仓库中的 issues（未指定子命令时的默认行为）。

**show** _number_
> 显示一个已有的 issue。

**create**
> 在当前仓库中新建一个 issue。

**update** _number_
> 更新已有 issue 的字段。

**labels**
> 列出此仓库中可用的标签。

**transfer** _number_ _repository_
> 将一个 issue 转移到其他仓库。

# PARAMETERS

**-a**, **--assignee** _user_
> 列表模式下，只显示指派给 _user_ 的 issues。在创建/更新模式（**--assign**）下，为以逗号分隔的待指派用户列表。

**-c**, **--creator** _user_
> 只显示由 _user_ 创建的 issues。

**-@**, **--mentioned** _user_
> 只显示提及 _user_ 的 issues。

**-s**, **--state** _state_
> 显示状态为 **open**、**closed** 或 **all** 的 issues（默认：open）。

**-f**, **--format** _format_
> 使用占位符自定义输出，例如 %i（编号）、%t（标题）、%S（状态）、%l（标签）、%b（正文）、%au（作者）。

**-M**, **--milestone** _name_
> 只显示属于给定里程碑的 issues。

**-l**, **--labels** _labels_
> 只显示带有给定逗号分隔标签的 issues。

**-d**, **--since** _date_
> 只显示在 _date_（ISO 8601）当天或之后更新过的 issues。

**-L**, **--limit** _n_
> 只显示前 _n_ 个 issues。

**-m**, **--message** _msg_
> issue 的标题/正文文本（可重复使用；第一行为标题）。

**-F**, **--file** _file_
> 从 _file_ 中读取 issue 的标题和描述。

**--edit**
> 提交前先在文本编辑器中编辑标题和描述。

**-o**, **--browse**
> 在 Web 浏览器中打开新 issue，而不是打印其 URL。

**--include-pulls**
> 在显示 issues 的同时一并显示 pull request。

# DESCRIPTION

**hub issue** 用于从命令行管理 GitHub issues。无需离开终端即可列出、创建、更新和查看 issues。

不带参数时，它会按创建日期排序列出当前仓库处于打开状态的 issues。子命令涵盖查看单个 issue、提交新 issue、编辑现有 issue、列出标签，以及将 issue 转移到另一个仓库。

# CAVEATS

属于 **hub** 的一部分，hub 已被弃用，推荐改用官方 GitHub CLI（**gh**）；可以考虑使用 **gh issue**。需要 GitHub 认证。

# INSTALL

```apt: sudo apt install hub```

```pacman: sudo pacman -S hub```

```zypper: sudo zypper install hub```

```brew: brew install hub```

```nix: nix profile install nixpkgs#hub```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[hub](/man/hub)(1), [gh-issue](/man/gh-issue)(1)

# RESOURCES

```[Source code](https://github.com/github/hub)```

```[Homepage](https://hub.github.com/)```

<!-- verified: 2026-07-19 -->
