# TAGLINE

Git 的交互式读入-求值-打印循环（REPL）

# TLDR

**启动 git REPL**

```git repl```

**在 REPL 中运行命令**

```status```

**在 REPL 中查看日志**

```log --oneline -10```

**退出 REPL**

```exit```

# SYNOPSIS

**git repl**

# DESCRIPTION

**git repl** 为 Git 命令提供一个交互式 Shell。它属于 git-extras，会启动一个读入-求值-打印循环，输入命令时无需带 "git" 前缀；以 `!` 开头的输入会作为原始 shell 命令执行，而 `ls` 被映射为 `git ls-files`。

这个 REPL 减少了敲键次数，让探索式的 Git 会话更加轻松。整个会话期间可以使用命令历史（通过 readline）。输入 "exit"、"quit" 或按 Ctrl-D 退出。

# CAVEATS

属于 git-extras 软件包。命令运行时不带 "git" 前缀。Shell 特性有限。

# HISTORY

git repl 是 **git-extras** 的一部分，为高频 Git 用户提供了一个交互式环境。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [tig](/man/tig)(1), [git-extras](/man/git-extras)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-repl)```

<!-- verified: 2026-07-17 -->
