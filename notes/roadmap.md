# roadmap

- chapter 1：CPU-work vs IO-work 的区分，以及 asyncio 单线程并发模型是如何工作的。
- chapter 2： asyncio coroutines 的基础，以及 async/await 语法的使用。
- chapter 3：非阻塞 socket 和 selectors 的工作原理。以及使用 asyncio 构建一个 echo server。
- chapter 4： 多个 web 并发请求。掌握 core asyncio APIs。
- chapter 5： 使用连接池实现数据库的并发查询请求。异步上下文管理器和异步生成器。
- chapter 6：多进程模型。map-reduce 例子。
- chapter 7： 专注于多线程，特别是如何将它与 asyncio 一起使用处理阻塞 I/O。
- chapter 8： 关注网络流和协议。创建一个聊天服务器和客户端，用于处理并发多人聊天。
- chapter 9： 关注异步驱动的 web 应用和 ASGI (asynchronous server gateway interface)。
- chapter 10： 描述了如何使用基于 asyncio 的 Web API 来构建一个假设的微服务架构。
- chapter 11： 关注单线程并发同步和如何解决它们。我们深入研究锁、信号量、事件和条件。
- chapter 12： 专注于异步队列。我们将使用这些来构建一个 Web 应用进程，即刻响应客户请求，尽管在后台工作做一些耗时的事情。
- chapter 13： 重点介绍如何创建和管理子流程，向您展示如何读取和写入数据。
- chapter 14： 重点介绍高级主题，例如强制事件循环迭代、上下文变量和创建自己的事件循环。

## 感悟
- chapter 1-4 是 asyncio 的基础使用。
- chapter 8,9 部分code运行失败，原因未知。
- chapter 14 难度很大，不过非常有价值，应该花精力去理解感悟。