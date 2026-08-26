# TAGLINE

合并 GitLab 合并请求

# TLDR

**合并一个合并请求**

```glab mr merge [number]```

压缩后合并

```glab mr merge [number] --squash```

合并且不删除分支

```glab mr merge [number] --remove-source-branch=false```

流水线成功后合并

```glab mr merge [number] --when-pipeline-succeeds```

使用自定义提交信息合并

```glab mr merge [number] --message "[commit message]"```

变基后合并

```glab mr merge [number] --rebase```

# SYNOPSIS

**glab** **mr** **merge** [_number_] [_options_]

# PARAMETERS

**--squash**
> 合并时压缩提交。

**--rebase**
> 合并前先将提交变基到基础分支上。

**--remove-source-branch**
> 合并后删除源分支。

**--when-pipeline-succeeds**
> 设置合并请求在流水线成功后自动合并。

**--message** _text_
> 自定义合并提交信息。

**--sha** _sha_
> 仅当源分支的 HEAD 与给定 SHA 匹配时才合并。防止意外合并其他更改。

**-y**, **--yes**
> 跳过确认提示。

# DESCRIPTION

**glab mr merge** 合并一个 GitLab 合并请求。它支持压缩合并、变基、自动删除源分支，以及等待 CI 流水线通过后再完成的延迟合并。

# INSTALL

```apt: sudo apt install glab```

```dnf: sudo dnf install glab```

```pacman: sudo pacman -S glab```

```apk: sudo apk add glab```

```zypper: sudo zypper install glab```

```brew: brew install glab```

```nix: nix profile install nixpkgs#glab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab-mr](/man/glab-mr)(1), [glab-mr-create](/man/glab-mr-create)(1)
