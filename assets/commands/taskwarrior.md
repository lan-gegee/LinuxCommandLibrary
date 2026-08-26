# TAGLINE

命令行任务与待办事项管理器

# TLDR

**添加新任务**

```task add [Buy groceries]```

**列出所有待办任务**

```task list```

**将任务标记为已完成**

```task [1] done```

**添加带项目和优先级的任务**

```task add [description] project:[Home] priority:[H]```

**添加带截止日期的任务**

```task add [description] due:[tomorrow]```

**添加带标签的任务**

```task add [description] +[work] +[urgent]```

**开始处理某个任务**

```task [1] start```

**查看任务详细信息**

```task [1] info```

**删除任务**

```task [1] delete```

**同步任务**

```task sync```

# SYNOPSIS

**task** [_filter_] [_command_] [_modifications_]

# COMMANDS

**add** _description_：创建新任务。

**done**：将任务标记为已完成。

**delete**：删除任务。

**start**：将任务标记为已开始。

**stop**：将任务标记为已停止。

**modify**：修改任务属性。

**annotate**：为任务添加备注。

**edit**：在文本编辑器中编辑任务。

**list**：显示待办任务。

**all**：显示包括已完成在内的所有任务。

**next**：显示最紧急的任务。

**active**：显示已开始的任务。

**blocked**：显示被阻塞的任务。

**projects**：列出所有项目。

**tags**：列出所有标签。

**reports**：列出可用的报告。

**sync**：与同步服务器或云端后端同步。

**undo**：撤销上一次更改。

**purge**：永久移除已删除的任务。

**shell**：交互式任务 Shell。

**config**：修改配置。

# MODIFICATIONS

**project:**_name_：指派到项目。

**priority:**_H|M|L_：设置优先级（高/中/低）。

**due:**_date_：设置截止日期。

**scheduled:**_date_：设置计划日期。

**until:**_date_：设置失效日期。

**recur:**_freq_：设置重复频率（daily、weekly、monthly）。

**wait:**_date_：在该日期前隐藏。

**+**_tag_：添加标签。

**-**_tag_：移除标签。

**depends:**_id_：设置任务依赖。

# DESCRIPTION

**Taskwarrior**（即 `task` 命令）是一个命令行待办清单管理器。它提供灵活的任务管理，支持项目、优先级、标签、截止日期、重复任务和依赖关系。

任务可以按任意属性、日期或逻辑表达式进行过滤。该工具能生成多种报告，包括列表、日历和燃尽图。

配置存储在 `~/.taskrc` 中，具有丰富的自定义选项。工具支持用于自动化的钩子（hooks），以及跨设备共享任务的同步功能。

从 **Taskwarrior 3.0**（2024 年）开始，数据存储在本地 SQLite 数据库（`taskchampion.sqlite3`）中，同步则使用支持 AWS S3、Google Cloud Storage 或 `taskchampion-sync-server` 的新后端。旧版 `taskd` 服务器不再受支持。

# CAVEATS

首次运行会创建 `~/.taskrc`。任务 ID 会随着任务完成而变化；在脚本中请使用 UUID 作为永久引用。某些报告需要足够的终端宽度才能正常显示。Taskwarrior 3.x 的存储方式与 Syncthing 或 rsync 等文件同步工具不兼容，因为数据存放在 SQLite 数据库中。

# HISTORY

**Taskwarrior** 由 Paul Beckingham 和 Federico Hernandez 创建。首个版本于 2006 年发布，此后项目逐渐发展成一个任务管理生态。Taskwarrior 3.0（2024 年）用 TaskChampion 库和新的同步协议取代了基于文件的存储和 `taskd` 服务器。

# INSTALL

```zypper: sudo zypper install taskwarrior```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[timew](/man/timew)(1), [todo.txt-cli](/man/todo.txt-cli)(1)
