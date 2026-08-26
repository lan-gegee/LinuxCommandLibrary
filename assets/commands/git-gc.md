# TAGLINE

清理不必要的文件并优化本地仓库

# TLDR

**运行垃圾回收**

```git gc```

**激进清理**（重新计算增量，较慢）

```git gc --aggressive```

**立即修剪所有不可达对象**

```git gc --prune=now```

**仅在需要整理时才运行 gc**

```git gc --auto```

**即使另一个实例可能正在运行也强制执行 gc**

```git gc --force```

**不带进度输出地运行**

```git gc --quiet```

# SYNOPSIS

**git gc** [_options_]

# PARAMETERS

**--aggressive**
> 重新计算增量以实现更彻底的优化。明显更慢。

**--prune=**_date_
> 修剪早于指定日期的松散对象（默认：两周前，可通过 gc.pruneExpire 配置）。

**--no-prune**
> 不修剪任何松散对象。

**--auto**
> 仅在根据 gc.auto 阈值判断需要整理时才运行。

**--cruft**
> 将不可达对象打包进 cruft 包而不是保持松散（默认：开启）。

**--no-cruft**
> 将不可达对象保留为松散对象，而不打包进 cruft 包。

**--quiet**
> 抑制所有进度报告。

**--force**
> 即使此仓库上可能已有另一个 git gc 实例在运行，仍强制执行 gc。

**--keep-largest-pack**
> 将除最大的非 cruft 包和 .keep 包之外的所有包合并为单个包。

# DESCRIPTION

**git gc**（garbage collection，垃圾回收）清理不必要的文件并优化本地仓库。它会打包松散对象、移除不可达对象并压缩文件修订版本，以获得更好的性能和更低的磁盘占用。

Git 会在某些操作（如 merge、rebase）之后自动运行 gc。手动执行 gc 在历史改写、大规模导入或磁盘占用偏高时很有用。**--aggressive** 模式从头重新计算所有增量以进行更深层的优化，但耗时明显更长。默认 **--prune** 的两周宽限期可以保护可能被并发操作引用的对象。

# CAVEATS

激进的 gc 在大型仓库上非常慢。gc 运行后，悬空对象会在修剪宽限期过后被移除。请让 gc 完成后再进行其他仓库操作。锁文件机制可防止多个 gc 实例并发运行。

# HISTORY

git gc 是用于仓库维护的 **Git** 核心命令，将原本独立的 git-prune 和 git-repack 等清理任务自动化。

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

[git-prune](/man/git-prune)(1), [git-repack](/man/git-repack)(1), [git-reflog](/man/git-reflog)(1), [git-fsck](/man/git-fsck)(1), [git-count-objects](/man/git-count-objects)(1)
