# TAGLINE

在 Jujutsu 中更新描述并在其上创建新变更

# TLDR

以指定消息创建提交

```jj commit -m "[message]"```

交互式提交，选择要包含的改动

```jj commit -i```

打开编辑器撰写提交描述

```jj commit```

仅提交特定文件

```jj commit [path/to/file1] [path/to/file2]```

使用特定的 diff 编辑器工具提交

```jj commit --tool [meld]```

设置消息后仍打开编辑器进行润色

```jj commit -m "[draft message]" --editor```

# SYNOPSIS

**jj** **commit** [_options_] [_FILESETS_...]

# PARAMETERS

_FILESETS_
> 将这些路径放入当前提交。

**-m**, **--message** _MESSAGE_
> 要使用的变更描述（不打开编辑器）。

**-i**, **--interactive**
> 交互式选择要包含在当前提交中的改动。

**--tool** _NAME_
> 指定要使用的 diff 编辑器（隐含 --interactive）。

**--editor**
> 打开编辑器来编辑变更描述。即使使用了 --message 也强制打开编辑器。

# DESCRIPTION

**jj commit** 更新当前工作副本提交的描述，并在其上创建一个新的空变更。它等价于先运行 **jj describe** 再运行 **jj new**，别名为 **jj ci**。

不带路径参数或 **--interactive** 调用时，工作副本中的所有改动都会被包含。使用路径或 **--interactive** 时，只有选中的改动会被提交，其余改动会移入上方新的工作副本提交。

与 git 不同，Jujutsu 自动将工作副本视为可变提交，因此该命令通过设置描述并前移工作副本来定稿当前改动。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-describe](/man/jj-describe)(1), [jj-new](/man/jj-new)(1), [jj-status](/man/jj-status)(1), [jj-diff](/man/jj-diff)(1)
