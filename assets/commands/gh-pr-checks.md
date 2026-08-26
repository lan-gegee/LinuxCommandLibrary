# TAGLINE

显示拉取请求上的 CI 检查状态

# TLDR

**查看当前分支 PR 的检查**

```gh pr checks```

**查看特定 PR 的检查**

```gh pr checks [pr-number]```

**持续监视检查直到完成**

```gh pr checks --watch```

**监视检查并在首次失败时退出**

```gh pr checks --watch --fail-fast```

**只显示必需检查**

```gh pr checks --required```

**以 JSON 输出检查结果**

```gh pr checks --json [name,state,bucket]```

**在网页浏览器中打开检查详情**

```gh pr checks --web```

# SYNOPSIS

**gh pr checks** [_number_ | _url_ | _branch_] [_options_]

# PARAMETERS

_number_ | _url_ | _branch_
> 拉取请求编号、URL 或分支名（默认为当前分支）。

**--watch**
> 持续监视检查直到全部结束。

**-i**, **--interval** _SECONDS_
> 监视时的刷新间隔（秒）（默认 10）。

**--fail-fast**
> 首次检查失败即退出监视模式。

**--required**
> 只显示必需的检查。

**-w**, **--web**
> 打开网页浏览器查看检查详情。

**--json** _fields_
> 输出包含指定字段的 JSON。可用字段：bucket、completedAt、description、event、link、name、startedAt、state、workflow。

**-q**, **--jq** _expression_
> 使用 jq 表达式过滤 JSON 输出。

**-t**, **--template** _string_
> 使用 Go template 格式化 JSON 输出。

**-R**, **--repo** _OWNER/REPO_
> 以 [HOST/]OWNER/REPO 格式选择其他仓库。

# DESCRIPTION

**gh pr checks** 显示拉取请求上 CI 检查和状态检查的情况，包括每项检查的名称、状态（pending、passing、failing）以及结论。

监视模式可以等待检查全部完成，适合只有在 CI 成功运行后才继续执行的脚本。该命令可与 GitHub Actions 及第三方 CI 服务集成。使用 **--json** 时，**bucket** 字段会把状态归类为 pass、fail、pending、skipping 或 cancel。

# CAVEATS

只显示已上报到 GitHub 的检查。某些 CI 系统的上报可能有延迟。**--fail-fast** 标志必须与 **--watch** 配合使用。监视模式受 API 速率限制约束。

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

[gh-pr](/man/gh-pr)(1), [gh-pr-merge](/man/gh-pr-merge)(1), [gh-run](/man/gh-run)(1), [gh-pr-view](/man/gh-pr-view)(1)
