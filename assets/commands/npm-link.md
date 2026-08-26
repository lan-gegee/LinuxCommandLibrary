# TAGLINE

为本地开发创建软件包符号链接

# TLDR

**将当前软件包链接到全局**

```npm link```

**链接到全局软件包**

```npm link [package-name]```

**链接本地依赖**

```npm link [../path/to/package]```

**取消链接软件包**

```npm unlink [package-name]```

# SYNOPSIS

**npm** **link** [_package_]

# PARAMETERS

_PACKAGE_
> 软件包名称或路径。

**--help**
> 显示帮助信息。

# DESCRIPTION

**npm link** 为本地开发创建软件包的符号链接，便于在本地测试软件包。

该命令会先创建全局符号链接，然后再链接进项目进行开发。

# CAVEATS

会创建符号链接。可能与打包工具产生冲突，请谨慎使用。

# HISTORY

npm link 通过在软件包之间创建符号链接来支持**本地软件包开发**。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1), [npm-unlink](/man/npm-unlink)(1)
