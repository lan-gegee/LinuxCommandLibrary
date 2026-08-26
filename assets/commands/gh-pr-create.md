# TAGLINE

在 GitHub 上创建新的拉取请求

# TLDR

**以交互方式创建 PR**

```gh pr create```

**带标题和正文创建**

```gh pr create -t "[title]" -b "[body]"```

**创建草稿 PR**

```gh pr create --draft -t "[title]"```

**创建并指定审查者**

```gh pr create -t "[title]" -r [reviewer1],[reviewer2]```

**创建到指定的 base 分支**

```gh pr create --base [main] --head [feature]```

**根据提交自动填充创建**

```gh pr create --fill```

**在浏览器中打开以创建**

```gh pr create -w```

# SYNOPSIS

**gh** **pr** **create** [_options_]

# PARAMETERS

**-t**, **--title** _title_
> PR 标题。

**-b**, **--body** _body_
> PR 正文。

**-d**, **--draft**
> 以草稿形式创建。

**-r**, **--reviewer** _users_
> 请求审查者。

**-a**, **--assignee** _users_
> 指派用户。

**-l**, **--label** _labels_
> 添加标签。

**--base** _branch_
> base 分支。

**--head** _branch_
> head 分支。

**--fill**
> 根据提交自动填充。

**-w**, **--web**
> 在浏览器中打开。

**-R**, **--repo** _owner/repo_
> 仓库。

# DESCRIPTION

**gh pr create** 在命令行中于 GitHub 上创建拉取请求。它会检测当前分支上下文并提供多种输入模式，从而精简 PR 创建流程。

不带参数运行时，命令会交互式提示填写标题、正文和元数据。--fill 标志会用第一条提交信息自动填充标题，并用分支分叉以来的所有提交信息填充正文。草稿 PR（--draft）允许推送进行中的变更以尽早获得反馈，而不必正式请求审查。

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

[gh-pr](/man/gh-pr)(1), [gh](/man/gh)(1)
