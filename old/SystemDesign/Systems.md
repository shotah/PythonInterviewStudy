# Common System Design services
<!-- TOC -->

- [Common System Design services](#common-system-design-services)
  - [Christopher's ideal app without cloud providers technology](#christophers-ideal-app-without-cloud-providers-technology)
  - [Software Definitions](#software-definitions)
    - [Nginx](#nginx)
    - [Alpine linux](#alpine-linux)
      - [ABOUT](#about)
    - [memcached](#memcached)
    - [Kafka](#kafka)
      - [What is Kafka Used For?](#what-is-kafka-used-for)
    - [Rabitmq](#rabitmq)
      - [What is RabbitMQ Used For?](#what-is-rabbitmq-used-for)
    - [LogStash](#logstash)
    - [Redis](#redis)
    - [MongoDB](#mongodb)
    - [MySQL](#mysql)
  - [Logging Software](#logging-software)
    - [prometheus](#prometheus)
    - [Grafana](#grafana)
  - [Github GitFarm and CI/CD](#github-gitfarm-and-cicd)
    - [Github actions to be used](#github-actions-to-be-used)
    - [Github packages and Container registry](#github-packages-and-container-registry)
    - [Github Alternative](#github-alternative)
  - [Protocol documentation](#protocol-documentation)
    - [gRPC](#grpc)
  - [Capacity Planning](#capacity-planning)
    - [Back of the envelope](#back-of-the-envelope)
    - [Latency Numbers](#latency-numbers)
    - [Test your knowledge](#test-your-knowledge)

<!-- /TOC -->

## Christopher's ideal app without cloud providers technology

Deployment (CI/CD):

- Github
- Github actions
  - To validate by making sure linting and testing are running clean and passing.
  - To build and push container builds to a container registry
  - To Validate a kubernetes cluster publishing
  - To Push updated pods to the cluster

- Orchestrated by kubernetes
- Use of Helm charts for ease of full cluster/pod deployment
- using the github package system to store packages and container images.

Networking:

- Bind on Alpine for DNS deployed and managed with Kube and Helm
- nginx with geoip2 for main app dns record
  - alternative option would be to use a CDN like Cloudflare
- nginx will forward to regional dns records like us.app.com and eu.app.com
- local region routing by nginx load balancer

Application:

- container of application
- queues provided by RabbitMQ
- Redis for database caching
- Preference for NoSQL MongoDB for object storage instead of relational db.
  - Considerations:
  - Trade off on performance, but ease of application object storage
  - Sharding for performance
  - MySql relational database for large complicated databases
  - Use of Primary and Secondary and Read-Only replica's

Monitoring:

- monitored by prometheus side car
- data visualized by grafana

## Software Definitions

### Nginx

Nginx is a web server that can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache. The software was created by Igor Sysoev and publicly released in 2004. Nginx is free and open-source software, released under the terms of the 2-clause BSD license. Wikipedia

[Nginx Homepage](https://www.nginx.com/)
[How geolocation works](https://www.bigdatacloud.com/blog/ip-geolocation-demystified)
[geolocation.com](https://www.geolocation.com/)
[ip geolocation databases](https://www.lir.services/blog/ip-geolocation/)
[nginx and geoip2](https://www.cleverti.com/blog/how-to-build-a-load-balancer-based-on-user-s-location-with-nginx-and-geoip2/)
[cloudflare CDN for Geolocation](https://support.cloudflare.com/hc/en-us/articles/200168236-Configuring-IP-geolocation)

```bash
NGINX
log_format cloudflare_custom '"$http_cf_ipcountry"';
More about NGINX log_format
```

### Alpine linux

#### ABOUT

Alpine Linux is an independent, non-commercial, general purpose Linux distribution designed for power users who appreciate security, simplicity and resource efficiency.

SMALL
Alpine Linux is built around musl libc and busybox. This makes it small and very resource efficient. A container requires no more than 8 MB and a minimal installation to disk requires around 130 MB of storage. Not only do you get a fully-fledged Linux environment but a large selection of packages from the repository.

Binary packages are thinned out and split, giving you even more control over what you install, which in turn keeps your environment as small and efficient as possible.

SIMPLE
Alpine Linux is a very simple distribution that will try to stay out of your way. It uses its own package manager called apk, the OpenRC init system, script driven set-ups and that’s it! This provides you with a simple, crystal-clear Linux environment without all the noise. You can then add on top of that just the packages you need for your project, so whether it’s building a home PVR, or an iSCSI storage controller, a wafer-thin mail server container, or a rock-solid embedded switch, nothing else will get in the way.

SECURE
Alpine Linux was designed with security in mind. All userland binaries are compiled as Position Independent Executables (PIE) with stack smashing protection. These proactive security features prevent exploitation of entire classes of zero-day and other vulnerabilities.

[Alpine Homepage](https://www.alpinelinux.org/about/)

### memcached

What is Memcached?
Free & open source, high-performance, distributed memory object caching system, generic in nature, but intended for use in speeding up dynamic web applications by alleviating database load.

Memcached is an in-memory key-value store for small chunks of arbitrary data (strings, objects) from results of database calls, API calls, or page rendering.

Memcached is simple yet powerful. Its simple design promotes quick deployment, ease of development, and solves many problems facing large data caches. Its API is available for most popular languages.

[Memcached Homepage](https://memcached.org/)

### Kafka

Apache Kafka is a distributed event store and stream-processing platform. It is an open-source system developed by the Apache Software Foundation written in Java and Scala. The project aims to provide a unified, high-throughput, low-latency platform for handling real-time data feeds. Wikipedia

#### What is Kafka Used For?

Kafka is best used for streaming from A to B without resorting to complex routing, but with maximum throughput. It’s also ideal for event sourcing, stream processing, and carrying out modeling changes to a system as a sequence of events. Kafka is also suitable for processing data in multi-stage pipelines.

Bottom line, use Kafka if you need a framework for storing, reading, re-reading, and analyzing streaming data. It’s ideal for routinely audited systems or that store their messages permanently. Breaking it down even further, Kafka shines with real-time processing and analyzing data.

[Kafka Homepage](https://kafka.apache.org/)

### Rabitmq

#### What is RabbitMQ Used For?

Developers use RabbitMQ to process high-throughput and reliable background jobs, plus integration and intercommunication between and within applications. Programmers also use RabbitMQ to perform complex routing to consumers and integrate multiple applications and services with non-trivial routing logic.

RabbitMQ is perfect for web servers that need rapid request-response. It also shares loads between workers under high load (20K+ messages/second). RabbitMQ can also handle background jobs or long-running tasks like PDF conversion, file scanning, or image scaling.

Summing it up, use RabbitMQ with long-running tasks, reliably running background jobs, and communication/integration between and within applications.

[RabbitMQ Homepage](https://www.rabbitmq.com/)

### LogStash

Logstash is a light-weight, open-source, server-side data processing pipeline that allows you to collect data from a variety of sources, transform it on the fly, and send it to your desired destination. It is most often used as a data pipeline for Elasticsearch, an open-source analytics and search engine.

[LogStash Homepage](https://www.elastic.co/logstash/)

### Redis

Redis is an in-memory data structure store, used as a distributed, in-memory key–value database, cache and message broker, with optional durability. Redis supports different kinds of abstract data structures, such as strings, lists, maps, sets, sorted sets, HyperLogLogs, bitmaps, streams, and spatial indices. Wikipedia

[Redis Homepage](https://redis.com/)

### MongoDB

MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, MongoDB uses JSON-like documents with optional schemas. MongoDB is developed by MongoDB Inc. and licensed under the Server Side Public License which is deemed non-free by several distributions. Wikipedia

[Mongo Homepage](https://www.mongodb.com/home)
[Caching with Redis](https://codeforgeek.com/caching-a-mongodb-database-with-redis/)

### MySQL

MySQL is an open-source relational database management system. Its name is a combination of "My", the name of co-founder Michael Widenius's daughter My, and "SQL", the abbreviation for Structured Query Language. Wikipedia

[MySQL Homepage](https://www.mysql.com/)

## Logging Software

### prometheus

Prometheus is a free software application used for event monitoring and alerting.[2] It records real-time metrics in a time series database (allowing for high dimensionality) built using a HTTP pull model, with flexible queries and real-time alerting.[3][4] The project is written in Go and licensed under the Apache 2 License, with source code available on GitHub,[5] and is a graduated project of the Cloud Native Computing Foundation, along with Kubernetes and Envoy.[6]

[prometheus Homepage](https://prometheus.io/)
[prometheus Wikipedia](https://en.wikipedia.org/wiki/Prometheus_(software))

### Grafana

Grafana is a multi-platform open source analytics and interactive visualization web application. It provides charts, graphs, and alerts for the web when connected to supported data sources. Wikipedia

[Grafana Homepage](https://grafana.com/)

## Github (GitFarm and CI/CD)

### Github actions to be used

Lint and test code
Package build
Container build
Cluster Deploy
Application deploy

### Github packages and Container registry

<https://github.com/features/packages>

### Github Alternative

Gitlab community edition <https://gitlab.com/rluna-gitlab/gitlab-ce>

## Protocol documentation

### gRPC

gRPC is a cross-platform open source high performance Remote Procedure Call framework. gRPC was initially created by Google, which has used a single general-purpose RPC infrastructure called Stubby to connect the large number of microservices running within and across its data centers for over a decade. Wikipedia

[gRPC Homepage](https://grpc.io/)

## Capacity Planning

https://www.dballona.com/en/system-design-capacity-planning-basics

### Back of the envelope

https://www.codementor.io/@robinpalotai/back-of-the-envelope-calculation-for-system-design-interviews-z4ljbsp5l

### Latency Numbers

https://github.com/sirupsen/napkin-math
https://gist.github.com/jboner/2841832

### Test your knowledge

https://computers-are-fast.github.io/
