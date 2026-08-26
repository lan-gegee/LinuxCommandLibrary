# TAGLINE

基于终端的 git 交互式变基序列编辑器

# TLDR

**用作** git 序列编辑器

```git rebase -i HEAD~5```

**配置**为默认编辑器

```git config --global sequence.editor interactive-rebase-tool```

# SYNOPSIS

**interactive-rebase-tool** [_options_] [_todo-file_]

# PARAMETERS

**--version**
> 显示版本并退出

**--help**
> 显示帮助并退出

# DESCRIPTION

**interactive-rebase-tool** 是一个功能齐全的、基于终端的 git 交互式变基序列编辑器。它为编辑 rebase todo 文件提供可视化界面，具备语法高亮、撤销/重做和可视化指示等功能。

该工具清晰地展示提交及其操作（pick、squash、fixup、reword、edit、drop 等），让复杂的变基更易于管理。

# KEYBINDINGS

**↑/↓** 或 **k/j**
> 在提交之间导航

**Page Up/Page Down**
> 翻页导航

**Home/End**
> 跳到开头/结尾

**p**
> Pick 提交

**r**
> Reword 提交

**e**
> Edit 提交

**s**
> Squash 提交

**f**
> Fixup 提交

**d**
> Drop 提交

**b**
> 切换 break 动作

**E**
> 编辑 exec 命令

**v**
> 切换可视化模式以进行批量操作

**c**
> 显示提交信息

**Ctrl+z**
> 撤销

**Ctrl+y**
> 重做

**!**
> 在外部编辑器中打开

**?**
> 显示内置帮助

**w**
> 保存更改

**q**
> 中止变基

# CAVEATS

必须通过 `git config --global sequence.editor interactive-rebase-tool` 将其配置为 Git 的序列编辑器。终端需要支持所需的转义序列。

# HISTORY

**interactive-rebase-tool** 的诞生是为了改进 git 交互式变基的体验，用可视化编辑器取代手动编辑 todo 文件的方式。

# INSTALL

```dnf: sudo dnf install git-interactive-rebase-tool```

```brew: brew install git-interactive-rebase-tool```

```nix: nix profile install nixpkgs#git-interactive-rebase-tool```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-rebase](/man/git-rebase)(1), [git](/man/git)(1), [vim](/man/vim)(1)
