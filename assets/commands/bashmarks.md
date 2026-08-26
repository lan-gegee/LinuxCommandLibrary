# TAGLINE

Shell 目录书签工具

# TLDR

**保存**当前目录书签

```s [bookmark-name]```

**跳转**到书签

```g [bookmark-name]```

**列出**书签

```l```

**打印**书签路径

```p [bookmark-name]```

**删除**书签

```d [bookmark-name]```

# SYNOPSIS

bashmarks directory bookmarking functions

# DESCRIPTION

**bashmarks** 是一个提供目录书签功能的 bash 脚本。它允许你用简短名称保存常用目录路径，并快速跳转过去。

该工具添加了一组便捷的 Shell 函数，用于管理和导航到已收藏的目录。

# FUNCTIONS

**s** _name_
> 将当前目录保存为书签

**g** _name_
> 跳转到书签目录

**l**
> 列出所有书签

**d** _name_
> 删除书签

**p** _name_
> 打印书签路径

# FEATURES

- 简单的书签管理
- 书签 Tab 补全
- 持久化存储
- 与 bash/zsh 集成

# WORKFLOW

```bash
# Save bookmark
cd /var/log/apache2
s apache

# Jump to bookmark
g apache

# List all
l

# Remove
d apache
```

# CAVEATS

需要在 Shell 配置中 source **~/.local/bin/bashmarks.sh**。书签名必须简单（不含空格或特殊字符）。书签存储在 **~/.sdirs** 中。与按访问频率排序目录的 z 或 autojump 不同。必须单独安装。

# HISTORY

**bashmarks** 由 Huy Nguyen 于 **2010** 年前后创建，旨在为 bash 用户提供简单的目录书签功能。

# SEE ALSO

[z](/man/z)(1), [autojump](/man/autojump)(1), [fasd](/man/fasd)(1)

# RESOURCES

```[Source code](https://github.com/huyng/bashmarks)```

<!-- verified: 2026-06-19 -->
