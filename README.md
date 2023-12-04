# todo_list

## 使用说明

- 本项目旨在设计一个命令行交互版本的todo list，对于程序员来说更加友好，也可以定义更多的操作

//to be filled later

## 支持功能及使用方法

1. 像传统todo list一样，可以插入任务，并且可以标记完成，或者删除任务

   - 插入任务：todo insert {**$task**} --{**total,today,1,2,...,n**}

     - {$task}是任务名称
     - {total,today,1,2,...,n}表示想要插入的时间点，total是加入总任务，today是加入今天的任务，1-n表示加入从今天向后第k天的任务

     - 例如： todo insert 复习编译原理 --today

   - 删除任务：todo delete {**$task_id**} 

2. 