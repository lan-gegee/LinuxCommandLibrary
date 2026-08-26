# TAGLINE

在网页浏览器中打开软件包的缺陷跟踪页面

# TLDR

**打开软件包的 bugs 页面**

```npm bugs [package-name]```

**打开当前项目的 bugs 页面**

```npm bugs```

# SYNOPSIS

**npm** **bugs** [_package_...]

**npm** **issues** [_package_...]

# PARAMETERS

**--browser** _BROWSER_
> 要使用的浏览器；设为 `false` 时改为打印 URL。

**--registry** _URL_
> npm registry URL（默认：https://registry.npmjs.org/）。

**-w**, **--workspace** _NAME_
> 在指定工作区（workspace）的上下文中运行。

**--workspaces**
> 在所有已配置的工作区中运行。

**--include-workspace-root**
> 使用工作区时包含根项目。

# DESCRIPTION

**npm bugs** 从软件包元数据中推测其缺陷跟踪 URL（或支持邮箱 `mailto:`），并在网页浏览器中打开。若未指定软件包，则使用当前目录中的 `package.json`。别名 **npm issues** 的作用相同。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-docs](/man/npm-docs)(1), [npm-repo](/man/npm-repo)(1)
