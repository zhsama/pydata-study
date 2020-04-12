-- 查询
	-- 查询所有字段
	-- select * from 表名;
	select * from students;

	-- 查询指定字段
	-- select 列1,列2,... from 表名;
	select name, height from students;

	-- 使用 as 给字段起别名
	-- select 字段 as 名字.... from 表名;
	select height 身高, name 姓名 from students;
	select height as 身高, name as 姓名 from students;

	-- sql语句完全的形式
	select name, height from students;
	select students.name, students.height from students;
	select python_test_1.students.name, python_test_1.students.height from students;
	-- 多表查询的时候就需要将表名带上
	-- select 表名.字段 .... from 表名;


	-- 可以通过 as 给表起别名
	-- select 别名.字段 .... from 表名 as 别名;
	-- 在当前的sql 语句中 临时的给students 起了一个别名叫做s
	select students.name, students.height from students;
	select s.name, s.height from students as s;

	-- 消除重复行
	-- distinct 字段, 修饰所有需要查询的字段
	-- 查询班级学生的性别
	select gender from students;

	-- 查询班级有多少种性别
	select distinct gender from students;

	-- 如果distinct后有多个字段, 只有当查询的多列的查询结果完全相同才能去重
	select distinct height,gender from students;

-- 条件查询 where
	-- 比较运算符
		-- >
		-- 查询大于18岁的信息
		select * from students where age > 18;

		-- <
		-- 查询小于18岁的信息

		-- >= 和 <=

		-- != 或者 <>  实际开发中 最好使用 ! 表示不等于
		select * from students where age != 18;
		select * from students where age <> 18;


	-- 逻辑运算符 与(and) 或(or) 非(not)
		-- and 必须同时满足所有的条件
		-- 18岁以上的女性
		select * from students where age > 18 and gender = '女';
		select * from students where age > 18 and gender = '女' and height > 167;

		-- or 只需要满足其中一个条件即可
		-- 18岁以上或者身高超过180(包含)以上
		select * from students where age > 18 or height > 180;

		-- not  非
		-- 年龄不是18岁的学生
		select * from students where age != 18;
		select * from students where age <> 18;
		select * from students where not age = 18;

	-- 模糊查询
		-- like
		-- % 表示任意字符可有可无
		-- 查询姓名中 以 "小" 开始的名字
		select * from students where name like '小%';
		-- 名字中包含杰 的名字
		select * from students where name like '%杰%';
		-- _ 表示任意一个字符
		-- 查询有2个字的名字
		select * from students where name like "__";
		-- 查询有3个字的名字
		select * from students where name like "___";

		-- sql中可以使用正则表达式完成查询 rlike
		select * from students where name rlike "^周";


	-- 范围查询
		-- in 表示在一个非连续的范围内
		-- 查询 年龄为18、34, 45,50岁的学生
		select * from students where age = 18 or age = 34 or age = 45;
		select * from students where age in (18, 34, 45, 50);

		-- not in 不在非连续的范围之内
		-- 年龄不是 18、34岁的学生的信息
		select * from students where age not in (18, 34);

		-- 18 ~ 34
		select * from students where age > 18 and age < 34;

		-- between ... and ...表示在一个连续的范围内  两边都会包含
		-- 查询 年龄在18到34之间的的信息
		select * from students where age between 18 and 34;

		-- not between ... and ...表示不在一个连续的范围内
		-- 查询 年龄不在在18到34之间的的信息
		select * from students where age not between 18 and 34;
		select * from students where not age between 18 and 34;

	-- 空判断 null  不能够使用比较运算符
		-- 查询身高为空的信息
		select * from students where height = null; # 错误
		select * from students where height is null; # 正确

		-- 查询身高不为空的学生
		select * from students where height is not null;
		select * from students where height not is null; # 错误
		select * from students where not height is null;


-- 排序 从大到小--> 降序排序 从小到大-->升序排序
	-- order by 字段  默认就是升序排序 asc 可以省略
	-- asc从小到大排列，即升序
	-- 查询年龄在18到34岁之间的男性，按照年龄从小到大排序
	select * from students where age between 18 and 34 and gender = 1 order by age asc;

	-- 降序 desc
	-- desc从大到小排序，即降序
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序
	select * from students where age between 18 and 34 and gender = 2 order by height desc;
	select * from students order by height desc where age between 18 and 34 and gender = 2; # 错误

	-- order by 多个字段 order by age asc, height desc
	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序
	select * from students where age between 18 and 34 and gender = 2 order by height desc, age asc;

	-- 查询年龄在18到34岁之间的女性，身高从高到矮排序, 如果身高相同的情况下按照年龄从小到大排序, 如果年龄也相同那么按照id从大到小排序
	select * from students where age between 18 and 34 and gender = 2 order by height desc, age asc, id desc;
	-- 按照年龄从小到大、身高从高到矮的排序
	select * from students order by age asc, height desc; -- asc 可以省略, 但是不建议省略

