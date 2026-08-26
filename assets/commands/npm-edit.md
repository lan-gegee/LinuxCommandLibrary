# TAGLINE

在默认编辑器中打开已安装软件包的目录

# TLDR

**编辑已安装的软件包**

```npm edit [package]```

**编辑嵌套的子包**

```npm edit [package]/[subpackage]```

**使用指定的编辑器编辑**

```EDITOR=[vim] npm edit [package]```

**持久配置默认编辑器**

```npm config set editor [code]```

# SYNOPSIS

**npm edit** _pkg_[**/**_subpkg_...]

# DESCRIPTION

**npm edit** 在默认编辑器中打开已安装软件包的目录，方便直接查看或修改 `node_modules` 下的内容。编辑器退出后，npm 会重新构建该软件包，使修改（例如对原生插件的修改）生效。

所用编辑器取自 npm 的 **editor** 配置，该配置默认来自 **EDITOR** 或 **VISUAL** 环境变量（Windows 上为 `notepad.exe`，Unix 上为 `vi`）。

# PARAMETERS

_pkg_
> 要编辑的依赖名称。

**/**_subpkg_
> 可选的嵌套包路径，用于深入 `node_modules` 下某个传递依赖。

**editor** (config)
> 用于打开软件包的编辑器。可通过 `npm config set editor <name>` 设置，或通过 **EDITOR**/**VISUAL** 指定。

# CAVEATS

对 `node_modules` 中文件的修改会在 npm 下次重装或更新该软件包时丢失。若要持久保留本地修改，请使用 **patch-package** 或在上游 fork 该软件包。**npm edit** 不感知工作区：在工作区中它操作的是根 `node_modules`。

# HISTORY

**npm edit** 从早期版本起就是 **npm** 的一部分，为调试期间快速阅读或修改已安装依赖提供了便利。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-explore](/man/npm-explore)(1)
