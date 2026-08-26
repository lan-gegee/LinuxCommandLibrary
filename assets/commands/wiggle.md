# TAGLINE

应用被拒绝的补丁并解决冲突

# TLDR

就地**应用被拒绝的补丁**

```wiggle --replace [original] [original.rej]```

**显示两个文件之间的词级差异**

```wiggle --diff [file1] [file2]```

**执行三方合并**

```wiggle --merge [original] [changed] [modified]```

**交互式浏览**合并或补丁结果

```wiggle --browse [original] [original.rej]```

**提取补丁或合并中的一个分支**

```wiggle --extract --patch [file.patch] > [patched]```

# SYNOPSIS

**wiggle** [_mode_] [_options_] _files_

# PARAMETERS

**-m**, **--merge**
> 三方合并模式（默认）。

**-d**, **--diff**
> 词级差异模式。

**-x**, **--extract**
> 从补丁或合并中提取一个文件/分支。

**-B**, **--browse**
> 用于合并、差异或补丁的交互式 ncurses 浏览器。

**-r**, **--replace**
> 用合并结果覆盖原文件（保留 `.porig` 备份）。

**-o** _file_, **--output** _file_
> 将输出发送到给定文件而不是 stdout。

**-p**, **--patch**
> 将其中一个参数视为补丁文件。

**-w**, **--words**
> 以词为粒度处理（文本默认）。

**-l**, **--lines**
> 以行为粒度处理。

**-b**, **--ignore-blanks**
> 合并时忽略仅空白字符的差异。

**-i**, **--no-ignore**
> 不忽略已应用的补丁（将它们包含在输出中）。

**-W**, **--show-wiggles**
> 标记被强行挪动到位的 hunk。

**-q**, **--quiet**
> 抑制提示性消息。

**-v**, **--verbose**
> 提高输出详细程度。

**-h**, **--help**
> 显示帮助并退出。

**-V**, **--version**
> 显示版本并退出。

# DESCRIPTION

**wiggle** 用于应用因补丁上下文与当前文件存在轻微冲突而被标准 patch 工具拒绝的补丁。patch 要求上下文完全匹配，而 wiggle 会执行词级分析，即使周围的行已移动或被修改，也能找到变更应当应用的位置。

该工具支持文件的三方合并，既能处理统一 diff 文件，也能处理补丁操作失败产生的 .rej 拒绝文件。当冲突无法自动解决时，交互式浏览模式允许用户手动审查并解决剩余的冲突。

这使得 wiggle 在维护针对不断演进的代码库的长期补丁系列时特别有价值——附近代码的无关更改经常导致补丁无法干净地应用。

# CAVEATS

用于补丁应用失败的情况。不一定总能成功。可能需要修改行内容。

# HISTORY

**wiggle** 由 **Neil Brown** 创建，用于帮助应用因轻微冲突而被拒绝的补丁。

# INSTALL

```apt: sudo apt install wiggle```

```apk: sudo apk add wiggle```

```zypper: sudo zypper install wiggle```

```brew: brew install wiggle```

```nix: nix profile install nixpkgs#wiggle```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[patch](/man/patch)(1), [diff](/man/diff)(1), [merge](/man/merge)(1)
