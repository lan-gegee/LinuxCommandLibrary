# TAGLINE

从 Git 仓库历史中移除不需要的数据

# TLDR

**从历史中移除**文件

```bfg --delete-files [secrets.txt] [repo.git]```

**移除**大文件

```bfg --strip-blobs-bigger-than [100M] [repo.git]```

**替换**历史中的文本

```bfg --replace-text [passwords.txt] [repo.git]```

**删除**文件夹

```bfg --delete-folders [.svn] [repo.git]```

# SYNOPSIS

**bfg** [_options_] _repository_

# DESCRIPTION

**bfg**（BFG Repo-Cleaner）是 git-filter-branch 的替代品，更快、更简单，用于从 Git 仓库中移除不需要的数据。它专为清理仓库历史中误提交的密码、大文件或其他敏感数据而设计。

该工具比 git-filter-branch 快得多，对于常见的清理任务也更易用。

# PARAMETERS

**--delete-files** _pattern_ (**-D**)
> 删除指定名称的文件（例如 '*.class'、'*.{txt,log}'）

**--delete-folders** _name_
> 删除指定名称的文件夹（例如 '.svn'、'*-tmp'）

**--strip-blobs-bigger-than** _size_ (**-b**)
> 剥离大于给定大小的 blob（例如 128K、1M、100M）

**--strip-biggest-blobs** _num_ (**-B**)
> 剥离最大的前 NUM 个 blob

**--strip-blobs-with-ids** _file_ (**-bi**)
> 剥离文件中列出的 Git 对象 id 对应的 blob

**--replace-text** _file_ (**-rt**)
> 过滤文件内容，替换匹配的文本（每行一个模式）

**--convert-to-git-lfs** _pattern_
> 将指定名称的文件（例如 '*.zip'）提取到 Git LFS

**--no-blob-protection**
> 允许 BFG 修改甚至你最新的提交

**--private**
> 将此次重写视为移除私有数据（抑制公开数据提示）

# WORKFLOW

```bash
# Clone a mirror
git clone --mirror https://github.com/user/repo.git

# Run BFG
bfg --delete-files passwords.txt repo.git

# Clean up and push
cd repo.git
git reflog expire --expire=now --all
git gc --prune=now --aggressive
git push --force
```

# REPLACE TEXT FORMAT

包含模式的文件（passwords.txt）：
```
PASSWORD1==>***REMOVED***
secret_key==>***REMOVED***
```

# FEATURES

- 比 git-filter-branch 快 10 到 1000 倍
- 基于简单模式的删除
- 默认保护当前提交
- 批量文本替换
- 大文件清理
- 文件夹删除

# CAVEATS

会重写历史（需要强制推送）。默认保护 HEAD（可用 --no-blob-protection 覆盖）。协作者必须变基或重新克隆。BFG 按文件名和大小而非路径操作：它无法只删除某个目录下的同名文件。需要按路径或其他复杂方式重写时，请使用 git-filter-repo。需要 Java 11+ 运行时（v1.14.0 是最后一个支持 Java 8 的版本）。

# HISTORY

**BFG Repo-Cleaner** 由 Roberto Tyley 于 **2012 年**创建，旨在提供比 git-filter-branch 更快、更友好的仓库清理方案。

# INSTALL

```aur: yay -S bfg```

```brew: brew install bfg```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[git-filter-branch](/man/git-filter-branch)(1), [git-filter-repo](/man/git-filter-repo)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/rtyley/bfg-repo-cleaner)```

```[Homepage](https://rtyley.github.io/bfg-repo-cleaner/)```

<!-- verified: 2026-06-19 -->
