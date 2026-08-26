# TAGLINE

显示 Angular CLI 及相关软件包的版本

# TLDR

**显示 Angular 版本信息**

```ng version```

**以 JSON 格式显示版本**

```ng version --json```

# SYNOPSIS

**ng** **version** [_options_]

# PARAMETERS

**--json**
> 以 JSON 格式输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ng version** 显示 Angular CLI 及各软件包的版本，包括 `@angular/core`、`@angular/cli`、RxJS、TypeScript、Node.js 以及正在使用的包管理器。在 Angular 工作区之外运行时，只输出全局安装的 CLI 信息。`v` 可作为简写别名（`ng v`）。

该输出适用于报告 bug、审计依赖版本或排查构建问题等场景。

# CAVEATS

属于 Angular CLI 的一部分。便于故障排查。显示的是本地项目的版本。

# HISTORY

ng version 是 **Angular CLI** 的一部分，用于显示版本信息和依赖详情。

# SEE ALSO

[ng](/man/ng)(1), [node](/man/node)(1), [npm](/man/npm)(1)
