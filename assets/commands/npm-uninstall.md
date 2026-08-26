# TAGLINE

从 node_modules 中移除软件包，并可选择从 package 中移除

# TLDR

**卸载软件包**

```npm uninstall [package-name]```

**卸载并从依赖中移除**

```npm uninstall --save [package-name]```

**卸载全局软件包**

```npm uninstall -g [package-name]```

**卸载多个软件包**

```npm uninstall [pkg1] [pkg2]```

# SYNOPSIS

**npm** **uninstall** [_packages_...] [_options_]

# PARAMETERS

**-g**, **--global**
> 卸载全局软件包。

**--save**
> 从 dependencies 中移除。

**--save-dev**
> 从 devDependencies 中移除。

# DESCRIPTION

**npm uninstall** 从 node_modules 中移除软件包，并可选择从 package.json 中移除。也会移除不再使用的依赖。别名：npm rm、npm remove、npm un。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-install](/man/npm-install)(1)