-- 聚合函数 做统计
	-- 总数: count()
	-- count(*) 以行单位来进行统计个数 按行统计
	-- count(*) 效率更高, 效率略差:count(height)--> 获取对应的行--> 获取该行对应字段是否为NULL
	-- 查询班级有多少人
	select count(*) from students;
	select count(id) from students;

	-- 查询男性有多少人，女性有多少人 (通过一个sql语句完成这个需求 需要掌握分组操作才行)
	select count(*) from students where gender = 1;
	select count(*) from students where gender = 2;


	-- 最大值: max()
		-- 查询最大的年龄
		select max(age) from students;

		-- 查询女性的最高身高
		select max(height) from students where gender = 2;

		-- 查询最高身高的学生的名字
		-- select name 14个结果
		-- select max(height) 1
		select name, max(height) from students; -- 不行
		-- select 语句的嵌套  --> 子查询
		-- 假设最高身高就是185
		select name from students where height = 185;
		select name from students where height = (select max(height) from students); -- ()提高sql语句执行的优先级


	-- 最小值: min()

	-- 求和: sum()
		-- 计算所有人的年龄总和
		select sum(age) from students;


	-- 平均值: avg()
		-- 计算平均年龄
		select avg(age) from students;

		-- 计算平均身高


	-- 四舍五入 round(123.23 , 1) 保留1位小数, 四舍五入
	-- 计算所有人的平均年龄，保留2位小数
	select avg(age) from students;
	select round(avg(age),2) from students;



	-- 计算男性的平均身高 保留2位小数
	now()
	verison()
	database()

-- SQL 中的内置函数帮助文档的查看
	? functions; 查看有哪些类型的函数

	ex:
		? round;


-- 分组 ,分组的目的就是为了进行聚合统计 通过某个字段进行分组(分) 然后做聚合统计(合)
	-- group by 字段
	-- 查询班级学生的性别
	select gender from students;

	-- 查看有哪几种性别
	select distinct gender from students;

	-- 按照性别分组
	select gender from students group by gender;

	-- 计算每种性别中的人数, 聚合统计函数只会作用在分组之后的数据上, 不会作用在源数据上
	select gender, count(*) from students group by gender;

	-- group_concat(...)
	-- 查询每个性别分组数据中的人的姓名
	select gender, name from students group by gender; 错误
	select gender,group_concat(name) from students group by gender;
	select gender,group_concat(name) as infos, count(*) from students group by gender;


	男 周杰伦
	男 彭于晏
	男 张学友
	...
	女 静香
	女 周杰

	男: 周杰伦, 彭于晏, 张学友
	女: 静香, 周杰


	-- 查询同种性别中的姓名和身高
	-- 计算男性的人数
	select count(*) from students where gender = 1;
	-- 通过分组来实现
	select gender, count(*) from students group by gender;

	+--------+----------+
	| gender | count(*) |
	+--------+----------+
	| 男     |        5 |
	| 女     |        7 |
	| 中性   |        1 |
	| 保密   |        1 |
	+--------+----------+
	需要在分组之后的数据中做进一步的筛选操作
	-- 使用having 条件筛选 表示对于已经分组的数据做进一步的筛选
	-- 对分组之后的数据做进一步的筛选操作, 只能够是用having 做筛选 不能够使用where
	select gender, count(*) from students group by gender having gender = 1;
	select gender, count(*) from students group by gender where gender = 1; 错误

	-- 除了男生以外的分组的人数
	select gender, count(*) from students group by gender having gender != 1;
	select gender, count(*) from students group by gender having not gender = 1;

	-- having  对于分组之后的数据 做进一步的筛选
	-- 查询每种性别中的平均年龄avg(age)
	select gender, avg(age) from students group by gender;

	-- 查询每种性别中的平均年龄avg(age), 最大年龄,平均身高,最高身高, 分组是为了更好的统计
	select gender, avg(age),max(age), avg(height), max(height) from students group by gender;

	-- 查询平均年龄超过30岁的性别，以及姓名, 对分组之后的数据做进一步筛选操作 having
	select gender, group_concat(name),avg(age) from students group by gender having avg(age) > 30;


	-- having 和 where 的区别
	having 表示对于已经分组的数据做进一步的筛选, 有having就一定有group by, 有group by 不一定有 having
	where 是对源数据做筛选操作

	select gender, substring_index(group_concat(height order by height desc),',', 2) from students group by gender;


