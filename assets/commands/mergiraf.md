# TAGLINE

具备语法感知能力的 Git 合并冲突解决器

# TLDR

将 mergiraf **注册为 Git 合并驱动器**

```mergiraf register```

**作为 Git 合并驱动器使用**（在 .gitattributes 中配置）

```*.rs merge=mergiraf```

手动**解决文件中的冲突**

```mergiraf resolve [path/to/conflicted_file]```

**显式指定语言**进行解决

```mergiraf resolve -L [rust] [path/to/conflicted_file]```

**检查 mergiraf 的自动解决结果**

```mergiraf review [path/to/file]```

**列出支持的语言**

```mergiraf languages```

# SYNOPSIS

**mergiraf** _command_ [_options_] [_file_]

# SUBCOMMANDS

**resolve**
> 尝试解决文件中的合并冲突。

**review**
> 检查 mergiraf 自动解决冲突的结果。

**register**
> 将 mergiraf 注册为全局 git 配置中的 Git 合并驱动器。

**languages**
> 列出支持的语言和文件扩展名。

**report**
> 生成用于复现有问题合并的归档。

# PARAMETERS

**-L, --language** _LANG_
> 按名称或文件扩展名指定语言。

# DESCRIPTION

**mergiraf** 是一个具备语法感知能力的 Git 合并驱动器，通过解析代码和结构化文件的语法树来解决合并冲突。它支持多种语言，包括 TypeScript、Python、Java、Rust、JSON 和 YAML。

它可以作为 **git merge**、**git rebase** 和 **cherry-pick** 的即插即用驱动器，也可以在出现冲突后手动运行。当无法安全地自动合并时，它会留下清晰的冲突标记供人工审查。

# CAVEATS

无法解决所有冲突——需要理解程序逻辑的语义冲突仍需手动处理。语言支持因文件类型而异。要获得最佳效果，请使用 Git v2.44.0 或更新版本。

# HISTORY

**mergiraf** 由 **Antonin Delpeuch** 创建，使用 **Rust** 编写。源代码托管在 Codeberg 上。

# INSTALL

```pacman: sudo pacman -S mergiraf```

```apk: sudo apk add mergiraf```

```zypper: sudo zypper install mergiraf```

```brew: brew install mergiraf```

```nix: nix profile install nixpkgs#mergiraf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-merge](/man/git-merge)(1), [git-mergetool](/man/git-mergetool)(1)
