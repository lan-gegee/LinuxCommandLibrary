# Tmux

## 入门
Tmux 是一款终端复用器：它在单个窗口内运行多个终端会话，并在你断开连接后让它们继续保持活跃。它分为三层结构：**会话** 包含 **窗口**，窗口又包含 **面板**。
```[tmux](/man/tmux)```
```[tmux](/man/tmux) new -s mysession```

所有快捷键都以 **前缀键** 开头，默认为 **Ctrl+b**。先按下前缀键，松开后再按命令键。

## 会话
会话是一组窗口的集合，在你分离会话或连接中断后，它仍在后台继续运行。之后重新接入，就能从上次离开的位置原样继续。

| 按键 | 说明 |
|-----|-------------|
| **Ctrl+b d** | 分离当前会话 |
| **Ctrl+b s** | 列出所有会话并切换 |
| **Ctrl+b $** | 重命名当前会话 |
| **Ctrl+b (** | 切换到上一个会话 |
| **Ctrl+b )** | 切换到下一个会话 |

```[tmux](/man/tmux) ls```
```[tmux](/man/tmux) attach -t mysession```
```[tmux](/man/tmux) new -d -s mysession```
```[tmux](/man/tmux) rename-session -t old new```
```[tmux](/man/tmux) kill-session -t mysession```
```[tmux](/man/tmux) kill-server```

不带 **-t** 时，**tmux attach** 会接入最近使用的会话。**kill-server** 会彻底停止 tmux，包括其中所有会话。

## 窗口
窗口类似于会话中的标签页。每个窗口都运行自己的 Shell，并带有编号，默认从 0 开始。

| 按键 | 说明 |
|-----|-------------|
| **Ctrl+b c** | 创建新窗口 |
| **Ctrl+b n** | 切换到下一个窗口 |
| **Ctrl+b p** | 切换到上一个窗口 |
| **Ctrl+b 0-9** | 按编号切换到指定窗口 |
| **Ctrl+b l** | 切换到最近活动的窗口 |
| **Ctrl+b w** | 列出所有窗口并选择其一 |
| **Ctrl+b ,** | 重命名当前窗口 |
| **Ctrl+b .** | 将当前窗口移到其他编号 |
| **Ctrl+b &** | 关闭当前窗口（需确认） |

## 面板
面板把窗口分割成多个终端区域。每个面板都运行着各自独立的 Shell。

| 按键 | 说明 |
|-----|-------------|
| **Ctrl+b %** | 左右分割面板 |
| **Ctrl+b "** | 上下分割面板 |
| **Ctrl+b Arrow** | 移动到该方向的面板 |
| **Ctrl+b o** | 循环切换到下一个面板 |
| **Ctrl+b ;** | 跳转到最近活动的面板 |
| **Ctrl+b z** | 切换当前面板的缩放（占满整个窗口） |
| **Ctrl+b x** | 关闭当前面板（需确认） |
| **Ctrl+b {** | 将当前面板与上一个面板交换 |
| **Ctrl+b }** | 将当前面板与下一个面板交换 |
| **Ctrl+b Space** | 循环切换面板布局 |
| **Ctrl+b q** | 显示面板编号（按对应数字即可跳转） |
| **Ctrl+b !** | 把当前面板拆分为一个新窗口 |

## 调整面板大小
先按前缀键，再按修饰键加方向键。按住修饰键不放就能连续调整大小，无需再按一次前缀键。

| 按键 | 说明 |
|-----|-------------|
| **Ctrl+b Ctrl+Arrow** | 沿该方向将面板调整 1 个单元格 |
| **Ctrl+b Alt+Arrow** | 沿该方向将面板调整 5 个单元格 |

在命令提示符下同样可行，**-D**、**-U**、**-L**、**-R** 分别对应向下、向上、向左、向右。
```[tmux](/man/tmux) resize-pane -D 10```
```[tmux](/man/tmux) resize-pane -R 10```

## 复制模式
复制模式让你滚动查看输出、搜索内容并复制文本。按 **Ctrl+b [** 进入复制模式（或按 **Ctrl+b PgUp** 进入并向上翻一页）。

默认情况下，tmux 在复制模式中使用 Emacs 风格按键。多数用户会改成 vi 风格按键，下面的表格就基于这一设置。
```[echo](/man/echo) "setw -g mode-keys vi" >> ~/.tmux.conf```

| 按键 | 说明 |
|-----|-------------|
| **q** | 退出复制模式 |
| **h j k l** | 向左、下、上、右移动 |
| **w / b** | 向前/向后移动一个单词 |
| **g / G** | 跳转到历史的顶部/底部 |
| **Ctrl+u / Ctrl+d** | 向上/向下滚动半页 |
| **/** | 向前搜索 |
| **?** | 向后搜索 |
| **n / N** | 下一个/上一个搜索匹配项 |
| **Space** | 开始选择文本 |
| **Enter** | 复制所选内容并退出复制模式 |

在复制模式之外，粘贴最近一次复制的内容。

| 按键 | 说明 |
|-----|-------------|
| **Ctrl+b ]** | 粘贴已复制的内容 |

## 命令模式
按 **Ctrl+b :** 打开 tmux 命令提示符。每个快捷键都是某条命令的捷径，这些命令都可以在这里直接执行。
```new-window -n mywin```
```split-window -h```
```swap-window -t 0```
```select-layout even-horizontal```
```setw synchronize-panes on```

**synchronize-panes** 会把你输入的内容同时发送到窗口中的所有面板。便于在多台服务器上运行同一条命令。用 **setw synchronize-panes off** 关闭。

## 配置
Tmux 在服务器启动时读取 **~/.tmux.conf**。下面是一些实用的选项：
```set -g mouse on```
```set -g history-limit 50000```
```set -g base-index 1```
```setw -g pane-base-index 1```

**mouse on** 启用点击面板、拖动边框调整大小和滚轮滚动。**base-index 1** 让窗口从 1 开始编号而不是 0，与键盘布局一致。

无需重启即可让更改在正在运行的服务器上生效。
```[tmux](/man/tmux) source-file ~/.tmux.conf```
