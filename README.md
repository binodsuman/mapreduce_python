# mapreduce_python
Python code and execution for map reduce

First run your program locallty for testing: <br />
Give all executable access to all python files.<br />
** Test Mapper code<br />
(base) Binods-MacBook-Pro:binod_python_mapreduce binod$ cat names.txt | ./mapper.py<br />
Binod	1<br />
Suman	1<br />
Pramod	1<br />
Modi	1<br />
Binod	1<br />
Ishan	1<br />
Suman	1<br />
Mukesh	1<br />
Ambani	1<br />
Mukesh	1<br />
Binod	1<br />
Ambani	1<br />
Ishan	1<br />
Ambani	1<br />
Binod	1<br />
<br />
** Test Mapper and Reducer code<br />
<br />
(base) Binods-MacBook-Pro:binod_python_mapreduce binod$ cat names.txt | ./mapper.py | ./reducer.py <br />
Binod	4<br />
Suman	2<br />
Pramod	1<br />
Modi	1<br />
Ishan	2<br />
Mukesh	2<br />
Ambani	3<br />
<br />
Now move names file to HDFS to /binod_python/input folder<br />
and execute below command to run these map reduce code on Hadoop environment<br />
<br />
[raj_ops@sandbox MapReduce]$ hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /binod_python/input  -output /binod_python/output2<br />
<br />You may get this below output at end of above command execution:<br />
Bytes Written=58<br />
20/04/07 18:27:47 INFO streaming.StreamJob: Output directory: /binod_python/output2<br />
<br />
<br />
Now check your output file<br />
[raj_ops@sandbox MapReduce]$ hadoop fs -cat /binod_python/output2/part-00000<br />
Ambani	3<br />
Mukesh	2<br />
Suman	2<br />
Binod	4<br />
Pramod	1<br />
Ishan	2<br />
Modi	1<br />
<br />



