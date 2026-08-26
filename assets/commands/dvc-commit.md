# TAGLINE

记录对 DVC 跟踪文件的更改

# TLDR

**将更改提交到 .dvc 文件**

```dvc commit```

**提交特定文件**

```dvc commit [data.csv.dvc]```

**带消息提交**

```dvc commit -m "[message]"```

**强制提交**

```dvc commit -f```

# SYNOPSIS

**dvc** **commit** [_options_] [_targets_...]

# PARAMETERS

**-f**, **--force**
> 即使未发生更改也强制提交。

**-m**, **--message** _msg_
> 提交消息。

**-R**, **--recursive**
> 递归地提交。

# DESCRIPTION

**dvc commit** 更新 .dvc 元数据文件，以反映对工作区中被跟踪数据文件的更改。修改 DVC 跟踪的文件后，其哈希值将不再与 .dvc 文件中存储的哈希值一致。运行 dvc commit 会计算新的哈希值并相应地更新 .dvc 文件。

这类似于 git commit，但针对的是 DVC 跟踪的数据：它记录你有意更改了该文件，并希望对这个新状态进行版本控制。该命令会将新版本移入 DVC 缓存并更新元数据。

在编辑数据文件、向被跟踪的目录添加内容或替换被跟踪的文件之后，可使用 dvc commit。随后可将更新后的 .dvc 文件提交到 Git，从而在项目历史中创建一个新的数据版本。

# INSTALL

```brew: brew install dvc```

```nix: nix profile install nixpkgs#dvc```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dvc-add](/man/dvc-add)(1)
