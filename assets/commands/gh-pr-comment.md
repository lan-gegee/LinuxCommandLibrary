# TAGLINE

为拉取请求添加评论

# TLDR

**为 PR 添加评论**

```gh pr comment [number] -b "[comment]"```

**以交互方式评论**

```gh pr comment [number]```

**从文件读取评论内容**

```gh pr comment [number] -F [comment.md]```

**编辑上一条评论**

```gh pr comment [number] --edit-last -b "[new text]"```

# SYNOPSIS

**gh** **pr** **comment** [_number_] [_options_]

# PARAMETERS

**-b**, **--body** _text_
> 评论正文。

**-F**, **--body-file** _file_
> 从文件读取正文。

**--edit-last**
> 编辑上一条评论。

**-R**, **--repo** _owner/repo_
> 仓库。

# DESCRIPTION

**gh pr comment** 在命令行中为拉取请求添加评论。它提供灵活的评论撰写方式，包括内联文本、文件输入和交互式编辑。

不带 --body 标志调用时，命令会打开你的默认编辑器来撰写评论。评论支持完整的 GitHub 风格 Markdown，包括代码块、表格、任务列表和 @ 提及。--edit-last 选项允许修改你在该拉取请求上的最近一条评论。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh-pr](/man/gh-pr)(1)
