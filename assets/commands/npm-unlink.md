# TAGLINE

移除已链接的软件包

# TLDR

**取消链接全局软件包**

```npm unlink -g [package]```

**取消链接本地软件包**

```npm unlink [package]```

**全局取消链接当前软件包**

```npm unlink```

# SYNOPSIS

**npm unlink** [_options_] [_packages_...]

# PARAMETERS

**-g**, **--global**
> 全局取消链接。

**--no-save**
> 不更新 package.json。

# DESCRIPTION

**npm unlink** 移除已链接的软件包。它是 npm link 的反向操作，用于删除软件包之间的符号链接，或移除全局链接的软件包。

它是 "npm uninstall" 的别名，但在语义上专门用于撤销 npm link 操作。

# WORKFLOW

```bash
# In library directory (linked globally)
cd my-library
npm link        # Creates global link

# In project (using linked library)
cd my-project
npm link my-library  # Uses linked version

# To unlink
cd my-project
npm unlink my-library  # Remove local link

cd my-library
npm unlink -g  # Remove global link
```

# CAVEATS

与 npm uninstall 相同。对全局链接的软件包请使用 -g。之后可能需要正常重新安装该软件包。

# HISTORY

npm unlink 作为 npm uninstall 的语义化别名被引入，专门用于撤销 npm link 操作。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-link](/man/npm-link)(1), [npm-uninstall](/man/npm-uninstall)(1)
