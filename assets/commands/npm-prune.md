# TAGLINE

移除不在依赖中的软件包

# TLDR

**移除多余的软件包**

```npm prune```

**移除 devDependencies**

```npm prune --omit=dev```

**试运行以查看将被移除的内容**

```npm prune --dry-run```

**以 JSON 格式输出结果**

```npm prune --json```

**修剪指定的软件包**

```npm prune [package_name]```

# SYNOPSIS

**npm** **prune** [[_@scope/_]_pkg_...] [_options_]

# PARAMETERS

**--omit** _type_
> 要省略的依赖类型：dev、optional 或 peer。可多次设置。

**--dry-run**
> 只显示将被移除的内容而不做更改。

**--json**
> 以 JSON 格式输出结果。

**--production**
> 已弃用，是 --omit=dev 的别名。

# DESCRIPTION

**npm prune** 移除项目依赖树中未列出的多余软件包。多余软件包指已安装但未被 **package.json** 或任何依赖的 package.json 引用的软件包。

如果指定了 **--omit=dev**，或将 **NODE_ENV** 环境变量设为 **production**，devDependencies 也会被移除。这有助于准备生产环境部署。

提供软件包名时，只在该软件包为多余软件包的前提下对其进行修剪。

# CAVEATS

请先用 **--dry-run** 确认将要移除的内容。**--production** 标志已弃用，请改用 **--omit=dev**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [npm-ls](/man/npm-ls)(1), [npm-dedupe](/man/npm-dedupe)(1)
