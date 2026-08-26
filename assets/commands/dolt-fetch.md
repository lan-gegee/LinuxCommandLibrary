# TAGLINE

从远程下载对象和引用

# TLDR

**从远程抓取**

```dolt fetch```

**从指定远程抓取**

```dolt fetch [remote]```

**抓取指定分支**

```dolt fetch [remote] [branch]```

**抓取所有远程**

```dolt fetch --all```

# SYNOPSIS

**dolt** **fetch** [_options_] [_remote_] [_refspec_]

# PARAMETERS

**--all**
> 从所有远程抓取。

**--prune**
> 移除过期的远程跟踪分支。

# DESCRIPTION

**dolt fetch** 从远程 Dolt 仓库下载对象、提交和分支引用。它同步本地仓库对远程状态的认知，但不会修改工作集或本地分支。

该命令会更新远程跟踪分支（例如 origin/main），使其反映远程仓库的当前状态。与 pull 不同，fetch 不会自动合并变更，你可以先审阅远程改动再决定是否整合到本地分支。

--prune 选项会移除远程上已不存在的远程跟踪分支，保持本地仓库整洁。在多远程工作流中，同时从所有远程抓取会很有用。

# INSTALL

```pacman: sudo pacman -S dolt```

```brew: brew install dolt```

```nix: nix profile install nixpkgs#dolt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

