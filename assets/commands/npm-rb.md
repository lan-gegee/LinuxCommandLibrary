# TAGLINE

重新构建带原生插件的软件包

# TLDR

**重新构建所有软件包**

```npm rb```

**重新构建指定软件包**

```npm rb [package-name]```

**重新构建全局软件包**

```npm rb -g```

**重新构建多个指定的软件包**

```npm rb [package1] [package2]```

# SYNOPSIS

**npm** **rb** [_packages_]

# PARAMETERS

_PACKAGES_
> 要重新构建的软件包。

**-g**
> 重新构建全局软件包。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm rb** 是 **npm rebuild** 的别名。它使用 node-gyp 重新编译原生插件模块（C/C++ 绑定）。

升级 Node.js 版本后通常需要执行此操作，因为原生插件是针对特定 Node.js ABI 编译的。在 node_modules 中手动修改过软件包源码后也很有用。

# CAVEATS

npm rebuild 的别名。需要已安装构建工具（make、gcc/g++ 或同等工具）。只影响带原生插件的软件包；纯 JavaScript 软件包不受影响。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-rebuild](/man/npm-rebuild)(1), [npm-install](/man/npm-install)(1), [node-gyp](/man/node-gyp)(1)
