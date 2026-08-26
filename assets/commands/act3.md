# TAGLINE

一览 GitHub Actions 最近 3 次运行

# TLDR

**查看当前仓库中所有工作流的最近 3 次运行**

```act3```

**查看特定仓库的运行**

```act3 -r [owner/repo]```

**以表格格式输出结果**

```act3 --format table```

**在浏览器中打开失败的工作流页面**

```act3 -o```

# SYNOPSIS

**act3** [_options_]

# PARAMETERS

**-r** _repo_
> 指定 GitHub 仓库（owner/repo 格式）

**-o**
> 在浏览器中打开失败的工作流运行页面

**--format** _format_
> 输出格式：table 或 html

# DESCRIPTION

**act3** 是一个命令行工具，可直接在终端中显示最近三次 GitHub Actions 工作流运行的结果。它会自动从当前目录检测 GitHub 仓库，并显示近期运行的状态（成功、失败、已取消），无需打开 GitHub 网页界面即可快速了解概况。

它用 Go 编写，适合希望不离开终端就能监控 CI/CD 流水线的开发者。还支持 HTML 输出，用于生成可分享的报告。

# CAVEATS

需要有效的 GitHub token 才能访问 API。每个工作流只显示最近三次运行。属于早期软件，功能仍在开发中。

# HISTORY

**act3** 由 **Dhruva Thakur**（dhth）创建，是在 GitHub 上以 MIT 许可证发布的开源 Go 项目。

# INSTALL

```nix: nix profile install nixpkgs#act3```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[gh](/man/gh)(1), [act](/man/act)(1)
