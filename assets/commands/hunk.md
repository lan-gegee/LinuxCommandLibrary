# TAGLINE

面向智能体编程的"审查优先"终端 diff 查看器

# TLDR

**在 git 仓库上打开** hunk

```hunk```

**通过 npm 或 Homebrew 安装**

```npm i -g hunk```

# SYNOPSIS

**hunk** [*options*] [*path*]

# DESCRIPTION

**hunk** 是一款面向开发者和编程智能体的终端 diff 审查工具：浏览各个 hunk、通过键盘优先的 UI 审查变更，并可集成到智能体工作流中。可从 npm、Homebrew 或上游发布页（**modem-dev/hunk**）安装。

# PARAMETERS

默认 UI 审查的是工作区/已暂存的变更。路径、暂存和主题相关的标志请参见 **hunk --help**。

# CAVEATS

相对较新；用户体验可能快速变化。常规使用需要 git 仓库。

# INSTALL

```brew: brew install hunk```

```nix: nix profile install nixpkgs#hunk```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-diff](/man/git-diff)(1), [delta](/man/delta)(1), [difft](/man/difft)(1)

# RESOURCES

```[Source code](https://github.com/modem-dev/hunk)```

<!-- verified: 2026-07-19 -->
