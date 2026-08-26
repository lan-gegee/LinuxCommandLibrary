# TAGLINE

在浏览器中打开软件包主页

# TLDR

**打开软件包主页**

```npm home [package-name]```

**打开当前项目的主页**

```npm home```

**打开多个软件包的主页**

```npm home [package1] [package2]```

# SYNOPSIS

**npm** **home** [_packages_]

# PARAMETERS

_PACKAGES_
> 软件包名称。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm home** 在浏览器中打开软件包主页，使用的是 package.json 中的 homepage 字段。

该命令会跳转到项目网站。它是 npm docs 的别名。

# CAVEATS

需要浏览器。无 homepage 时回退到 npm registry 页面。使用 package.json 的 homepage 字段。

# HISTORY

npm home 让你可以从命令行**快速访问**软件包主页。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-docs](/man/npm-docs)(1), [npm-repo](/man/npm-repo)(1)
