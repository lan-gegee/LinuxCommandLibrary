# TAGLINE

加固 npm、pnpm、yarn、bun 和 uv 配置，防范供应链风险

# TLDR

**启动**交互式 TUI 进行扫描并应用修复

```depsguard```

**仅扫描**并输出只读报告

```depsguard scan```

**跳过递归文件发现**，只检查本地配置

```depsguard --no-search```

**恢复** depsguard 之前创建的备份

```depsguard restore```

**显示**帮助

```depsguard --help```

# SYNOPSIS

**depsguard** [_scan_|_restore_] [_options_]

# DESCRIPTION

**depsguard** 是一个 Rust 编写的 CLI 工具，用于审计 JavaScript 和 Python 包管理器的配置文件是否具备供应链加固设置，并在用户明确批准后应用缺失的保护措施。

它会检查用户级文件如 `~/.npmrc`、`~/.yarnrc.yml`、`~/.bunfig.toml` 和 `uv.toml`，以及仓库级文件如 `package.json`、lockfile、Renovate 配置和 Dependabot 配置。它检查的设置包括：最小发布时长（延迟安装新发布的版本）、禁止安装脚本、限制特殊的传递依赖、信任策略以及严格的构建要求。

在默认的交互模式下，depsguard 通过 TUI 展示检测到的问题，让用户选择要应用的修复项，并在修改任何文件之前先在 `~/.depsguard/backups/` 下写入带时间戳的备份。`restore` 子命令可回放选定的备份。

该工具本身从不安装软件包，且不带任何第三方 crate 依赖。

# PARAMETERS

**scan**
> 只读报告。不会修改任何文件。

**restore**
> 从带时间戳的备份中恢复配置。

**--no-search**
> 仅检查当前目录中的本地配置文件。跳过递归发现。

**--help**
> 显示 CLI 文档。

# CONFIGURATION

每次执行 apply 操作前都会将备份写入 `~/.depsguard/backups/`。

# CAVEATS

部分加固选项要求较新的包管理器版本（例如某些标志需要 npm 11.10 或更高版本）。建议使用支持 VT 的终端以正确渲染 TUI。从源码构建需要 Rust 1.74 或更高版本。

# INSTALL

```brew: brew install depsguard```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [pnpm](/man/pnpm)(1), [yarn](/man/yarn)(1), [bun](/man/bun)(1), [uv](/man/uv)(1)
