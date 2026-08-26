# TAGLINE

在终端中跟踪 GitHub pull request 的 TUI 工具

# TLDR

**使用配置文件启动**（默认进入 query 模式）

```prs```

**以 query 模式运行**，使用 GitHub 搜索语法

```prs -q '[type:pr author:@me state:open]'```

**以 repos 模式运行**，显式指定仓库列表

```prs -m repos --repos='[owner/repo1,owner/repo2]'```

**限制结果数量**

```prs -q '[type:pr state:open]' -n [30]```

**使用自定义配置文件**

```prs --config-path [path/to/prs.yml]```

# SYNOPSIS

**prs** [_options_]

# PARAMETERS

**-m**, **--mode** _MODE_
> 运行模式：`query`（用 GitHub 搜索语法检索 PR，默认）或 `repos`（浏览预定义的仓库列表）。

**-q**, **--query** _QUERY_
> query 模式下运行的 GitHub 搜索查询。语法与 github.com 的 PR 搜索相同。

**--repos** _LIST_
> repos 模式使用的 `owner/repo` 条目列表，以逗号分隔。

**-n**, **--num** _N_
> 每页获取的最大 PR 数量。

**--config-path** _FILE_
> YAML 配置文件的路径（默认 `~/.config/prs/prs.yml`）。

**-h**, **--help**
> 显示帮助。

# CONFIGURATION

配置来源及其优先级：命令行标志 → 环境变量（`PRS_QUERY`、`PRS_REPOS`、`PRS_MODE`、`PRS_NUM`）→ YAML 配置文件。

YAML 文件可存放可复用的查询和仓库列表，这样 `prs` 无需参数即可启动。

# KEYBOARD SHORTCUTS

**通用**

- `q` / `esc` / `ctrl+c` — 返回
- `Q` — 从任意位置退出
- `?` — 打开帮助视图

**PR 列表视图**

- `⏎` / `tab` — 切换到时间线视图
- `ctrl+s` — 切换到仓库列表（repos 模式）
- `d` — 打开 PR 详情
- `ctrl+d` — 显示 PR diff
- `ctrl+v` — 使用 `gh` 显示 PR 详情
- `ctrl+r` — 重新加载列表
- `ctrl+b` — 在浏览器中打开 PR

**详情 / 时间线**

- `h` / `l` / `←` / `→` — 在各区块间导航
- `J` / `K` / `[` / `]` — 在 PR 之间移动

# DESCRIPTION

**prs** 是一个终端用户界面工具，让你无需离开终端即可查看 GitHub pull request。query 模式可以执行任意的 GitHub PR 搜索；repos 模式则遍历一组精选的仓库列表并显示每个仓库的开放 PR。该工具的部分操作（详情、diff 查看）会调用 `gh` 完成，列表获取则使用 GitHub API。

# CAVEATS

需要通过 `gh` CLI 或环境变量中的 `GITHUB_TOKEN` 进行身份验证。获取大量结果时受 API 速率限制约束。

# HISTORY

**prs** 由 **dhth** 创建，使用 **Go** 编写。源代码位于 github.com/dhth/prs。

# INSTALL

```apt: sudo apt install prs```

```brew: brew install prs```

```nix: nix profile install nixpkgs#prs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [git](/man/git)(1), [hub](/man/hub)(1)
