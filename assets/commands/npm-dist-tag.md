# TAGLINE

管理软件包的发行标签（dist-tag）

# TLDR

**列出软件包的标签**

```npm dist-tag ls [package-name]```

**为版本添加标签**

```npm dist-tag add [package]@[version] [tag]```

**移除标签**

```npm dist-tag rm [package] [tag]```

# SYNOPSIS

**npm** **dist-tag** _command_ [_options_]

# PARAMETERS

**ls** _package_
> 列出软件包的标签。

**add** _pkg@version_ _tag_
> 为版本添加标签。

**rm** _package_ _tag_
> 移除标签。

# DESCRIPTION

**npm dist-tag** 管理软件包的发行标签。latest、next 或 beta 等标签指向特定版本，用于控制 npm install 默认安装哪个版本。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1)
