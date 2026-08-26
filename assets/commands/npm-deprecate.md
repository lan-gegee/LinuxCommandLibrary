# TAGLINE

在 npm registry 上将软件包版本标记为已弃用

# TLDR

**弃用软件包的某个版本**

```npm deprecate [package]@[version] "[message]"```

**弃用版本范围**

```npm deprecate [package]@"<[1.0.0]" "[message]"```

**弃用所有版本**

```npm deprecate [package] "[message]"```

**取消弃用**

```npm deprecate [package]@[version] ""```

# SYNOPSIS

**npm deprecate** _pkg_@_version_ _message_

# PARAMETERS

**pkg@version**
> 要弃用的软件包及版本。

**message**
> 弃用消息（留空即移除弃用标记）。

# DESCRIPTION

**npm deprecate** 在 npm registry 上将软件包版本标记为已弃用。安装了被弃用版本的用户会看到警告消息。

它通常用于劝阻使用旧版本或有漏洞的版本，同时仍允许安装。
# Deprecate specific version
npm deprecate my-package@1.0.0 "Critical bug, please upgrade"

# Deprecate old versions
npm deprecate my-package@"<2.0.0" "Version 1.x is no longer supported"

# Remove deprecation
npm deprecate my-package@1.0.0 ""
```

# USE CASES

```
- Security vulnerabilities
- Breaking changes
- Package renamed
- End of support
```

# CAVEATS

需要对软件包有发布权限。不会阻止安装。消息为空即移除弃用标记。

# HISTORY

npm deprecate 的加入提供了一种比取消发布更温和的方式，让维护者可以警告用户，同时不破坏现有的安装。

# SEE ALSO

[npm](/man/npm)(1), [npm-publish](/man/npm-publish)(1), [npm-unpublish](/man/npm-unpublish)(1)

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->
