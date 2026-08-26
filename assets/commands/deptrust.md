# TAGLINE

多生态软件包漏洞检查器

# TLDR

**检查指定版本的软件包**

```deptrust check npm lodash 4.17.20```

**检查最新版本**

```deptrust check pypi requests latest```

**以 JSON 格式输出结果**

```deptrust check --json cargo serde latest```

**建议最安全的可用版本**

```deptrust suggest npm lodash```

**比较两个版本**

```deptrust compare npm lodash 4.17.20 4.17.21```

# SYNOPSIS

**deptrust** _command_ [_ecosystem_] [_package_] [_version_]

# PARAMETERS

**check**
> 查询某个软件包版本的已知漏洞。

**suggest**
> 返回获得 **allow** 建议的最新版本。

**compare**
> 比较同一软件包两个版本之间的风险。

**version**
> 显示已安装的 **deptrust** 版本。

**mcp**
> 启动用于 agent 集成的 MCP 服务器。

**--json**
> 输出结构化的 JSON 结果。

# DESCRIPTION

**deptrust** 是一个 Go 编写的 CLI 工具，可跨 npm、PyPI、crates.io、Go modules、RubyGems、NuGet、Maven、Packagist、pub.dev、CocoaPods、Hex.pm、Hackage 和 GitHub Actions 检查软件包版本的已知漏洞。它直接查询 OSV 与 GitHub 安全公告数据库——无需任何托管的 deptrust 服务。

每次检查都会返回一个**建议**：**block**（严重/高危）、**review**（中等风险/未知或刚发布）或 **allow**（未发现阻塞性漏洞）。**allow** 并不证明该软件包是安全的。JSON 输出包含安全公告覆盖情况、风险评分、漏洞详情以及数据源错误信息。

它也可以作为本地 MCP 服务器运行，并通过安装钩子与 Codex 和 Claude Code 集成，在软件包命令执行前对其进行审查。

# CAVEATS

各数据源的覆盖范围因生态系统而异；覆盖不全或缺失时返回 **unknown**，不应视为安全。GitHub Actions 的分支引用和仅含主版本号的标签即使技术上有效，也会增加 review 信号。

# SEE ALSO

[npm-audit](/man/npm-audit)(1), [osv-scanner](/man/osv-scanner)(1), [snyk](/man/snyk)(1)

# RESOURCES

```[Source code](https://github.com/clidey/deptrust)```

<!-- verified: 2026-07-11 -->
