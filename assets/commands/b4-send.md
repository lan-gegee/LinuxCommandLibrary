# TAGLINE

将准备好的补丁系列发送给收件人

# TLDR

**发送当前**已准备好的系列

```b4 send```

**仅预览不发送**，看看将要发出什么

```b4 send -d```

**发送测试副本**，只发给自己

```b4 send --reflect```

**将消息写入目录**而不是发送

```b4 send -o [path/to/dir]```

**发送前编辑 cover letter**

```b4 send --edit-cover```

**重发**先前已发送过的修订版

```b4 send --resend```

# SYNOPSIS

**b4** **send** [_options_]

# DESCRIPTION

**b4 send** 发送用 **b4 prep** 准备好的系列。它会把跟踪分支转换成带编号的补丁集，附上保存的 cover letter，填写 To 和 Cc 收件人列表，然后通过你配置好的 SMTP 服务器（或在支持的情况下通过项目的 Web 提交端点）发出消息。

默认情况下 b4 会附加加密证明（attestation），评审者可以据此核实补丁在传输过程中未被篡改。在提交到公开邮件列表之前，请先用 dry-run 和 reflect 选项演练。

# PARAMETERS

**-d**, **--dry-run**
> 打印将要发送的内容，但不实际发送任何东西。

**-o** _DIR_, **--output-dir** _DIR_
> 将消息作为文件写入 _DIR_，而不发送。

**--reflect**
> 只将该系列发送给你自己，用于测试。

**--resend** _[VER]_
> 原样重发之前发送过的修订版。

**--no-sign**
> 不为消息添加加密证明。

**-e**, **--edit-cover**
> 发送前编辑 cover letter。

**--preview-to** _ADDR_
> 向指定的地址发送预览副本。

# CAVEATS

发送前需要配置好可用的 SMTP 或 **git send-email**。发布到公开邮件列表之前，务必先用 **-d** 或 **--reflect** 演练，因为补丁一经发出就无法撤回。

# INSTALL

```dnf: sudo dnf install b4```

```pacman: sudo pacman -S b4```

```apk: sudo apk add b4```

```zypper: sudo zypper install b4```

```brew: brew install b4```

```nix: nix profile install nixpkgs#b4```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[b4](/man/b4)(1), [b4-prep](/man/b4-prep)(1), [git-send-email](/man/git-send-email)(1)

# RESOURCES

```[Documentation](https://b4.docs.kernel.org/)```

<!-- verified: 2026-06-10 -->
