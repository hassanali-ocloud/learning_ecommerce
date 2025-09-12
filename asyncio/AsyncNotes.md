# 1. Diff:
- Async: for managing many waiting tasks
- Processes: For maximizing performance on cpu intensive tasks
- Threads: For parallel tasks that share data with minimal cpu usuage.

# 2. Event Loop:
- When tasks awaits it allows other one to come and start processing.

# 3. Coroutine:
- Without await, it return coroutine object.
- Without await, coroutine is just created but is not executed. It executed when await is called.

# 4. Tasks:
- Let us schedule multiple coroutines to run.
- asyncio.create_task(<coroutine object>)

# 5. Gather:
- Quick way to concurrently run multiple coroutines.
- asyncio.gather(<Couroutine><Couroutine><Couroutine>)
- Wait for all of them to finish.

# 6. TaskGroup:
- This provides built-in error handling.
- asyncio.TaskGroup() & tg.create_task

# 7. Future:
- Made in lower level libraries.
- It is just like TaskCompletionSource

# 8. Synchronization:
- Within this lock, first finish all instruction even their is await
- lock = asyncio.Lock()

# 9. Symaphore:
- semaphore = asyncio.Semaphore(2)

# 10. Event:
- Deals with only bool  

## 11. Event Loop:
- Stack -> WebApis -> MicroTask Queue, Task/Callbacks Queue, Render Queue -> Event Loop -> Stack
- Event Loop Job: Look at stack and look at task queue, if stack is empty it will take first thing in queue and pushed on stack
- WebApis (XHR) -> Job is to run ajax requests, when its done only then it is move to queue.
-> User Click Input also waits in WebApis section
- Render Queue: It first wait for the call stack to get empty and then send its instr there.
-> Render happens when tasks/callback queues are done.
-> If 60fps then render is going to send to queue after every 60 millisecond so that it execute cmd.
-> Mircotask contains the promises callbacks.
-> Microtask > Task/Callback Queue > Render Queue or when browser decides to render

- Sequence:
Event loop tick starts.
One task (callback) is dequeued from the callback queue and executed.
Flush microtasks (if any were scheduled during that task).
Browser checks: “Is it time to paint?”
If yes, it processes the render queue (runs requestAnimationFrame callbacks, updates DOM, paints).
If no, it skips rendering and continues with the next callback.
Next event loop tick → repeat.