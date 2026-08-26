# TAGLINE

配有开放测试套件的本地 LeetCode 运行器

# TLDR

按题目 ID **提交** Python 解答

```openleetcode submit ./solution.py --id 1```

按标题子串**提交** C++ 解答

```openleetcode submit ./solution.cpp --title two-sum```

扩展名有歧义时**覆盖**语言检测

```openleetcode submit ./main.abc --id 1 --lang python3```

将测试和运行时模板**下载**到数据目录

```openleetcode download all```

仅**下载**测试清单

```openleetcode download tests```

**列出**后端类型、URL 和配置文件路径

```openleetcode config list```

将 CLI **指向**某个 Piston 后端

```openleetcode config set backend.url http://localhost:2000```

**重新运行**官方安装程序以更新 CLI

```openleetcode update```

# SYNOPSIS

**openleetcode** [**--plain**] [**--no-color**] [**--version**] _command_ [_args_]

**openleetcode submit** _PATH_ {**--id** _INT_ | **--title** _STR_} [**--lang** _LANG_]

**openleetcode download** {**all** | **runtimes** | **tests**}

**openleetcode config list**

**openleetcode config set** _KEY_ _VALUE_

**openleetcode update**

# PARAMETERS

**--plain**
> 禁用动画和颜色。输出为面向行的格式（`scope: message`）。

**--no-color**
> 禁用 ANSI 颜色。环境变量 `NO_COLOR` 具有同样效果。

**--version**
> 打印 `openleetcode <version>` 后退出。

**submit** _PATH_
> 针对本地测试套件运行解答文件。必须提供 **--id** 或 **--title** 之一。

**--id** _INT_
> 题目 ID（例如 Two Sum 为 `1`）。两者同时给出时优先于 **--title**。

**--title** _STR_
> 与已下载测试树下题目目录名称进行匹配的子串。使用第一个匹配项。

**--lang** _LANG_
> 覆盖基于文件扩展名的语言检测。支持的值包括 `cpp`、`rust`、`python3`、`python2`、`ruby`、`java`、`csharp`、`kotlin`、`go`、`dart`、`swift` 和 `typescript`。

**download** {**all** | **runtimes** | **tests**}
> 获取上游仓库归档，并将运行时模板、测试清单或两者解压到数据目录。

**config list**
> 打印 `backend.type`、`backend.url` 和配置文件路径。

**config set** _KEY_ _VALUE_
> 写入一个配置键。允许的键：`backend.type`（目前仅 `piston`）和 `backend.url`。

**update**
> 下载官方安装程序并运行（Unix 上为 `bash`，Windows 上为 PowerShell）。

# DESCRIPTION

**openleetcode** 是一个用 Haskell 编写的 CLI，可在你自己的机器上评判 LeetCode 风格的解答。它读取普通的解答文件，在已下载的开放测试套件中找到匹配的题目清单，将代码包装进特定语言的处理框架，把这一批任务发送给可插拔的执行后端，并在本地给出类似 LeetCode 的判定结果。

CLI 只起粘合作用。测试以每题一个目录的形式存放（`manifest.yaml` 加参考解答）。运行时模板（入口 `main` 以及数组、链表、树等 LeetCode 类型的辅助代码）与它们放在一起。两者都不打包在二进制文件内：首次交互式启动会创建 XDG 配置目录并提议下载这两类内容。非交互式启动会跳过该提示；你需要自己运行 **openleetcode download all**。

**submit** 需要一个选择器。**--id** 在 `tests/<range>/` 下查找名称以 `<id>.` 开头的目录。**--title** 对目录名做子串搜索并取第一个命中项。除非设置了 **--lang**，否则语言由文件扩展名决定。运行器与所配置的后端通信（默认是位于 `http://localhost:2000` 的 Piston）；批处理超时时间为 20 秒。判定结果包括 accepted（通过）、wrong answer（答案错误）、time limit exceeded（超出时间限制）和 runtime error（运行时错误）。本项目与 LeetCode 无从属关系；它的目标是让导入和环境尽量接近官方的语言配置。

# CONFIGURATION

**$XDG_CONFIG_HOME/openleetcode/** (默认 **~/.config/openleetcode/**)
> 首次运行时创建的数据目录。存放 `config.yml`、解压后的 `runtimes/` 和 `tests/`。

**config.yml**
> 包含 `backendType` 和 `backendUrl` 的 YAML 文件。缺失时会自动以默认值创建。解析出错时会回退到默认值并打印警告。

**backend.type** / **backend.url**
> **config set** 使用的 CLI 配置键。唯一允许的类型是 `piston`。默认 URL 为 `http://localhost:2000`。

**OPENLEETCODE_BACKEND_URL**
> 创建新配置时用作默认后端 URL。不会覆盖已有的 `config.yml`。

默认的 Piston 后端可通过仓库中的 `docker compose -f backends/piston/docker-compose.yml up -d` 启动。Linux 和 macOS 安装程序会尝试启动该 compose 文件；Windows 仅安装 CLI。

# CAVEATS

评判需要可访问的后端。如果 Piston 未运行，**submit** 会以基础设施错误退出并建议使用 **config list**。测试和运行时模板必须已经下载；缺少套件时会打印 "test suite not found"。**--title** 是不带锚定的子串匹配并取第一个命中项，因此较短的标题可能匹配到错误的题目。清单由社区维护，质量参差不齐。**update** 会重新运行远程安装脚本。退出码：**0**（成功/accepted）、**1**（输入有误：缺少选择器、未知扩展名、缺少套件）、**2**（基础设施问题：后端、下载、配置写入）以及 **3**（解答判定未通过）。

# HISTORY

由 **therepanic** 使用 **Haskell**（Cabal）编写。仓库于 **2026 年 1 月**发布。采用 **Unlicense** 许可证。可执行文件名为 **openleetcode**。

# SEE ALSO

[docker](/man/docker)(1), [docker-compose](/man/docker-compose)(1), [cabal](/man/cabal)(1), [python](/man/python)(1), [rustc](/man/rustc)(1)

# RESOURCES

```[Source code](https://github.com/therepanic/openleetcode)```

<!-- verified: 2026-08-18 -->
