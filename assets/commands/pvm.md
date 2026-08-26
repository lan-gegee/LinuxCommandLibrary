# TAGLINE

并行虚拟机（PVM）控制台

# TLDR

**启动 PVM 控制台**，必要时启动守护进程

```pvm```

**启动控制台并从主机文件添加主机**

```pvm [path/to/hostfile]```

**显示当前虚拟机**配置

```pvm> conf```

以交互方式向虚拟机中**添加主机**

```pvm> add [hostname]```

从虚拟机中**移除主机**

```pvm> delete [hostname]```

在虚拟机上**派生任务**

```pvm> spawn -[count] [a.out]```

**列出所有正在运行的 PVM 任务**

```pvm> ps -a```

**关闭所有 PVM 守护进程**

```pvm> halt```

# SYNOPSIS

**pvm** [_hostfile_]

# DESCRIPTION

**pvm** 是 **Parallel Virtual Machine (PVM)** 系统的交互式控制台。它本身就是一个 PVM 任务，让用户可以启动、查询和修改一个分布式虚拟机，该虚拟机由通过网络连接的异构 Unix（及 Windows）主机构成。

启动 **pvm** 时会联系本地主机上已在运行的 **pvmd3** 守护进程，若没有则在运行中启动一个。传入 _hostfile_ 还会在启动时把所列出的机器加入虚拟机。连接建立后，控制台会显示 **pvm>** 提示符，并接受交互式命令来管理主机、任务和 PVM 环境。

PVM 将网络中的多台工作站组成一台逻辑上的并行计算机，使消息传递型并行程序能够跨这些机器运行。控制台本身并不运行并行代码；它是管理前端。

# CONSOLE COMMANDS

**add** _hostname(s)_
> 向虚拟机添加一台或多台主机。

**alias**
> 定义或列出命令别名。

**conf**
> 列出当前虚拟机配置（主机、架构、ID）。

**delete** _hostname(s)_
> 从虚拟机中移除主机。

**echo** _args_
> 将参数回显到控制台。

**export** _VAR_
> 将环境变量加入 spawn 导出列表。

**halt**
> 停止所有 **pvmd** 守护进程并退出 PVM。

**help** [_command_]
> 打印某个控制台命令的帮助。

**id**
> 打印控制台任务的 ID。

**jobs**
> 列出正在运行的任务。

**kill** _task-tid_
> 按 PVM 任务 ID 终止任务。

**mstat** _host_
> 显示主机状态。

**pstat** _task-tid_
> 显示特定任务的状态。

**ps -a**
> 列出所有 PVM 任务。

**quit**
> 退出控制台（虚拟机继续运行）。

**reset**
> 杀死所有 PVM 任务。

**setenv**
> 显示或设置环境变量。

**sig** _signum_ _task_
> 向任务发送信号。

**spawn** [_options_] _a.out_
> 派生一个任务。选项：**-**_count_（副本数量）、**-**_host_（目标主机）、**-**_ARCH_（架构）。

**unalias** _name_
> 移除别名。

**version**
> 打印 PVM 版本。

# HOST FILE

主机文件是以换行分隔的机器名列表，可选地附带每台主机的选项（登录名、工作目录、架构）。示例：

```
# one host per line; options use key=value
node1
node2 lo=alice
node3 ep=/opt/pvm3/bin/LINUX
```

# ENVIRONMENT

**PVM_ROOT**
> PVM 安装的根目录（如 _/usr/lib/pvm3_）。

**PVM_ARCH**
> 用于定位可执行文件的架构名称（如 _LINUX64_、_SUN4SOL2_）。

**PVM_TMP**
> 存放 PVM 临时文件的目录（默认为 _/tmp_）。

# FILES

**$HOME/.pvmrc**
> 控制台启动时执行的命令。

**/tmp/pvmd.\<uid\>**
> 用于联系本地 **pvmd** 守护进程的套接字。

**/tmp/pvml.\<uid\>**
> 每个用户的 PVM 日志文件。

# CAVEATS

PVM 是**遗留**软件：活跃开发于 2000 年代中期停止，在严肃的并行计算领域实际上已被 **MPI** 实现（**Open MPI**、**MPICH**）取代。它对教学场景以及维护旧的科学代码库仍有价值。PVM 默认的网络通信未经身份验证也未加密，因此只能在可信网络内使用。

# HISTORY

**PVM** 自 **1989** 年起由 **Al Geist**、**Adam Beguelin**、**Jack Dongarra**、**Robert Manchek**、**Weicheng Jiang** 和 **Vaidy Sunderam** 在 **Oak Ridge National Laboratory**、**University of Tennessee** 和 **Emory University** 开发。在 MPI 标准兴起之前，它是整个 1990 年代异构分布式计算的事实标准。PVM 版本 3 是打包最广泛的发行版。

# INSTALL

```aur: yay -S pvm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mpirun](/man/mpirun)(1)
