# TAGLINE

带语法高亮的 git diff 审阅终端 TUI

# TLDR

**审阅**未暂存的工作区变更

```critique```

仅审阅**已暂存**的变更

```critique --staged```

审阅**自某个 ref 以来**或两个 ref 之间的变更

```critique [main]
critique [main] [HEAD]```

审阅**单个提交**

```critique --commit [abc1234]```

**监视**工作区并在文件变化时刷新

```critique --watch```

**按 glob 模式过滤**文件

```critique --filter "[src/**/*.ts]"```

将 **Web 预览**上传到 critique.work

```critique --web "[title]"```

为当前 diff 生成 **AI 代码审查**

```critique review --agent [claude|opencode]```

# SYNOPSIS

**critique** [_options_] [_ref_ [_ref2_]]

**critique review** [_options_] [_ref_]

# PARAMETERS

**--staged**
> 仅显示已暂存的变更

**--commit** _ref_
> 显示某个提交所引入的变更

**--watch**
> 文件变化时刷新视图

**--filter** _pattern_
> 将审阅范围限定在匹配 glob 的文件（可重复指定）

**--web** [_title_]
> 将可分享的 Web 预览上传到 critique.work

**--pdf** [_filename_]
> 将 diff 或审查结果生成为 PDF

**--stdin**
> 从标准输入读取补丁（例如作为 git 分页器使用）

**--agent** _name_
> 用于 **critique review**：选择 **opencode** 或 **claude**

# DESCRIPTION

**critique** 是一个用于审阅 Git 变更的终端用户界面。它遵循与 **git diff** 相同的心智模型：不带参数时显示工作区（包括未跟踪文件）；**--staged** 显示暂存区；给定一个或两个 ref 则按常规方式比较历史。

该 TUI 使用 Tree-sitter 进行语法高亮，支持词级 diff、分屏或统一布局，以及在文件之间用键盘导航。可选功能包括把预览上传到 **critique.work**、导出适合电子阅读器的 PDF，或者通过 OpenCode 或 Claude Code 运行 **critique review** 以获得 AI 讲解。

它需要 **Bun**（而非 Node.js）。可用 **bun install -g critique** 安装，或通过 **bunx critique** 运行。

# CAVEATS

需要 Bun。Web 上传会把渲染后的 diff HTML 和原始补丁发送到 critique.work（除非获得授权，否则上传内容会过期）。锁文件以及非常大的文件 diff 可能会被自动隐藏。

# SEE ALSO

[git-diff](/man/git-diff)(1), [delta](/man/delta)(1), [lazygit](/man/lazygit)(1)

# RESOURCES

```[Source code](https://github.com/remorses/critique)```

```[Homepage](https://critique.work)```

<!-- verified: 2026-07-14 -->

# INSTALL

```aur: yay -S critique```

<!-- packages: 2026-07-22 -->
