# mapreduce_python
Python code and execution for map reduce

First run your program locallty for testing:
Give all executable access to all python files.
** Test Mapper code
(base) Binods-MacBook-Pro:binod_python_mapreduce binod$ cat names.txt | ./mapper.py
Binod	1
Suman	1
Pramod	1
Modi	1
Binod	1
Ishan	1
Suman	1
Mukesh	1
Ambani	1
Mukesh	1
Binod	1
Ambani	1
Ishan	1
Ambani	1
Binod	1

** Test Mapper and Reducer code

(base) Binods-MacBook-Pro:binod_python_mapreduce binod$ cat names.txt | ./mapper.py | ./reducer.py 
Binod	4
Suman	2
Pramod	1
Modi	1
Ishan	2
Mukesh	2
Ambani	3

Now move names file to HDFS to /binod_python/input folder
and execute below command to run these map reduce code on Hadoop environment

[raj_ops@sandbox MapReduce]$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /binod_python/input  -output /binod_python/output2
You may get this below output at end of above command execution:
		Bytes Written=58
20/04/07 18:27:47 INFO streaming.StreamJob: Output directory: /binod_python/output2


Now check your output file:
[raj_ops@sandbox MapReduce]$ hadoop fs -cat /binod_python/output2/part-00000
Ambani	3
Mukesh	2
Suman	2
Binod	4
Pramod	1
Ishan	2
Modi	1




