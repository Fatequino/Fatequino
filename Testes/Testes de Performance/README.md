<!--lint ignore double-link-->
A curated collection of resources covering [Apache JMeter](https://jmeter.apache.org/) and related.

<!--lint ignore double-link-->
[<img src="https://github.com/aliesbelik/awesome-jmeter/raw/main/assets/images/jmeter-logo.svg" align="right" width="260" alt="Apache JMeter">](https://jmeter.apache.org/)

<!--lint ignore double-link-->
> [Apache JMeter](https://jmeter.apache.org/) is open source, pure Java application designed to load test functional behavior and measure performance.

## Contents

<!--lint ignore double-link-->
- [Official Resources](#official-resources)
- [Distributions](#distributions)
- [Getting Started](#getting-started)
- [Best Practices](#best-practices)
- [Distributed Testing](#distributed-testing)
- [Results Processing](#results-processing)
  - [Results Analysis](#results-analysis)
- [Performance Testing](#performance-testing)
  - [RESTful API](#restful-api)
- [Tools](#tools)
  - [Plugins](#plugins)
  - [Extending JMeter](#extending-jmeter)
  - [IDE Integration](#ide-integration)
- [JMeter Performance](#jmeter-performance)
- [Trainings & Courses](#trainings--courses)
- [Videos](#videos)


## Official Resources

<!--lint ignore double-link-->
- [Apache JMeter Project](https://jmeter.apache.org/) - Apache JMeter official website.
- [GitHub Repository](https://github.com/apache/jmeter) - Apache JMeter source code repository.
- [JMeter Wiki](https://cwiki.apache.org/confluence/display/jmeter) - Apache JMeter official documentation.

## Distributions

- [Download Apache JMeter](https://jmeter.apache.org/download_jmeter.cgi) - Apache JMeter: Official downloads.
- [JMeter for Windows](https://sourceforge.net/projects/jmeterforwindows/) - Package for installation JMeter with plugins.

## Getting Started

- [Getting Started with Apache JMeter](https://dzone.com/refcardz/getting-started-with-apache-jmeter)
- [A Simple Load Test with JMeter](https://www.urbaninsight.com/article/simple-load-test-with-jmeter)
- [The Beginner's Guide to Performance Testing with Apache JMeter](https://betterprogramming.pub/the-beginners-guide-to-performance-testing-with-apache-jmeter-5cc52c327ff6)

## Tutorials

- [JMeter Tutorial](https://artoftesting.com/jmeter-tutorial) - By ArtOfTesting.
- [Load Testing your Applications with Apache JMeter](http://www.jguru.com/article/server-side/load-testing-with-apache-jmeter.html) - By Keld H. Hansen.
- [Load Testing with JMeter](https://lincolnloop.com/blog/search/?q=jmeter) - By Brandon Konkle.
- [JMeter Resources](https://resources.infosecinstitute.com/?s=jmeter) - By Dejan Lukan.
- [JMeter Tutorial](https://www.tutorialspoint.com/jmeter/) - By Tutorials Point.
- [JMeter Tutorial for Load Testing: The Ultimate Guide](https://www.javacodegeeks.com/2014/11/jmeter-tutorial-load-testing.html) - By Daniel Gutierrez Diez.
- [JMeter: Load Development LifeCycle](https://datacadamia.com/jmeter/lifecycle) - By DataCadamia.
- [Load Testing with Apache JMeter](https://www.digitalocean.com/community/tutorial_series/load-testing-with-apache-jmeter) - By DigitalOcean.
- [JMeter Tutorial for Beginners](https://www.guru99.com/jmeter-tutorials.html) - By Guru99.

## Best Practices

- [JMeter Official Best Practices](https://jmeter.apache.org/usermanual/best-practices.html)
- [JMeter Best Practices](https://guide.blazemeter.com/hc/en-us/articles/207421405-JMeter-Best-Practices)
- [Optimize JMeter for Large Scale Tests](https://octoperf.com/blog/2017/10/12/optimize-jmeter-for-large-scale-tests/)
- [Concurrent, High Throughput Performance Testing with JMeter](https://howtojboss.wordpress.com/2012/07/31/concurrent-high-throughput-performance-testing-with-jmeter/)

## Distributed Testing

- [JMeter Distributed Testing Step-by-step](https://jmeter.apache.org/usermanual/jmeter_distributed_testing_step_by_step.pdf)
- [JMeter Remote Testing](https://jmeter.apache.org/usermanual/remote-test.html)
- [Setting up a JMeter Cluster for web server load testing](https://www.howtoforge.com/setting-up-jmeter-cluster-for-load-testing/)

## Results Processing

- [JMeter Report Dashboard](https://jmeter.apache.org/usermanual/generating-dashboard.html) - JMeter supports dashboard report generation to get graphs and statistics from a test plan.

### Results Analysis

- [JMeter Log Analysis](https://cwiki.apache.org/confluence/display/jmeter/LogAnalysis) - Suggestions and recipes for JMeter log analysis.
- [Analyzing JMeter Results](http://www.datazoo.de/articles/158/performance-testing-analyzing-jmeter-results)
- [JMeter Result Analysis: The Ultimate Guide](https://octoperf.com/blog/2017/10/19/how-to-analyze-jmeter-results/)
- [BlazeMeter Sense](https://sense.blazemeter.com/) - Service for storing and analysing performance test results.
- [JtlReporter](https://github.com/ludeknovy/jtl-reporter) - Online reporting application to generate reports by uploading JTL file.
- [JAnalyser](http://janalyser.com/) - Browser-based results analysis tool.
- [JMeter Result Analysis Plugin](https://github.com/afranken/jmeter-analysis-maven-plugin) - Maven plugin that parses JMeter test results and generates detailed reports with charts.
- [JMeter Results Analyser](https://sourceforge.net/projects/jmstats/) - Web-based application for collating, analysing and reporting JMeter test results.
- DB Results Collectors
  - [JMeter DBCollector Plugin](https://sourceforge.net/projects/jmeterdbcollect/) - Plugin to enable results logging into a database for more effective reporting.
  - [JMeter MySQLCollector Plugin](https://cwiki.apache.org/confluence/display/jmeter/MysqlCollectorPlugin) - Patch to configure listener to log into MySQL database.
- [JMeter SLA Report](https://github.com/sgoeschl/jmeter-sla-report) - JMeter HTML report generator based on JAMon.


## Performance Testing

### Streaming Protocols

- [Easy and realistic Load Testing of HTTP Live Streaming (HLS) with Apache JMeter](https://www.ubik-ingenierie.com/blog/easy-and-realistic-load-testing-of-http-live-streaming-hls-with-apache-jmeter/)
- [Using JMeter to Load Test Live HLS Concurrency of Wowza Streaming Engine](https://www.realeyes.com/blog/wowza-streaming/)
- [Load testing HLS with Ruby JMeter](https://www.flood.io/blog/load-testing-hls-with-ruby-jmeter)
- [Media Live Streaming Load Testing with JMeter](https://www.blazemeter.com/live-streaming/) - Collection of articles by BlazeMeter ([HLS](https://www.blazemeter.com/hls/), [RTMP](https://www.blazemeter.com/rtmp/), WS, podcasts, etc.).
- [HLS JMeter Plugin](https://github.com/Blazemeter/HLSPlugin)

### RESTful API

- [REST API Testing with JMeter. Step by Step Guide](https://octoperf.com/blog/2018/04/23/jmeter-rest-api-testing/)

## Tools

### Plugins

- [JMeter Plugins list](https://docs.google.com/spreadsheets/d/1FYMw3zCMr2Y37QCG_vOyC3HyrLxxi7x5I3khWLj3isU/) - List of available plugins and extensions.
- [JMeter Plugins](https://jmeter-plugins.org/) - Independent set of plugins for Apache JMeter, with plugin manager references many plugins and simplifies installation.
- [Ubik Load Pack](https://ubikloadpack.com/) - Productivity extensions for Apache JMeter.

### Extending JMeter

- [JMeter Developer Manual](https://cwiki.apache.org/confluence/display/jmeter/DeveloperManual)
- [How to write a plugin for JMeter](https://jmeter.apache.org/usermanual/jmeter_tutorial.html)
- [How to build a JMeter plugin utilising groovy](https://web.archive.org/web/20180225144718/http://artur.ejsmont.org/blog/content/how-to-build-a-jmeter-plugin-utilising-groovy)
- [How to create a plugin in JMeter](https://stackoverflow.com/questions/20422640/how-to-create-a-plugin-in-jmeter)
- [Custom JMeter Samplers and Config Elements](http://codyaray.com/2014/07/custom-jmeter-samplers-and-config-elements)
- [Implement Custom JMeter Samplers](https://dzone.com/articles/implement-custom-jmeter-samplers)

### IDE Integration

- [Intellij IDEA IDE Plugin](https://plugins.jetbrains.com/plugin/7013-jmeter-plugin) - Create run configurations and run JMeter tests from Intellij IDEA.
- [JMeter + Eclipse HOWTO](https://cwiki.apache.org/confluence/display/jmeter/JMeterAndEclipseHowTo) - Develop the JMeter project with Eclipse IDE.
- [NetBeans JMeter Kit](http://plugins.netbeans.org/plugin/49923/jmeter) - JMeter integration module for NetBeans IDE.
- [Using a Load Generator in NetBeans IDE](https://netbeans.apache.org//kb/docs/java/profile-loadgenerator.html)


## JMeter Performance

- [JMeter Performance](https://cwiki.apache.org/confluence/display/jmeter/JMeterPerformance) - JMeter performance evolution across versions.
- [JMeter Performance and Tuning Tips](https://www.ubik-ingenierie.com/blog/jmeter_performance_tuning_tips/) - By Ubik Ingenierie.
- [JMeter Performance and Tuning Tips](https://www.blazemeter.com/blog/jmeter-performance-and-tuning-tips) - By BlazeMeter.
- How to speed up JMeter: [part 1](https://performancelabus.com/how-to-speed-up-jmeter-part-1/), [part 2](https://performancelabus.com/how-to-speed-up-jmeter-part-2/)

## Trainings & Courses

- [JMeter: Performance and Load Testing (Feb 2019)](https://www.linkedin.com/learning/jmeter-performance-and-load-testing) - By LinkedIn Learning.
- [Advanced JMeter (Jul 2020)](https://www.linkedin.com/learning/advanced-jmeter) - By LinkedIn Learning.
- [JMeter Training Courses](https://www.nobleprog.co.uk/jmeter-training) - By NobleProg.
- [BlazeMeter University](https://www.blazemeter.com/university/) - By BlazeMeter.
- [JMeter Courses collection](https://www.udemy.com/topic/jmeter/) - By Udemy.
- [JMeter Training Course](http://www.absofttrainings.com/jmeter-training-course-and-tutorials/) - By ABSoft Trainings.
- [Web Applications (and Mobile Apps) Performance Testing with JMeter](http://pragmatictestlabs.com/web-applications-mobile-apps-performance-testing-jmeter/) - By Pragmatic Test Labs.
- [Training courses on Load Testing with Apache JMeter](https://www.ubik-ingenierie.com/blog/jmeter-trainings-by-contributors-and-committers/) - By Ubik Ingenierie.
- [Apache JMeter Training](https://qainsights.com/apache-jmeter-training/) - By QAInsights.
- [JMeter Getting Started Course (Apr 2019)](https://www.pluralsight.com/courses/jmeter-getting-started) - By Pluralsight.

## Videos

- [JMeter Tutorials](https://www.youtube.com/c/AutomationStepByStep/search?query=jmeter) - By Automation Step by Step.
- [Learn Apache JMeter Series](https://www.youtube.com/playlist?list=PLJ9A48W0kpRIjLkZ32Do9yDZXnnm7_uj_) - By QAInsights.
- [JMeter / Devops/ CI-CD / Cloud](https://www.youtube.com/c/xavki-linux/search?query=jmeter) - By xavki :fr:.

To see more check [Awesome JMeter](https://github.com/aliesbelik/awesome-jmeter)
