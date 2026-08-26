# TAGLINE

用选择器查询依赖图

# TLDR

**查询依赖**

```npm query "[name=lodash]"```

**查找开发依赖**

```npm query ":type(dev)"```

**查找过时的软件包**

```npm query ":outdated(major)"```

**查找有漏洞的软件包**

```npm query ":vuln"```

**复杂查询**

```npm query "[name^=@babel]"```

# SYNOPSIS

**npm** **query** _selector_

# PARAMETERS

_SELECTOR_
> 类似 CSS 的查询选择器。支持伪类（`:root`、`:type(dev)`、`:outdated`、`:deprecated`、`:vuln`、`:attr`、`:semver`、`:path`）、属性选择器（`[name=foo]`、`[name^=@scope]`、`[keywords=cli]`）和组合器（` `、`>`、`,`）。

**--global**
> 查询全局安装的包树而非项目。

**--workspace** _NAME_
> 将查询限制到给定的工作区。

**--workspaces**
> 应用到所有工作区。

**--include-workspace-root**
> 在结果中包含工作区根软件包。

**--package-lock-only**
> 仅从 `package-lock.json` 读取，不触碰 `node_modules`。

**--expect-result-count** _N_, **--expect-results** _BOOL_
> 当结果数量不匹配时让 npm 以非零码退出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm query** 用选择器查询依赖图，为软件包提供类似 CSS 的语法。

该命令用于过滤依赖，是强大的软件包搜索工具。

# CAVEATS

使用 CSS 选择器语法。在 npm 8.16 中加入。支持复杂查询。

# HISTORY

npm query 的加入是为了提供对依赖树的**类 CSS 查询**能力。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-ls](/man/npm-ls)(1), [npm-explain](/man/npm-explain)(1)
