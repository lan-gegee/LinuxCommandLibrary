# TAGLINE

获取补丁系列并应用到当前分支

# TLDR

**获取系列并应用**到当前分支

```b4 shazam [message-id]```

**从归档 URL 应用**

```b4 shazam [https://lore.kernel.org/.../message-id]```

**以合并方式引入系列**，而不是线性应用

```b4 shazam -M [message-id]```

**创建 FETCH_HEAD**，以便之后手动 merge 或 cherry-pick

```b4 shazam -H [message-id]```

**应用来自 cover letter 回复的评审 trailer**

```b4 shazam -t [message-id]```

# SYNOPSIS

**b4** **shazam** [_options_] _msgid_

# DESCRIPTION

**b4 shazam** 会完成 **b4 am** 所做的一切（取回线程、挑选最新修订版、收集评审 trailer），然后用 **git am** 将得到的系列直接应用到当前的 git 分支上。它是从 message-id 到工作区中已应用提交的一条龙路径。

使用 **-M** 时，系列会以合并方式引入；使用 **-H** 时，b4 会准备一个 FETCH_HEAD，让你自行决定如何集成。这个名字意在致敬"用一条命令取回并'播放'补丁系列"。

# PARAMETERS

**-H**, **--make-fetch-head**
> 先将系列应用到一个临时 ref 并让 FETCH_HEAD 指向它，方便你随后手动 merge 或 cherry-pick。

**-M**, **--merge**
> 以合并提交的方式引入系列，而不是线性地执行 **git am**。

**-v** _VER_, **--use-version** _VER_
> 应用该系列的特定修订版。

**-t**, **--apply-cover-trailers**
> 将 cover letter 上发现的 trailer 应用到每个补丁。

**-l**, **--add-link**
> 为每条消息添加包含其归档 URL 的 Link trailer。

**-s**, **--add-my-sob**
> 为每个补丁添加你自己的 Signed-off-by trailer。

**-P** _RANGE_, **--cherry-pick** _RANGE_
> 只应用系列中的一个补丁子集。

**-m** _MBOX_, **--use-local-mbox** _MBOX_
> 从本地 mbox 文件读取线程，而不是联网获取。

# CAVEATS

系列会被应用到当前检出（checkout）的分支上，因此运行前请确保自己位于预期的基准提交。b4 会尽力找到正确的基础，但代码树不匹配时仍可能出现 **git am** 冲突。

# INSTALL

```dnf: sudo dnf install b4```

```pacman: sudo pacman -S b4```

```apk: sudo apk add b4```

```zypper: sudo zypper install b4```

```brew: brew install b4```

```nix: nix profile install nixpkgs#b4```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b4](/man/b4)(1), [b4-am](/man/b4-am)(1), [git-am](/man/git-am)(1)

# RESOURCES

```[Documentation](https://b4.docs.kernel.org/)```

<!-- verified: 2026-06-10 -->
