# TAGLINE

创建 npm-shrinkwrap 文件

# TLDR

**创建 shrinkwrap 文件**

```npm shrinkwrap```

**包含开发依赖**

```npm shrinkwrap --dev```

# SYNOPSIS

**npm** **shrinkwrap** [_options_]

# PARAMETERS

**--dev**
> 包含 devDependencies。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm shrinkwrap** 创建 npm-shrinkwrap.json，在发布时锁定依赖版本。

该命令会创建可随软件包发布的 lockfile。与 package-lock.json 不同，它会被包含在发布的软件包中。

# CAVEATS

随软件包一起发布。会覆盖 package-lock.json。适用于库类项目。

# HISTORY

npm shrinkwrap 提供**版本锁定**能力，锁定信息随已发布的软件包一同分发。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [package-lock.json](/man/package-lock.json)(5)
