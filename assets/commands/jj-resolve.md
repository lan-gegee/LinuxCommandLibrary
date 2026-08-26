# TAGLINE

帮助解决合并冲突

# TLDR

解决冲突

```jj resolve```

解决特定文件

```jj resolve [path/to/file]```

列出存在冲突的文件

```jj resolve --list```

使用指定工具解决冲突

```jj resolve --tool [meld]```

# SYNOPSIS

**jj resolve** [_options_] [_path_]

# PARAMETERS

_PATH_
> 要解决的特定文件。

**-l**, **--list**
> 列出存在冲突的文件，而不是启动合并工具。

**--tool** _NAME_
> 要使用的合并工具。该工具必须在 `ui.merge-editor` 或 `merge-tools.<name>` 中配置。与 **--list** 互斥。

**-r**, **--revision** _REVSET_
> 要解决冲突的修订（默认 `@`）。

**--help**
> 显示帮助信息。

# DESCRIPTION

**jj resolve** 帮助解决合并冲突。它会为存在冲突的文件启动合并工具。

该命令识别并处理带有冲突标记的文件。Jujutsu 将冲突作为一等状态进行跟踪。

# CAVEATS

jj 的子命令。需要已配置的合并工具。冲突在被解决前会一直存在。

# HISTORY

jj resolve 是 **Jujutsu** 的一部分，支持其"将冲突视为正常仓库状态"的独特方法。

# INSTALL

```pacman: sudo pacman -S jujutsu```

```apk: sudo apk add jujutsu```

```zypper: sudo zypper install jujutsu```

```brew: brew install jujutsu```

```nix: nix profile install nixpkgs#jujutsu```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jj](/man/jj)(1), [jj-squash](/man/jj-squash)(1), [jj-status](/man/jj-status)(1), [jj-new](/man/jj-new)(1), [jj-describe](/man/jj-describe)(1)
