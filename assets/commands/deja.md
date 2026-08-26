# TAGLINE

为 zsh 提供预测式幽灵文本自动建议

# TLDR

**导入**现有的 zsh 历史到本地数据库

```deja import```

**在当前会话中激活** shell 集成

```eval "$(deja init zsh)"```

**检查**后台守护进程是否响应

```deja ping```

**显示**当前的模糊匹配预设

```deja fuzzy```

**收紧**模糊匹配，只接受相邻字符匹配

```deja fuzzy tight```

**向守护进程查询**一条建议（由 zsh widget 调用）

```deja query```

# SYNOPSIS

**deja** **import** [_options_]

**deja** **init** _zsh_

**deja** **ping**

**deja** **fuzzy** [_preset_|**cycle**|**back**]

**deja** **query** [_options_]

# PARAMETERS

**--file** _path_
> 当 **$HISTFILE** 未设置或未导出时，**import** 使用的历史文件路径（默认 **~/.zsh_history**）。

**DEJA_FUZZY**
> 在守护进程启动前覆盖会话的模糊匹配预设（**tight**、**smart**、**loose**）。

**DEJA_ACCEPT_KEY**, **DEJA_CYCLE_KEY**, **DEJA_TOGGLE_KEY**, **DEJA_DISMISS_KEY**
> 重新映射按键序列（需在 **eval "$(deja init zsh)"** 之前导出）。

# DESCRIPTION

**deja** 是 **zsh-autosuggestions** 的本地优先替代品。一个后台 Go 守护进程通过模糊匹配、目录亲和性、frecency 衰减和序列预测对命令历史打分，然后通过 Unix 套接字在不到一毫秒内返回行内幽灵文本建议。

运行 **deja import** 之后，将 **eval "$(deja init zsh)"** 加入 **~/.zshrc**。初始化脚本会在首次使用时拉起守护进程并绑定 ZLE widget：**→** 接受完整建议，**Tab** 在排名靠前的候选项之间循环，**Ctrl+X** 在当前会话内屏蔽建议，**Shift+→** / **Shift+←** 循环切换模糊匹配预设（**tight**、**smart**、**loose**）。

状态保存在 **~/.local/share/deja/deja.db**（SQLite WAL）。任何数据都不会同步到云服务。如果 **zsh-autosuggestions** 已经加载，deja 会检测到它并自动退避，避免产生冲突的 ZLE 包装器。

# CONFIGURATION

数据目录：**~/.local/share/deja/**（包含 **deja.db**、**sock** 和生成的 **init.zsh**）。模糊匹配预设可通过 **deja fuzzy** _preset_ 在重启后保持。Oh My Zsh 用户可以直接从上游仓库安装 **deja** 插件，而不必手动编辑 **~/.zshrc**，但不要同时启用插件和重复添加 **eval "$(deja init zsh)"** 一行。

# CAVEATS

仅支持 zsh。需要守护进程可达（**deja ping** → **pong**）。崩溃之后，删除残留的 **~/.local/share/deja/sock** 并打开新的 shell。不要与 **zsh-autosuggestions** 同时运行。

# INSTALL

```nix: nix profile install nixpkgs#deja```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[zsh](/man/zsh)(1), [history](/man/history)(1)