-- 分页
	-- limit start, count
	-- start: 表示从哪里开始查询, start 默认值为0, 可以省略, start跳过多少条数据
	-- count: 查询多少条

	获取第一页, 每页显示4条数据
	select * from students limit 0,4;

	第1页

	第2页

	第3页

	第4页


	-- 每页显示4个，显示第3页的信息, 按照年龄从小到大排序
	select name from student limit 8,4 order by age;
	select name from student order by age limit 8,4;


-- 连接查询  将两个表按照某种条件合并到一起

	-- 查询学生的名字和学生对应的班级名字
	-- 学生名字在学生表, 班级名字在班级表
	select students.name,classes.name from students,classes; -- 笛卡尔积查询 有可能产生庞大的中间表
	select * from students,classes;
	-- 笛卡尔积查询, 会产生很多无用的信息


	-- 连接查询 将两个表中的数据按照设置的连接条件进行筛选, 符合连接条件的数据才能够被筛选出来
	-- table1 inner join table2 on 条件   ,  设置内连接条件 内连接查询
	select students.name, classes.name from students inner join classes on students.cls_id = classes.id;
	select s.name,c.name from students as s inner join classes as c on s.cls_id = c.id;
	select s.*,c.* from students as s inner join classes as c on s.cls_id = c.id;

	-- 按照要求显示姓名、和学生对应的班级的名字(学生所在的班级)
	select s.name,c.name from students as s inner join classes as c on s.cls_id = c.id;
	-- 在以上的查询中，将班级名字显示在第1列
	select c.name,s.name from students as s inner join classes as c on s.cls_id = c.id;
	-- 查询 学生所在的班级, 按照班级进行排序
	select c.name,s.name from students as s inner join classes as c on s.cls_id = c.id order by c.name;


	-- 外连接查询: left join + right join
	-- left join 左外连接查询
	-- 查询每位学生对应的班级信息, 不满足连接条件的数据会以NULL填充
	select s.*,c.* from students as s left join classes as c on s.cls_id = c.id;

	-- right join 右外连接查询  使用的比较少
	-- 将数据表名字互换位置，用left join完成

	-- 扩充了解, 内连接和外连接的其他写法
	-- 内连接的其他写法
	select s.*,c.* from students as s inner join classes as c on s.cls_id = c.id;
	select s.*,c.* from students as s join classes as c on s.cls_id = c.id;
	select s.*,c.* from students as s cross join classes as c on s.cls_id = c.id;

	-- 外连接的其他写法
	select s.*,c.* from students as s left outer join classes as c on s.cls_id = c.id;
	select s.*,c.* from students as s right outer join classes as c on s.cls_id = c.id;




-- 自关联  自己关联自己 a inner join a




-- 通过 source 指令导入一个sql文件
	-- 省级联动 url:http://demo.lanrenzhijia.com/2014/city0605/
	-- 查询所有省份


	-- 查询出广东省有哪些市
	广东省 广州市
	广东省 深圳市
	...
	select p.atitle,c.atitle from areas as p inner join areas as c on c.pid = p.aid where p.atitle = '广东省';
	--  需要有想象力, 将areas 想象成两张表 , 一张是省表, 一张是市表\

	-- 查询出广州市有哪些区县
	select p.atitle,s.atitle from areas as p inner join areas as s on s.pid = p.aid where p.atitle = '广州市';



-- 子查询
-- 查询班级最高身高的学生的名字
select name from students where height = 185;
select name from students where height = (select max(height) from students);


子查询语句按照查询的结果可以分为四种类型的子查询
-- 标量子查询: 子查询语句查询的结果是一行一列(就是一个最基本的结果)
select name from students where height = (select max(height) from students);

-- 列级子查询 子查询语句查询的结果是一列多行(就是一个最基本的结果)
select * from students where age in (18, 20, 30);
select * from students where age in (select age from students where age in (18, 20, 30))
select classes.name from classes where id in (select cls_id from students);
select classes.name from classes where id = (select cls_id from students); # 错误
select classes.name from classes where id = any(select cls_id from students); # 正确

-- 行级子查询
-- 实现行子子查询, 需要构建行元素
-- 查找班级年龄最大,身高最高的学生
select * from students where (age, height) = (select max(age), max(height) from students);

-- 表级子查询 查询的结果是多行多列, 充当的是数据源
select * from students;
select * from (select * from students) tmp;
select * from (select * from students) as tmp;
select tmp.* from (select students.* from students) as tmp;



# 终端备份
-- 需要退出mysql连接再执行mysqldump命令
mysqldump -uroot -p python_test_1 > python_res.sql

-- 恢复数据之前先创建数据表
mysql -uroot -p yyyy < python_res.sql

扩展阅读: https://blog.csdn.net/helloxiaozhe/article/details/77680255
