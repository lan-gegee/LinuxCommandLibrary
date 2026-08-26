# TAGLINE

将补丁系列下载为可直接应用的 mbox

# TLDR

**按 message-id 获取系列**

```b4 am [message-id]```

**从归档 URL 获取系列**

```b4 am [https://lore.kernel.org/.../message-id]```

**应用从 cover letter 回复中收集的评审 trailer**

```b4 am -t [message-id]```

**添加指回消息归档的 Link trailer**

```b4 am -l [message-id]```

**将 mbox 写入指定目录**

```b4 am -o [path/to/dir] [message-id]```

**获取系列的特定修订版**

```b4 am -v [3] [message-id]```

# SYNOPSIS

**b4** **am** [_options_] _msgid_

# DESCRIPTION

**b4 am** 从 public-inbox 归档中取回完整的补丁线程，选出该系列的最新修订版，并生成一个干净的 mbox 文件，可以直接交给 **git am** 应用。过程中它会收集评审者在回复中留下的 trailer（Reviewed-by、Acked-by、Tested-by），并将其应用到对应的补丁上。

生成的 mbox 以该系列命名，默认保存在当前目录。与 **b4 shazam** 不同，这个子命令只负责写出 mbox，不会触碰工作区，把实际应用补丁的工作留给维护者完成。

# PARAMETERS

**-o** _DIR_, **--outdir** _DIR_
> 将生成的 mbox 写入 _DIR_ 而不是当前目录。

**-v** _VER_, **--use-version** _VER_
> 获取该系列的指定修订版，而不是最新修订版。

**-t**, **--apply-cover-trailers**
> 将 cover letter 上发现的 trailer 应用到系列中的每个补丁。

**-T**, **--no-add-trailers**
> 不添加也不重排任何 trailer。

**-s**, **--add-my-sob**
> 为每个补丁添加你自己的 Signed-off-by trailer。

**-l**, **--add-link**
> 为每条消息添加包含其归档 URL 的 Link trailer。

**-P** _RANGE_, **--cherry-pick** _RANGE_
> 只应用系列中的一个补丁子集。

**-c**, **--check-newer-revisions**
> 若邮件列表上存在该系列的更新修订版则发出警告。

**-m** _MBOX_, **--use-local-mbox** _MBOX_
> 从本地 mbox 文件读取线程，而不是联网获取。

**-3**, **--prep-3way**
> 准备后备 blob，以便 **git am -3** 能够解决冲突。

# INSTALL

```dnf: sudo dnf install b4```

```pacman: sudo pacman -S b4```

```apk: sudo apk add b4```

```zypper: sudo zypper install b4```

```brew: brew install b4```

```nix: nix profile install nixpkgs#b4```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b4](/man/b4)(1), [b4-shazam](/man/b4-shazam)(1), [git-am](/man/git-am)(1)

# RESOURCES

```[Documentation](https://b4.docs.kernel.org/)```

<!-- verified: 2026-06-10 -->
