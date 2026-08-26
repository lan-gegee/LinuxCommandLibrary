# TAGLINE

将软件包更新到 package 中 semver 范围内的最新版本

# TLDR

**更新所有软件包**

```npm update```

**更新指定软件包**

```npm update [package-name]```

**更新全局软件包**

```npm update -g```

**更新到最新版（超出 semver 范围）**

```npm update [package] --latest```

**试运行更新**

```npm update --dry-run```

# SYNOPSIS

**npm** **update** [_packages_...] [_options_]

# PARAMETERS

**-g**, **--global**
> 更新全局软件包。

**--save**
> 更新 package.json。

**--dry-run**
> 预览更新。

# DESCRIPTION

**npm update** 将软件包更新到 package.json 中 semver 范围内的最新版本，同时更新 package-lock.json。建议先用 npm outdated 查看可用的更新。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-outdated](/man/npm-outdated)(1)
