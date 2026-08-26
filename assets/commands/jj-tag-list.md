# TAGLINE

显示仓库中的所有标签

# TLDR

列出所有标签

```jj tag list```

列出匹配 glob 模式的标签

```jj tag list "[v*]"```

按作者日期排序列出标签（降序）

```jj tag list --sort author-date-```

使用自定义模板列出标签

```jj tag list -T '[name ++ "\n"]'```

# SYNOPSIS

**jj** **tag** **list** [_options_] [_pattern_]

# PARAMETERS

**-T**, **--template** _TEMPLATE_
> 使用自定义模板渲染输出。

**--sort** _KEY_
> 按键排序：name、author-name、author-email、author-date、committer-name、committer-email、committer-date。加后缀 - 表示降序。

# DESCRIPTION

**jj tag list** 显示仓库中的所有标签。可选按 glob 模式过滤。显示标签名及其引用的提交。可以指定多个排序键，第一个键的优先级最高。默认排序方式可通过配置中的 `ui.tag-list-sort-keys` 设置。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-tag](/man/jj-tag)(1), [jj-tag-set](/man/jj-tag-set)(1), [jj-tag-delete](/man/jj-tag-delete)(1)
