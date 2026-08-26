# TAGLINE

管理大文件存储

# TLDR

**为仓库安装 LFS**

```git lfs install```

**跟踪文件模式**

```git lfs track "*.psd"```

**显示已跟踪的模式**

```git lfs track```

**列出 LFS 文件**

```git lfs ls-files```

**获取 LFS 对象**

```git lfs fetch```

# SYNOPSIS

**git lfs** _command_ [_options_]

# PARAMETERS

**install**
> 为仓库设置 LFS。

**track** _PATTERN_
> 跟踪匹配模式的文件。

**untrack** _PATTERN_
> 停止跟踪某个模式。

**ls-files**
> 列出被跟踪的 LFS 文件。

**fetch**
> 下载 LFS 对象。

**pull**
> 获取并检出 LFS 文件。

**push**
> 将 LFS 对象推送到远程。

**lock** _PATH_
> 在服务器上锁定文件，使只有你能向其推送更改。

**unlock** _PATH_
> 释放服务器端锁。

**locks**
> 列出已锁定的文件。

**status**
> 显示被 LFS 跟踪的文件状态。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git lfs**（Large File Storage）管理 Git 仓库中的大文件。它不会将大型二进制文件直接存入仓库，而是将其替换为轻量的指针文件，并把实际内容存储在单独的 LFS 服务器上。

LFS 只按需下载大文件，从而显著缩小仓库体积并缩短克隆时间。它与标准 Git 命令透明集成，因此 `git add`、`git commit` 和 `git push` 都能按预期工作，而 LFS 在幕后高效地处理内容存储。

# CONFIGURATION

**.gitattributes**
> 指定哪些文件模式由 LFS 跟踪。

```
*.psd filter=lfs diff=lfs merge=lfs -text
*.zip filter=lfs diff=lfs merge=lfs -text
```

**.lfsconfig**
> 仓库专属的 LFS 配置，包括端点 URL 等。

# CAVEATS

需要 LFS 服务器支持。可能有存储限制。部分托管服务设有 LFS 配额。

# HISTORY

Git LFS 由 **GitHub** 与 Atlassian 于 **2015 年**共同创建，旨在解决 git 仓库中大文件这一长期存在的问题。

# INSTALL

```apt: sudo apt install git-lfs```

```dnf: sudo dnf install git-lfs```

```pacman: sudo pacman -S git-lfs```

```apk: sudo apk add git-lfs```

```zypper: sudo zypper install git-lfs```

```brew: brew install git-lfs```

```nix: nix profile install nixpkgs#git-lfs```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [git-annex](/man/git-annex)(1)

# RESOURCES

```[Source code](https://github.com/git-lfs/git-lfs)```

```[Homepage](https://git-lfs.com/)```

```[Documentation](https://github.com/git-lfs/git-lfs/tree/main/docs)```

<!-- verified: 2026-07-17 -->
