# TAGLINE

带文件树界面的 Git diff 查看器

# TLDR

**查看**带交互式文件树的 git diff

```diffnav```

**查看**特定提交的 diff

```diffnav [commit_hash]```

**查看**两个提交之间的 diff

```diffnav [commit1] [commit2]```

**仅查看**特定文件的 diff

```diffnav -- [file1] [file2]```

# SYNOPSIS

**diffnav** [_options_] [_commit_range_]

# PARAMETERS

**-d, --diff** _MODE_
> Diff 模式：unified、context 或 side-by-side

**-w, --width** _N_
> 设置并排视图的显示宽度

**--no-color**
> 禁用彩色输出

**-h, --help**
> 显示帮助并退出

**-v, --version**
> 显示版本并退出

# DESCRIPTION

**diffnav** 是一个 git diff 查看器，提供交互式文件树界面来浏览代码变更。它将传统 diff 查看器的功能与可视化文件浏览器相结合，更便于浏览涉及多个文件的大型变更集。

该工具与 git 集成，以逐个文件的方式显示差异，支持语法高亮、可折叠区域和键盘导航。在审查 pull request 或浏览涉及大量文件的提交时特别有用。

# KEYBINDINGS

**↑/↓**
> 在树中导航各文件

**Enter**
> 查看所选文件的 diff

**Space**
> 展开/折叠文件

**n/p**
> 跳转到下一个/上一个有变更的文件

**/**
> 在 diff 中搜索

**q**
> 退出

# CAVEATS

需要在 PATH 中安装并可访问 git。大型仓库加载可能较慢。语法高亮依赖于文件扩展名检测。部分终端模拟器的颜色支持有限。

# HISTORY

**diffnav** 旨在改善 git diff 的浏览体验，它在传统分页器界面基础上增加了可视化文件树组件，使用户更容易了解变更在多个文件中的影响范围。

# INSTALL

```pacman: sudo pacman -S diffnav```

```brew: brew install diffnav```

```nix: nix profile install nixpkgs#diffnav```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [diff](/man/diff)(1), [less](/man/less)(1), [difftastic](/man/difftastic)(1)
