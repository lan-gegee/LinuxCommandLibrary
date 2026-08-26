# TAGLINE

编辑和管理 PATH 环境变量的 TUI

# TLDR

**启动 PATH 编辑器**

```pathos```

# SYNOPSIS

**pathos**

# DESCRIPTION

**pathos** 是一个终端用户界面，用于交互式编辑 shell 的 PATH 环境变量。你可以用它重排、添加和删除目录，并借助彩色标记识别状态：黄色表示当前位置，红色表示不存在的目录，青色表示重复项。更改会写入 **~/pathos.sh**，必须 source 该文件才能生效。

该工具旨在清理积累在 **.zshrc**、**.bashrc** 等 shell 资源文件中的 PATH 变量。保存时会生成一条修订后的 `export $PATH` 语句。

# CAVEATS

更改不会自动生效。必须在 shell 配置中 source **~/pathos.sh** 才能让修改持久生效。安装方式：`go install github.com/chip/pathos@latest`。

# HISTORY

**pathos** 由 **chip** 创建，使用 **Go** 编写。

# SEE ALSO

[export](/man/export)(1), [env](/man/env)(1), [direnv](/man/direnv)(1)
