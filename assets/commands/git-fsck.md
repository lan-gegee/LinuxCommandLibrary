# TAGLINE

验证仓库对象的连接性与有效性

# TLDR

**检查仓库完整性**

```git fsck```

**检查并显示不可达对象**

```git fsck --unreachable```

**仅检查连通性**（更快，跳过 blob 内容）

```git fsck --connectivity-only```

**将悬空对象写入 .git/lost-found** 以便恢复

```git fsck --lost-found```

**带对象命名的详细检查**

```git fsck --verbose --name-objects```

**不考虑 reflog 引用的检查**

```git fsck --no-reflogs```

**严格检查**以进行更严格的验证

```git fsck --strict```

# SYNOPSIS

**git** **fsck** [_options_] [_objects_...]

# PARAMETERS

**--unreachable**
> 打印存在但无法从任何引用节点到达的对象。

**--dangling**
> 打印存在但从未被直接使用的对象（默认）。

**--no-dangling**
> 从输出中省略悬空对象信息。

**--full**
> 检查备用对象库和包文件中的对象。这现在是默认行为。

**--connectivity-only**
> 只检查可达对象的连通性，跳过 blob 内容。速度更快，但无法检测损坏的 blob。

**--strict**
> 启用更严格的检查，例如捕获设置了 g+w 位的文件模式。

**--lost-found**
> 将悬空对象写入 .git/lost-found/commit/ 或 .git/lost-found/other/。

**--no-reflogs**
> 判断可达性时不考虑 reflog 条目。

**--cache**
> 将索引中的对象视为可达性追踪的起始节点。

**--root**
> 报告根节点。

**--tags**
> 报告标签。

**--name-objects**
> 显示描述性名称，说明对象如何可达（如 HEAD~25^2:src/）。

**--verbose**
> 输出详细信息。

**--progress**, **--no-progress**
> 强制或抑制进度状态报告。

# DESCRIPTION

**git fsck**（file system check）对 Git 对象数据库中的所有对象执行完整性验证。它验证对象格式是否良好、连接是否正确，以及仓库结构是否一致且未损坏。

该命令检查损坏的对象、断裂的链接、无效的对象类型，以及存在但未被任何分支或标签引用的不可达对象。不可达对象通常源于变基、修正提交或删除分支等操作，可以通过 --lost-found 选项找回意外删除的工作。

建议在怀疑仓库损坏、磁盘出错或硬件故障之后定期运行 fsck。--full 选项（现为默认）将检查范围扩展到包文件内的对象。需要更快的检查时可使用 --connectivity-only，它会跳过 blob 内容的验证。

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

[git-gc](/man/git-gc)(1), [git-prune](/man/git-prune)(1), [git-reflog](/man/git-reflog)(1)
