# 打印

## 入门
Linux 上的打印通过 **CUPS** 完成，它提供两套命令家族：System V 风格（**lp**、**lpstat**、**cancel**）和 BSD 风格（**lpr**、**lpq**、**lprm**）。两者对接的是同一个打印系统，任选一套即可。CUPS 还提供网页界面，地址为 http://localhost:631。

## 列出打印机
显示可用打印机、默认打印机以及完整状态。
```[lpstat](/man/lpstat) -p -d```
```[lpstat](/man/lpstat) -t```

设置默认打印机。
```[lpoptions](/man/lpoptions) -d [printerName]```

## 打印文件
打印到默认打印机，或显式指定一台：**lp** 使用 **-d**（目标），**lpr** 使用 **-P**。
```[lp](/man/lp) [file]```
```[lp](/man/lp) -d [printerName] [file]```
```[lpr](/man/lpr) [file]```
```[lpr](/man/lpr) -P [printerName] [file]```

任何内容都可以通过管道送往打印机，**pr** 能先把纯文本整齐地分页。
```[echo](/man/echo) "Hello" | [lp](/man/lp)```
```[pr](/man/pr) -l60 [file] | [lpr](/man/lpr)```

## 打印选项
**-n** 设置打印份数；**-o** 传递打印机选项。
```[lp](/man/lp) -n 3 [file]```
```[lp](/man/lp) -o sides=two-sided-long-edge [file]```
```[lp](/man/lp) -o page-ranges=1-4,7 [file]```
```[lp](/man/lp) -o landscape -o fit-to-page [image.png]```

| 选项 | 说明 |
|-----|-------------|
| **sides=two-sided-long-edge** | 双面打印（长边装订） |
| **page-ranges=1-4,7** | 只打印这些页 |
| **number-up=2** | 每张纸打印多页 |
| **landscape** | 将输出旋转 90 度 |
| **fit-to-page** | 缩放以适应纸张 |

## 查看打印队列
```[lpq](/man/lpq)```
```[lpstat](/man/lpstat) -o```

## 取消打印任务
按 ID 取消特定任务（ID 由 **lpq** 或 **lpstat -o** 显示）、取消你最近的任务，或取消全部任务。
```[cancel](/man/cancel) [jobID]```
```[cancel](/man/cancel) -a [printerName]```
```[lprm](/man/lprm) [jobID]```
```[lprm](/man/lprm) -```

**lprm -** 会删除你自己的全部任务。取消其他用户的任务需要 root 权限。

## 管理打印机
停止和恢复打印机的输出，例如在清除卡纸时不丢失队列中的任务。
```[cupsdisable](/man/cupsdisable) [printerName]```
```[cupsenable](/man/cupsenable) [printerName]```

使用 CUPS 管理工具添加打印机，或列出可用的驱动与连接（需要 root）。
```[lpinfo](/man/lpinfo) -v```
```[lpadmin](/man/lpadmin) -p [printerName] -E -v ipp://[host]/ipp/print -m everywhere```

大多数现代网络打印机支持无驱动打印（IPP Everywhere），**-m everywhere** 设置的正是这种方式。
