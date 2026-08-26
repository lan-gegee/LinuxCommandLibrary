# TAGLINE

面向提交信息的交互式 emoji 指南

# TLDR

**交互式提交**

```gitmoji -c```

**列出可用的 emoji**

```gitmoji -l```

**搜索 emoji**

```gitmoji -s [bug]```

**初始化仓库**

```gitmoji -i```

**配置 gitmoji**

```gitmoji -g```

**移除提交钩子**

```gitmoji -r```

**更新 emoji 列表**

```gitmoji -u```

# SYNOPSIS

**gitmoji** [_options_]

# PARAMETERS

**-c**, **--commit**
> 使用 emoji 进行交互式提交。

**-l**, **--list**
> 列出所有 gitmoji。

**-s** _TEXT_, **--search** _TEXT_
> 搜索 emoji。

**-i**, **--init**
> 将 gitmoji 初始化为提交钩子。

**-r**, **--remove**
> 移除先前初始化的提交钩子。

**-g**, **--config**
> 配置各项设置。

**-u**, **--update**
> 与上游仓库同步 emoji 列表。

**-v**, **--version**
> 打印已安装的版本。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gitmoji** 按照标准化约定在提交信息中加入 emoji。每个 emoji 代表一种提交类型（修复 bug、新功能、文档等），使提交历史更直观、更易于浏览。

交互模式会引导你选择 emoji 并撰写信息。它还可以安装为 Git 钩子，在每次提交时自动弹出 emoji 选择提示。

# CAVEATS

基于 Node.js 的工具。团队须就约定达成一致。某些工具可能无法渲染 emoji。

# HISTORY

gitmoji 由 **Carlos Cuesta** 创建，用于规范提交信息中 emoji 的使用，让仓库历史更具表现力。

# INSTALL

```brew: brew install gitmoji```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-commit](/man/git-commit)(1), [gitlint](/man/gitlint)(1)
