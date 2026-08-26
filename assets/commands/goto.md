# TAGLINE

支持别名的目录导航工具

# TLDR

**注册**当前目录

```goto -r [alias-name]```

**跳转**到别名对应的目录

```goto [alias-name]```

**列出**所有别名

```goto -l```

**注销**一个别名

```goto -u [alias-name]```

# SYNOPSIS

**goto** [_options_] [_alias_]

# PARAMETERS

**-r, --register** _ALIAS_
> 将当前目录注册为别名

**-u, --unregister** _ALIAS_
> 注销别名

**-l, --list**
> 列出所有已注册的别名

**-c, --clean**
> 移除指向不存在目录的别名

**-x, --expand** _ALIAS_
> 打印别名对应的路径

**-p, --push**
> 使用 pushd 而不是 cd

**-v, --version**
> 显示版本并退出

**-h, --help**
> 显示帮助并退出

# DESCRIPTION

**goto** 是一个目录导航工具，允许用户为经常访问的目录创建别名。它提供 Tab 补全以及在项目之间快速跳转的能力。

该工具与 shell（bash、zsh、fish）集成，无需输入冗长的路径即可实现快速导航。

# SHELL INTEGRATION

添加到 shell 配置中：

**Bash/Zsh:**
```bash
eval "$(goto -r)"
```

**Fish:**
```fish
goto -r | source
```

# EXAMPLES

```bash
goto -r proj      # Register current dir as 'proj'
goto proj         # Jump to ~/projects/myproject
goto -l           # List: proj -> ~/projects/myproject
goto -u proj      # Remove alias
```

# CAVEATS

需要集成到 shell。别名存储在用户主目录中。Tab 补全需要进行相应的 shell 设置。

# HISTORY

**goto** 的灵感来自 z.lua 和 autojump 等类似工具，专注于简洁性和基于别名的导航方式。

# INSTALL

```brew: brew install goto```

```nix: nix profile install nixpkgs#goto```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[z.lua](https://github.com/skywind3000/z.lua), [autojump](https://github.com/wting/autojump), [zoxide](https://github.com/ajeetdsouza/zoxide)
