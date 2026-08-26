# TAGLINE

将本地提交上传到远程

# TLDR

**推送到远程**

```git push [origin] [branch]```

**推送并设置上游**

```git push -u [origin] [branch]```

**推送所有分支**

```git push --all```

**推送标签**

```git push --tags```

**安全地强制推送**

```git push --force-with-lease```

**删除远程分支**

```git push [origin] --delete [branch]```

# SYNOPSIS

**git push** [_options_] [_remote_] [_refspec_]

# PARAMETERS

_REMOTE_
> 远程仓库名称（例如 origin）。

_REFSPEC_
> 要推送的引用（例如分支名或 src:dst）。

**-u**, **--set-upstream**
> 为分支设置上游跟踪引用。

**--all**
> 推送所有分支。

**--tags**
> 推送 refs/tags 下的所有引用。

**--force**
> 强制更新远程引用，即使不是 fast-forward。

**--force-with-lease**
> 仅当远程引用与上次抓取的内容一致时才强制推送。

**--force-if-includes**
> 若远程跟踪引用存在尚未在本地整合的更新，则拒绝强制更新。

**--delete**
> 删除指定的远程引用。

**--dry-run**
> 执行除实际发送更新之外的一切操作。

**--no-verify**
> 跳过 pre-push 钩子。

**-q**, **--quiet**
> 抑制全部输出，包括已更新引用的列表。

**-v**, **--verbose**
> 详细运行。

**--progress**
> 即使 stderr 不是终端也强制输出进度状态。

**--prune**
> 删除没有本地对应分支的远程分支。

**-o** _option_, **--push-option** _option_
> 向服务端 receive 钩子传递字符串。

**--porcelain**
> 产生机器可读的输出。

# DESCRIPTION

**git push** 将本地提交上传到远程仓库，用本地引用更新远程引用，并传输补全这些提交所需的对象。本地工作正是通过它才得以与协作者共享。

`--force-with-lease` 选项是 `--force` 的更安全替代：它在覆盖之前会检查远程自你上次抓取以来是否被更新过。`-u` 标志设置上游跟踪，简化之后的 push 和 pull 命令。

# CAVEATS

强制推送会覆盖远程历史。为安全起见请使用 --force-with-lease。分支保护规则可能限制推送。

# HISTORY

git push 是 **Git** 自初始发布就有的核心命令，通过实现提交共享支撑了分布式工作流。

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

[git-pull](/man/git-pull)(1), [git-fetch](/man/git-fetch)(1), [git-remote](/man/git-remote)(1)
