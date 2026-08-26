# TAGLINE

简单的命令行片段管理器

# TLDR

**添加新片段**

```pet new```

**添加带标签的新片段**

```pet new -t```

**搜索并运行片段**

```pet exec```

**按标签过滤后运行片段**

```pet exec -t [tag_name]```

**把片段复制到剪贴板**

```pet clip```

**列出所有片段**

```pet list```

**交互式搜索片段**

```pet search```

**编辑片段文件**

```pet edit```

# SYNOPSIS

**pet** _command_ [_options_]

# PARAMETERS

**new**
> 创建新的命令片段。使用 **-t** 添加标签。

**exec**
> 搜索并执行某个片段。使用 **-t** 按标签过滤。

**clip**
> 把选中的片段复制到剪贴板。

**list**
> 显示所有已保存的片段。

**search**
> 交互式搜索片段。

**edit**
> 在编辑器中打开片段文件。

**configure**
> 编辑配置文件。

**sync**
> 通过 Gist、GitLab Snippets 或 GitHub Enterprise 同步片段。

**version**
> 打印版本号。

**--config** _string_
> 指定配置文件（默认 $HOME/.config/pet/config.toml）。

**--debug**
> 启用调试模式。

# DESCRIPTION

**pet** 是一个简单的命令行片段管理器。它保存常用命令以及描述和可选的参数占位符，然后让你借助 fzf 或 peco 等模糊查找器交互式地搜索并执行它们。片段可以通过 GitHub Gist、GitLab Snippets 或 GitHub Enterprise 在多台机器之间同步。

# CAVEATS

交互式选择需要 **fzf** 或 **peco**。

# HISTORY

**pet** 由 **Teppei Fukuda**（knqyf263）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install pet```

```nix: nix profile install nixpkgs#pet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nap](/man/nap)(1), [tldr](/man/tldr)(1), [fzf](/man/fzf)(1), [peco](/man/peco)(1)
