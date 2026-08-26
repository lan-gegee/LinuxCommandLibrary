# TAGLINE

管理代码片段和可分享的文件

# TLDR

**创建 gist**

```gh gist create [file]```

**创建公开 gist**

```gh gist create -p [file]```

**从标准输入创建**

```echo "[content]" | gh gist create```

**列出 gists**

```gh gist list```

**查看 gist**

```gh gist view [gist_id]```

**编辑 gist**

```gh gist edit [gist_id]```

**删除 gist**

```gh gist delete [gist_id]```

**克隆 gist**

```gh gist clone [gist_id]```

# SYNOPSIS

**gh** **gist** _command_ [_options_]

# SUBCOMMANDS

**create**
> 从文件或标准输入创建新的 gist。

**list**
> 列出你的 gists。

**view**
> 查看 gist 的内容。

**edit**
> 编辑你的某个 gist。

**delete**
> 删除 gist。

**clone**
> 通过 git 将 gist 克隆到本地。

**rename**
> 重命名 gist 中的文件。

# PARAMETERS

**-p**, **--public**
> 将 gist 设为公开（默认为私密）。

**-d**, **--desc** _text_
> gist 描述。

**-f**, **--filename** _name_
> 为从标准输入读取的内容指定文件名。

**-w**, **--web**
> 创建或查看后在网页浏览器中打开该 gist。

**-r**, **--raw**
> 查看时输出未经渲染的原始内容。

# DESCRIPTION

**gh gist** 用于管理 GitHub Gist——一种分享代码片段、笔记和小文件的简单方式。Gist 可分为公开和私密两种，私密 gist 不出现在搜索结果中，但仍可通过 URL 访问。

每个 gist 支持多个文件，并借助 git 提供完整版本历史。它们可以像普通仓库一样被克隆，因此很适合分享配置文件、脚本或文档。Gist 支持语法高亮，也可以嵌入网站。

CLI 提供从创建到编辑、删除的完整生命周期管理，并支持从标准输入读取内容，方便脚本化工作流。

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

[gh](/man/gh)(1), [gist](/man/gist)(1), [git](/man/git)(1)
