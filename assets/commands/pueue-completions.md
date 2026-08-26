# TAGLINE

为 pueue 生成 shell 补全脚本

# TLDR

**生成 bash 补全**

```pueue completions bash [output_directory]```

**生成 zsh 补全**

```pueue completions zsh [output_directory]```

**生成 fish 补全**

```pueue completions fish [output_directory]```

**生成 elvish 补全**

```pueue completions elvish [output_directory]```

**生成 PowerShell 补全**

```pueue completions power-shell [output_directory]```

# SYNOPSIS

**pueue** **completions** _shell_ _output-directory_

# PARAMETERS

_shell_
> 要生成补全的 Shell：**bash**、**elvish**、**fish**、**power-shell** 或 **zsh**。

_output-directory_
> 补全文件的写入目录。文件名由 Pueue 决定（如 zsh 为 _pueue_，fish 为 **pueue.fish**）。

# DESCRIPTION

**pueue completions** 将 **pueue** 客户端的 shell 补全脚本写入磁盘上的某个目录。生成的文件名取决于 shell：bash 为 **pueue.bash**，zsh 为 **_pueue**，fish 为 **pueue.fish**，等等。生成后，应将该文件 source 或放置到 shell 的补全路径目录中（例如 bash 的 **~/.local/share/bash-completion/completions/** 或 zsh 的 **$fpath**）。

# CAVEATS

与许多将补全打印到 stdout 的 Rust CLI 工具不同，**pueue completions** 以目标目录作为第二个参数并将文件写入其中。基于管道的重定向无法工作。

# SEE ALSO

[pueue](/man/pueue)(1)
