# TAGLINE

在 npm registry 上将软件包标记为收藏

# TLDR

**收藏软件包**

```npm star [package]```

**收藏多个软件包**

```npm star [package1] [package2]```

**查看你收藏的软件包**

```npm stars```

**取消收藏软件包**

```npm unstar [package]```

# SYNOPSIS

**npm** **star** _package_...

# DESCRIPTION

**npm star** 在 npm registry 上将一个或多个软件包标记为收藏，用来表达对你觉得有用的软件包的认可。需要先通过 **npm login** 完成 npm 身份验证。

收藏的软件包之后可用 **npm stars** 列出。要移除收藏，请使用 **npm unstar**。

# PARAMETERS

**--registry** _url_
> 使用指定的 registry URL 而非默认值。

**--otp** _code_
> 为两步验证提供一次性密码。

# CAVEATS

需要已登录 npm（**npm login**）。收藏是公开的，并与你的 npm 账户关联。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-unstar](/man/npm-unstar)(1), [npm-stars](/man/npm-stars)(1), [npm-login](/man/npm-login)(1)
