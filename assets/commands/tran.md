# TAGLINE

使用 TUI 在计算机之间安全传输文件

# TLDR

**打开文件浏览器 TUI**

```tran```

**在指定目录中打开 TUI**

```tran --start-dir [/path/to/dir]```

**向远程计算机发送文件或目录**

```tran send [file_or_directory]```

**从远程计算机接收文件**

```tran receive [password]```

**进行 GitHub 身份验证**

```tran auth login```

**同步 tran 配置文件**

```tran sync start```

# SYNOPSIS

**tran** [_options_] [_command_]

# PARAMETERS

**--start-dir** _path_
> 设置 TUI 的起始目录。

# SUBCOMMANDS

**send** _file_or_directory_
> 向远程计算机发送文件或目录。

**receive** _password_
> 使用密码从远程计算机接收文件。

**auth login**
> 进行 GitHub 身份验证。

**sync start**
> 同步你的 tran 配置文件。

# DESCRIPTION

**tran** 是一个命令行工具和 TUI，可在计算机之间安全地传输和发送文件与目录。它提供文件浏览器界面用于选择文件，并使用基于密码的身份验证来接收传输。

配置保存在 **~/.config/tran/tran.yml**。

# HISTORY

**tran** 由 **abdfnx** 创建，使用 **Go** 编写。

# INSTALL

```nix: nix profile install nixpkgs#tran```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[croc](/man/croc)(1), [portal](/man/portal)(1)
