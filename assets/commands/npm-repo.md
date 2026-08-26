# TAGLINE

在浏览器中打开软件包的仓库页面

# TLDR

**打开某个软件包的仓库页面**

```npm repo [package-name]```

**打开当前项目的仓库页面**

```npm repo```

**打开多个软件包的仓库页面**

```npm repo [package1] [package2]```

**只打印仓库 URL 而不打开浏览器**

```npm repo [package-name] --no-browser```

# SYNOPSIS

**npm** **repo** [_packages_]

# PARAMETERS

_PACKAGES_
> 一个或多个软件包名。省略时使用当前项目的 `package.json`。

**--browser** _BROWSER_
> 用于打开 URL 的浏览器。默认为系统默认（macOS 上为 `open`，Windows 上为 `start`，Linux 上为 `xdg-open`）。

**--no-browser**
> 将仓库 URL 打印到 stdout 而不打开浏览器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm repo** 从软件包 `package.json` 的 `repository` 字段推测其仓库 URL，然后在所配置的浏览器中打开。若未提供软件包名，则读取当前目录中的 `package.json`。

可以通过 `--browser` 配置选项覆盖所用浏览器，或通过 `npm config set browser [program]` 全局设置。传入 `--no-browser` 可抑制打开浏览器并改为打印 URL。

# CAVEATS

如果软件包的 `package.json` 中没有 `repository` 字段，npm 会回退到该软件包在 npm registry 上的页面。查询未在本地安装的软件包需要网络连接。

# HISTORY

**npm repo** 从早期版本起就是 npm CLI 的一部分，让你可以快速访问软件包的源码仓库。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-home](/man/npm-home)(1), [npm-docs](/man/npm-docs)(1)
