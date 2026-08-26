# TAGLINE

将闪卡导入 Anki 的 CLI 与管道框架

# TLDR

**将 CSV 卡片导入**牌组（默认使用 Basic 笔记类型）

```hanky pipe [words.csv] --into [english::vocab]```

将目录下**每个匹配的文件导入**嵌套牌组

```hanky pipe-dir [french/] ["*.csv"] -r```

**覆盖 Anki 笔记类型**/模型名称

```hanky pipe [cards.csv] -m [Basic] --into [deck]```

**试运行**各处理器而不写入 collection

```hanky pipe [words.csv] --dry-run```

对每张处理的卡片输出**详细报告**

```hanky pipe [words.csv] -v --into [deck]```

以与 hanky 可执行文件相同的方式**运行自定义管道脚本**

```python3 [my_script.py] pipe [words.csv] --into [english::vocab]```

# SYNOPSIS

**hanky** **pipe** [**-m** _MODEL_] [**--into** _DECK_] [**--fail-fast**] [**--dry-run**] [**-v**] [**--args** _K=V_ ...] _file_

**hanky** **pipe-dir** [**-m** _MODEL_] [**-r**] [**--fail-fast**] [**--dry-run**] [**-v**] [**--args** _K=V_ ...] _dir_ _pattern_

# PARAMETERS

**pipe** _file_
> 从单个文件（**.csv**、**.json** 或已注册的扩展名）读取卡片并将其添加到 Anki。

**pipe-dir** _dir_ _pattern_
> 加载 _dir_ 下匹配 glob 模式 _pattern_ 的多个文件。牌组名称由相对路径派生（例如 **french/animals.csv** → **french::animals**）。

**-m** _MODEL_, **--model** _MODEL_
> 覆盖新卡片使用的 Anki 模型（笔记类型）。独立运行的 **hanky** 默认为 **Basic**；管道脚本则在 **HankyPipeline(...)** 中设置模型。

**--into** _DECK_
> **pipe** 的目标牌组。默认为不含扩展名的输入文件名。

**-r**, **--recursive**
> 对 **pipe-dir** 而言，同时深入子目录。

**--fail-fast**
> 遇到第一张无法添加的卡片就停止并抛出错误，而不是跳过并在最后统一报告。

**--dry-run**
> 运行卡片处理器并报告结果，但不修改 Anki collection（不创建牌组、媒体、卡片或备份）。

**-v**, **--verbose**
> 在处理器运行后打印每张卡片的字典，并在最终报告中附上错误信息。

**--args** _K=V_
> 转发给自定义卡片处理器的键值对（仅限管道脚本）。可重复指定。

# DESCRIPTION

**hanky** 是一个 Python CLI 和库，它从文件（或脚本内的数据源）读取闪卡，可选择通过用户自定义的**卡片处理器**进行转换，然后将笔记写入本地 **Anki** collection。它面向 ETL 式工作流：抓取或 OCR 材料、充实字段（翻译、例句、TTS 音频），再批量导入牌组。

内置的 **pipe** / **pipe-dir** 命令在列名或键名与目标笔记类型字段一致时，开箱即可处理 CSV 和 JSON。若需自定义逻辑，可以安装该软件包，编写一个小脚本在 **HankyPipeline** 上注册 **@hanky.card_processor** 函数，然后调用 **hanky.run()**，这样就能通过 **python3 my_script.py pipe ...** 获得同样的 CLI 界面。处理器可以通过 **CardMedia** 附加音频媒体（**.mp3**、**.oga**、**.opus**、**.wav**、**.weba**、**.aac**）。还可以为 Excel 等格式注册自定义文件加载器。

hanky 只**添加**卡片、媒体和牌组。笔记类型（模型）必须已存在于 collection 中；请先在 Anki 界面里创建它们。需要 Python **3.11+** 和本地 Anki collection 数据库。与 AnkiWeb 或 Anki 项目无从属关系。

# CONFIGURATION

**~/.config/hanky/hanky.toml**
> 可选的 TOML 配置文件。主要在不使用默认 Anki 配置文件（**User 1**）或在 Windows 上时才需要。

**ANKI_DB_PATH**
> Anki collection SQLite 文件（**collection.anki2**）的路径。默认为平台 Anki2 数据目录下的 **User 1** 配置文件。

**DO_SAFETY_CHECK**
> 为 true（默认）时，若另一个进程（例如 Anki）似乎正占用该 collection，则拒绝打开。

**ALLOW_DUPLICATES**
> 为 false（默认）时，跳过与现有笔记重复的卡片。

**BACKUP_FOLDER**
> 写入之前存放 collection 备份的目录。默认：**~/.local/share/hanky/backups**。

在脚本中传给 **HankyPipeline** 的 **Config** 对象会覆盖上述文件配置。

# CAVEATS

写入 collection 前请先关闭 Anki（或者仅在你接受损坏风险的前提下才禁用安全检查）。笔记类型必须预先存在；hanky 不会创建模型。重复检测和字段名称取决于你的笔记类型。Windows 和非默认配置文件几乎总是需要设置 **ANKI_DB_PATH**。调用外部 API（翻译、TTS、视觉识别）的自定义处理器需要自备凭据和依赖。

# HISTORY

由 **HBA** 编写，是以 MIT 许可证发布在 PyPI 上的开源 Python 软件包。同时提供 **hanky** 控制台脚本和用于可编程 Anki 导入管道的库 API。

# SEE ALSO

[anki](/man/anki)(1), [python](/man/python)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/Haeata-Ash/hanky)```

<!-- verified: 2026-07-23 -->
