# TAGLINE

Google Drive 命令行客户端

# TLDR

在目录中**初始化 drive**

```drive init [~/gdrive]```

从 Google Drive **拉取文件**

```drive pull [path/to/file]```

向 Google Drive **推送文件**

```drive push [path/to/file]```

**列出** Google Drive 中的文件

```drive list```

**拉取全部变更**

```drive pull -all```

**强制推送**

```drive push -force [path]```

**查看差异**

```drive diff [path]```

# SYNOPSIS

**drive** _command_ [_options_] [_path_]

# PARAMETERS

**init**
> 在目录中初始化 drive 上下文。

**pull** [_path_]
> 从 Google Drive 下载文件。

**push** [_path_]
> 向 Google Drive 上传文件。

**list** [_path_]
> 列出文件和目录。

**diff** [_path_]
> 显示本地与远端的差异。

**trash** [_path_]
> 将文件移入回收站。

**untrash** [_path_]
> 从回收站恢复文件。

**delete** [_path_]
> 永久删除文件。

**-all**
> 对所有文件执行操作。

**-force**
> 强制操作，无需确认。

**-no-prompt**
> 禁用确认提示。

**-depth** _n_
> 限制目录遍历深度。

# DESCRIPTION

**drive** 是一款 Google Drive 命令行客户端，刻意借鉴了 Git 的模型：由你显式地 **pull** 和 **push**，而不是让守护进程在后台自动同步。在你发话之前什么都不会动——这正是所有目睹过自动同步客户端扩散错误的人看重它的原因。

`drive init` 会创建一个上下文目录（`.gd/`），把某个本地文件夹标记为 Drive 镜像的根，就像 `.git/` 标记一个仓库那样。后续命令会将本地状态与远端比较并报告将要发生的变更；`drive diff` 只显示差异，不传输任何内容。

注意它的标志是 Go 风格的**单横线**长选项：`-force`、`-no-prompt`、`-depth`，而不是 `--force`。习惯了 GNU 约定的人常常在这里踩坑。

# CAVEATS

该项目**实际上已处于休眠状态**：上游最后一次提交是在 **2024 年**初，而 Google 的 Drive API 和 OAuth 要求仍在不断变化。新安装常常卡在 OAuth 配置上——现在需要在 Google Cloud 项目中注册你自己的客户端凭据，而不再使用内置密钥。

如今对多数人而言 **rclone** 才是更好的选择：它维护活跃，除了 Drive 还支持几十种其他后端，支持服务端复制和加密，同步引擎也强大得多。

它基本没有冲突解决机制。当文件在两端都被修改时，drive 只会询问，而 `-force` 则直接覆盖，一次粗心的 push 就可能丢弃远端的修改。Google Docs、Sheets 和 Slides 并不是真正的文件，无法按原样拉取；必须先导出为具体格式。

# HISTORY

drive 由 **Emmanuel Odeke** 于 **2015 年**编写。当时 Google 完全没有面向 Linux 的官方 Drive 客户端，现有替代品是容易挂起的 FUSE 挂载方案。它那 Git 式的显式 push/pull 模型正是对其他平台上自动同步客户端的直接回应，也因此收获了大批拥趸。此后它被 rclone 超越——后者覆盖同样的场景且功能更广。

# INSTALL

```nix: nix profile install nixpkgs#drive```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rclone](/man/rclone)(1), [gdrive](/man/gdrive)(1), [rsync](/man/rsync)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/odeke-em/drive)```

<!-- verified: 2026-07-14 -->
