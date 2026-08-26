# TAGLINE

在 Jujutsu 中将一个修订的改动移入其父修订或指定目标

# TLDR

将工作副本压缩进其父修订

```jj squash```

将特定修订压缩进其父修订

```jj squash -r [revision]```

交互式选择要压缩的部分

```jj squash -i```

压缩到指定的目标修订

```jj squash --into [destination]```

从一个修订压缩到另一个修订

```jj squash --from [source] --into [destination]```

以自定义描述消息进行压缩

```jj squash -m "[message]"```

仅压缩特定文件路径的改动

```jj squash [path/to/file]```

# SYNOPSIS

**jj** **squash** [_options_] [_FILESETS_]

# PARAMETERS

**-r**, **--revision** _REVSET_
> 要压缩进父修订的修订（默认：@）。

**-f**, **--from** _REVSETS_
> 改动来源修订（默认：@）。

**-t**, **--into** _REVSET_
> 压缩目标修订（默认：源修订的父修订）。

**-i**, **--interactive**
> 交互式选择要压缩的部分。

**--tool** _NAME_
> 指定要使用的 diff 编辑器（隐含 --interactive）。

**-m**, **--message** _MESSAGE_
> 被压缩修订的描述（不打开编辑器）。

**-u**, **--use-destination-message**
> 使用目标修订的描述，并丢弃源修订的描述。

**-k**, **--keep-emptied**
> 即使源修订变为空也不废弃它。

# DESCRIPTION

**jj squash** 在 Jujutsu 中将一个修订的改动移入其父修订或指定目标。不带选项时，它会把工作副本提交（@）的所有改动移入其父修订。源提交会变为空并默认被废弃。使用 **--from** 和 **--into** 可在任意修订之间移动改动。通过传入 fileset 参数可以将操作限制在特定的文件路径上。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-abandon](/man/jj-abandon)(1), [jj-split](/man/jj-split)(1), [jj-diffedit](/man/jj-diffedit)(1)
