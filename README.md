# MapReduce-Practice-for-Udacity-Hadoop-Course

My MapReduce practices for the Udacity Course: https://www.udacity.com/course/intro-to-hadoop-and-mapreduce--ud617

Sample data is in the 'data' directory. Full data can be found on the course website.

Summay of each project:

1. post_answer_length:

      id of the question | length of the question | average length of the answers to teh question

2. student_times:

      author id | Hour of the day that the author posts most frequently
      
3. study_groups:

      id of the question | a list ids of students that have involved in the question (asked, answered, commented)
      
4. top_tags:
      outputs top 10 popular tags
      
      tag name | number of posts that use this tag
      


Notes:

1. HDFS commands:
   $ hadoop fs -ls <directory>
   $ hadoop fs -put <local directory> <HDFS directory>
   $ hadoop fs -mv <old file> <new file>
   $ hadoop fs -rm <file>

2. Run MapReduce:
   $ hadoop jar <path to jar> -mapper mapper.py -file -reducer reducer.py -file input <input dir> -output <output dir>
   
3. Test map reduce on local machine:
   $ cat <test data> | ./mapper.py | sort | ./reducer.py
