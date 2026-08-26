# TAGLINE

在浏览器中打开软件包文档

# TLDR

**打开软件包文档**

```npm docs [package-name]```

**打开当前项目的文档**

```npm docs```

**打开多个软件包的文档**

```npm docs [package1] [package2]```

# SYNOPSIS

**npm** **docs** [_packages_]

# PARAMETERS

_PACKAGES_
> 要打开其文档的软件包名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm docs** 在浏览器中打开软件包文档。它会从 package.json 读取 homepage 字段。

该命令会跳转到文档 URL。它是 npm home 的别名，偏向于打开文档页。

# CAVEATS

需要浏览器。使用 package.json 中的 homepage；若无则回退到 npm 页面。

# HISTORY

npm docs 让你可以通过命令行快速访问**软件包文档**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-home](/man/npm-home)(1), [npm-repo](/man/npm-repo)(1)
