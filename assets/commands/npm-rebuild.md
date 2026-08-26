# TAGLINE

为当前 Node 版本重新构建原生插件模块

# TLDR

**重新构建所有原生模块**

```npm rebuild```

**重新构建指定软件包**

```npm rebuild [package]```

**针对不同的 Node 版本重新构建**

```npm rebuild --target=[18.0.0]```

**重新构建全局安装的软件包**

```npm rebuild -g```

# SYNOPSIS

**npm rebuild** [_options_] [_packages_...]

# PARAMETERS

**-g**, **--global**
> 重新构建全局软件包。

**--ignore-scripts**
> 不运行脚本。

**--foreground-scripts**
> 在前台运行脚本。

# DESCRIPTION

**npm rebuild** 为当前 Node.js 版本重新构建原生插件模块。在升级 Node.js 之后或原生模块无法加载时需要执行此操作。

该命令会对每个包含原生代码的软件包运行 node-gyp rebuild。

# COMMON USE CASES

```bash
# After Node.js upgrade
npm rebuild

# Fix broken native module
npm rebuild bcrypt

# Rebuild with verbose output
npm rebuild --verbose
```

# NATIVE MODULES

```
bcrypt, node-sass, sqlite3
sharp, canvas, grpc
leveldown, node-rdkafka
```

# CAVEATS

需要构建工具（Python、C++ 编译器）。可能耗时较长。某些模块需要特定的 Node 版本。

# HISTORY

npm rebuild 自早期版本起就是 npm 的一部分，对于在不同 Node.js 版本间维护原生插件兼容性至关重要。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [node-gyp](/man/node-gyp)(1)
