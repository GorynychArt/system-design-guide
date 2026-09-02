# Карта плейлиста → темы

Источник: [ByteByteGo — System Design Fundamentals](https://www.youtube.com/playlist?list=PLCRMIe5FDPsd0gVs500xeOewfySTsmEjf), 103 видео, суммарно 9 ч 41 мин.
Снято 2026-09-02 через внутренний API YouTube; порядок соответствует порядку в плейлисте.

> Классификация выполнена по названиям видео (без просмотра/расшифровок). Спорные случаи помечены в разделе «Требует проверки».

## Сводка по блокам

| Блок | Тема | Видео | Время | Файл документа |
|---|---|--:|--:|---|
| B00 | Процесс и обзорные | 6 | 44 мин | `00-workflow.md / 01-roadmap.md` |
| B01 | Сеть, протоколы, API | 17 | 1 ч 27 мин | `topics/01-network-and-api.md` |
| B02 | Приём трафика: LB / proxy / gateway / CDN | 6 | 28 мин | `topics/02-traffic-and-edge.md` |
| B03 | Хранилища и данные | 6 | 40 мин | `topics/03-storage-and-data.md` |
| B04 | Кэширование | 5 | 31 мин | `topics/04-caching.md` |
| B05 | Асинхронность и обмен сообщениями | 9 | 45 мин | `topics/05-async-and-messaging.md` |
| B06 | Распределённые системы и масштабирование | 5 | 32 мин | `topics/06-distributed-systems.md` |
| B07 | Архитектурные стили | 3 | 18 мин | `topics/07-architecture-styles.md` |
| B08 | Надёжность и отказоустойчивость | 1 | 5 мин | `topics/08-reliability.md` |
| B09 | Безопасность | 6 | 34 мин | `topics/09-security.md` |
| B10 | Доставка и эксплуатация | 13 | 1 ч 18 мин | `topics/10-delivery-and-ops.md` |
| B11 | Производительность и стоимость | 7 | 40 мин | `topics/11-performance-and-cost.md` |
| B12 | Кейсы: разборы реальных систем | 6 | 32 мин | `topics/12-case-studies.md` |
| BXX | Вне ядра system design | 13 | 1 ч 2 мин | `приложение «Смежное»` |
| | **Итого** | **103** | **9 ч 41 мин** | |

## Раскладка по блокам

### B00 — Процесс и обзорные

`00-workflow.md / 01-roadmap.md` · 6 видео · 44 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 85 | [8 Most Important System Design Concepts You Should Know](https://www.youtube.com/watch?v=BTjxUS_PylA) | 6:05 | Обзор ключевых концепций | — |
| 92 | [System Design Was HARD - Until You Knew the Trade-Offs](https://www.youtube.com/watch?v=1nENigGr-a0) | 5:09 | Trade-offs в system design, ч. 1 | — |
| 93 | [System Design Was HARD - Until You Knew the Trade-Offs, Part 2](https://www.youtube.com/watch?v=2g1G8Jr88xU) | 6:12 | Trade-offs в system design, ч. 2 | — |
| 96 | [7 System Design Concepts Explained in 10 Minutes](https://www.youtube.com/watch?v=Qd9tJ3H_hPE) | 10:44 | Обзор концепций (7 шт.) | — |
| 97 | [20 System Design Concepts You Must Know - Final Part](https://www.youtube.com/watch?v=uq-JpclPQV4) | 9:25 | Обзор концепций (20 шт., финал) | — |
| 98 | [System Design Interview – BIGGEST Mistakes to Avoid](https://www.youtube.com/watch?v=OvufRkoD-D0) | 6:48 | Ошибки на system design интервью | — |

### B01 — Сеть, протоколы, API

`topics/01-network-and-api.md` · 17 видео · 1 ч 27 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 2 | [Everything You Need to Know About DNS: Crash Course System Design #4](https://www.youtube.com/watch?v=27r4Bzuj5NQ) | 5:45 | DNS и разрешение имён | — |
| 4 | [What Is REST API? Examples And How To Use It: Crash Course System Design #3](https://www.youtube.com/watch?v=-mN3VyJuCjM) | 5:21 | REST | — |
| 14 | [What is OSI Model \| Real World Examples](https://www.youtube.com/watch?v=0y6FtKsg6J4) | 4:45 | Сетевая модель OSI / TCP-IP | — |
| 16 | [What is RPC? gRPC Introduction.](https://www.youtube.com/watch?v=gnchfOojMk4) | 6:09 | RPC и gRPC | — |
| 17 | [What Is GraphQL? REST vs. GraphQL](https://www.youtube.com/watch?v=yWzKJPw_VzM) | 5:15 | GraphQL vs REST | — |
| 24 | [HTTP/1 to HTTP/2 to HTTP/3](https://www.youtube.com/watch?v=a-sBfyiXysI) | 4:07 | Эволюция HTTP | — |
| 29 | [Top 6 Most Popular API Architecture Styles](https://www.youtube.com/watch?v=4vLxWqE94l4) | 4:21 | Стили API (REST / GraphQL / gRPC / WebSocket / webhook) | — |
| 44 | [HTTP Status Codes Explained In 5 Minutes](https://www.youtube.com/watch?v=qmpUfWN7hh4) | 5:07 | HTTP-коды состояния | — |
| 63 | [Top 9 Most Popular API Protocols](https://www.youtube.com/watch?v=zY2DMpCUfCg) | 3:54 | Протоколы API | — |
| 74 | [How the Internet Works in 9 Minutes](https://www.youtube.com/watch?v=sMHzfigUxz4) | 9:15 | Как работает интернет | — |
| 75 | [HTTP 1 Vs HTTP 2 Vs HTTP 3!](https://www.youtube.com/watch?v=UMwQjFzTQXw) | 7:37 | HTTP/1 vs HTTP/2 vs HTTP/3 (расширенно) | — |
| 80 | [Everything You NEED to KNOW About Web Applications](https://www.youtube.com/watch?v=_higfXfhjdo) | 3:03 | Устройство веб-приложения | B07 |
| 83 | [API Pagination: Making Billions of Products Scrolling Possible](https://www.youtube.com/watch?v=14K_a2kKTxU) | 3:12 | Пагинация API (offset vs cursor) | B11 |
| 86 | [API Vs SDK! What's the difference?](https://www.youtube.com/watch?v=GhX8sNyFo5w) | 4:52 | API vs SDK | — |
| 91 | [Top 6 Most Popular API Architecture Styles](https://www.youtube.com/watch?v=PNRbanEKGtw) | 1:14 | Стили API (короткая версия) | — |
| 94 | [APIs Explained in 6 Minutes!](https://www.youtube.com/watch?v=hltLrjabkiY) | 6:41 | Что такое API | — |
| 102 | [HTTP vs HTTPS Explained](https://www.youtube.com/watch?v=WvSVSbGo0wI) | 7:11 | HTTP vs HTTPS / TLS | B09 |

### B02 — Приём трафика: LB / proxy / gateway / CDN

`topics/02-traffic-and-edge.md` · 6 видео · 28 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 15 | [What Is A CDN? How Does It Work?](https://www.youtube.com/watch?v=RI9np1LWzqw) | 4:24 | CDN | — |
| 18 | [What is API Gateway?](https://www.youtube.com/watch?v=6ULyxuHKxg8) | 3:26 | API Gateway | — |
| 19 | [Proxy vs Reverse Proxy (Real-world Examples)](https://www.youtube.com/watch?v=4NB0NDtOwIQ) | 5:17 | Proxy и reverse proxy | — |
| 40 | [Top 6 Load Balancing Algorithms Every Developer Should Know](https://www.youtube.com/watch?v=dBmxNsS3BGE) | 5:18 | Алгоритмы балансировки нагрузки | — |
| 58 | [Reverse Proxy vs API Gateway vs Load Balancer](https://www.youtube.com/watch?v=RqfaTIWc3LQ) | 3:06 | Reverse proxy vs API gateway vs LB | — |
| 87 | [What is a LOAD BALANCER really about?](https://www.youtube.com/watch?v=LQuuoHTyYz8) | 6:45 | Балансировщик нагрузки | — |

### B03 — Хранилища и данные

`topics/03-storage-and-data.md` · 6 видео · 40 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 1 | [10+ Key Memory & Storage Systems: Crash Course System Design #5](https://www.youtube.com/watch?v=lX4CrbXMsNQ) | 4:17 | Иерархия памяти и типы хранилищ | B11 |
| 27 | [Secret To Optimizing SQL Queries - Understand The SQL Execution Order](https://www.youtube.com/watch?v=BHwzDmr6d7s) | 5:57 | Порядок выполнения SQL и оптимизация запросов | B11 |
| 60 | [ACID Properties in Databases With Examples](https://www.youtube.com/watch?v=GAe5oB742dw) | 4:57 | ACID | — |
| 68 | [7 Must-know Strategies to Scale Your Database](https://www.youtube.com/watch?v=_1IKwnbscQU) | 8:42 | Стратегии масштабирования БД | B06 |
| 76 | [How Search Really Works](https://www.youtube.com/watch?v=TByRaraQqW4) | 9:18 | Поисковые системы и инвертированный индекс | B12 |
| 101 | [What is a Data Lakehouse?](https://www.youtube.com/watch?v=taSmwcqdkQk) | 6:59 | Data lakehouse | — |

### B04 — Кэширование

`topics/04-caching.md` · 5 видео · 31 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 6 | [Cache Systems Every Developer Should Know](https://www.youtube.com/watch?v=dGAgxozNWFE) | 5:48 | Уровни кэширования | — |
| 10 | [Top 5 Redis Use Cases](https://www.youtube.com/watch?v=a4yX7RUgTxI) | 6:28 | Redis: сценарии применения | — |
| 25 | [System Design: Why is single-threaded Redis so fast?](https://www.youtube.com/watch?v=5TRFpFBccQM) | 3:39 | Redis: однопоточная модель | B11 |
| 57 | [Caching Pitfalls Every Developer Should Know](https://www.youtube.com/watch?v=wh98s0XhMmQ) | 6:41 | Грабли кэширования (инвалидация, stampede, hot key) | — |
| 100 | [What Is Redis Really About? Why Is It So Popular?](https://www.youtube.com/watch?v=z_NbVtbgBJw) | 9:01 | Redis: обзор | — |

### B05 — Асинхронность и обмен сообщениями

`topics/05-async-and-messaging.md` · 9 видео · 45 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 21 | [System Design: Why is Kafka fast?](https://www.youtube.com/watch?v=UNUz1-msbOM) | 5:02 | Kafka: механика производительности | B11 |
| 41 | [System Design: Apache Kafka In 3 Minutes](https://www.youtube.com/watch?v=HZklgPkboro) | 3:46 | Kafka: базовая архитектура | — |
| 56 | [Top 3 Things You Should Know About Webhooks!](https://www.youtube.com/watch?v=x_jjhcDrISk) | 3:55 | Webhooks | B01 |
| 59 | [System Design: Why is Kafka so Popular?](https://www.youtube.com/watch?v=yIAcHMJzqJc) | 4:20 | Kafka: почему популярен | — |
| 66 | [What is Data Pipeline? \| Why Is It So Popular?](https://www.youtube.com/watch?v=kGT4PcTEPP8) | 5:25 | Data pipeline | B03 |
| 67 | [Kafka vs. RabbitMQ vs. Messaging Middleware vs. Pulsar](https://www.youtube.com/watch?v=x4k1XEjNzYQ) | 4:31 | Kafka vs RabbitMQ vs Pulsar | — |
| 77 | [Top Kafka Use Cases You Should Know](https://www.youtube.com/watch?v=Ajz6dBp_EB4) | 5:56 | Сценарии применения Kafka | — |
| 84 | [Apache Kafka Fundamentals You Should Know](https://www.youtube.com/watch?v=-RDyEFvnTXI) | 4:55 | Kafka: фундамент | — |
| 99 | [System Design: Why is Kafka Popular?](https://www.youtube.com/watch?v=7_wkWQ9rB5I) | 7:41 | Kafka: почему популярен (расширенно) | — |

### B06 — Распределённые системы и масштабирование

`topics/06-distributed-systems.md` · 5 видео · 32 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 13 | [CAP Theorem Simplified](https://www.youtube.com/watch?v=BHqjEjzAicA) | 5:33 | CAP-теорема | — |
| 26 | [Top 7 Most-Used Distributed System Patterns](https://www.youtube.com/watch?v=nH4qjmP2KEE) | 6:14 | Паттерны распределённых систем | — |
| 50 | [Vertical Vs Horizontal Scaling: Key Differences You Should Know](https://www.youtube.com/watch?v=dvRFHG2-uYs) | 4:34 | Вертикальное vs горизонтальное масштабирование | — |
| 65 | [KISS, SOLID, CAP, BASE: Important Terms You Might Not Know!](https://www.youtube.com/watch?v=cTyZ_hbmbDw) | 6:38 | KISS / SOLID / CAP / BASE | B00 |
| 79 | [Scalability Simply Explained in 10 Minutes](https://www.youtube.com/watch?v=EWS_CIxttVw) | 9:20 | Масштабируемость | — |

### B07 — Архитектурные стили

`topics/07-architecture-styles.md` · 3 видео · 18 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 8 | [But What Is Cloud Native Really All About?](https://www.youtube.com/watch?v=p-88GN1WVs8) | 7:32 | Cloud native | — |
| 20 | [What Are Microservices Really All About? (And When Not To Use It)](https://www.youtube.com/watch?v=lTAcCNbJ7KE) | 4:45 | Микросервисы vs монолит | — |
| 52 | [Everything You NEED to Know About Client Architecture Patterns](https://www.youtube.com/watch?v=I5c7fBgvkNY) | 5:51 | Клиентские архитектурные паттерны | — |

### B08 — Надёжность и отказоустойчивость

`topics/08-reliability.md` · 1 видео · 5 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 90 | [8 Most Important Tips for Designing Fault-Tolerant System](https://www.youtube.com/watch?v=3Lis4w4_bBc) | 5:11 | Проектирование отказоустойчивых систем | — |

### B09 — Безопасность

`topics/09-security.md` · 6 видео · 34 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 22 | [System Design: How to store passwords in the database?](https://www.youtube.com/watch?v=zt8Cocdy15c) | 3:44 | Хранение паролей (хэш, соль) | — |
| 33 | [OAuth 2 Explained In Simple Terms](https://www.youtube.com/watch?v=ZV5yTm4pT8g) | 4:32 | OAuth 2.0 | — |
| 48 | [Why is JWT popular?](https://www.youtube.com/watch?v=P2CPd9ynFLg) | 5:14 | JWT | — |
| 61 | [Top 12 Tips For API Security](https://www.youtube.com/watch?v=6WZ6S-qmtqY) | 9:47 | Безопасность API | — |
| 71 | [Session Vs JWT: The Differences You May Not Know!](https://www.youtube.com/watch?v=fyTxwIa-1U0) | 7:00 | Session vs JWT | — |
| 81 | [How SSH Really Works](https://www.youtube.com/watch?v=rlMfRa7vfO8) | 4:05 | SSH | — |

### B10 — Доставка и эксплуатация

`topics/10-delivery-and-ops.md` · 13 видео · 1 ч 18 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 9 | [Debugging Like A Pro](https://www.youtube.com/watch?v=J8uAiZJMfzQ) | 5:48 | Отладка и диагностика в проде | — |
| 11 | [CI/CD In 5 Minutes \| Is It Worth The Hassle: Crash Course System Design #2](https://www.youtube.com/watch?v=42UP1fxi2SY) | 5:46 | CI/CD | — |
| 12 | [Kubernetes Explained in 6 Minutes \| k8s Architecture](https://www.youtube.com/watch?v=TlHvYWVUZyc) | 6:28 | Kubernetes: архитектура | — |
| 23 | [Big Misconceptions about Bare Metal, Virtual Machines, and Containers](https://www.youtube.com/watch?v=Jz8Gs4UHTO8) | 7:02 | Bare metal / VM / контейнеры | — |
| 30 | [Top 5 Most-Used Deployment Strategies](https://www.youtube.com/watch?v=AWVTKBUnoIg) | 10:00 | Стратегии деплоя (blue-green, canary, rolling) | — |
| 36 | [DevOps vs SRE vs Platform Engineering \| Clear Big Misconceptions](https://www.youtube.com/watch?v=an8SrFtJBdM) | 4:44 | DevOps / SRE / Platform Engineering | — |
| 38 | [Why Google and Meta Put Billion Lines of Code In 1 Repository?](https://www.youtube.com/watch?v=x3cANGNPyx0) | 7:09 | Монорепозиторий vs полирепо | B07 |
| 43 | [Is Docker Still Relevant?](https://www.youtube.com/watch?v=Cs2j-Rjqg94) | 3:46 | Docker: актуальность | — |
| 46 | [How Big Tech Ships Code to Production](https://www.youtube.com/watch?v=xSPA2yBgDgA) | 4:28 | Пайплайн доставки в бигтехе | — |
| 51 | [Top 9 Most Popular Types of API Testing](https://www.youtube.com/watch?v=qquIJ1Ivusg) | 4:08 | Виды тестирования API | — |
| 64 | [Do You Know How Mobile Apps Are Released?](https://www.youtube.com/watch?v=RIX4ufelA58) | 5:00 | Релиз мобильных приложений | — |
| 78 | [Why is Kubernetes Popular \| What is Kubernetes?](https://www.youtube.com/watch?v=lv0DdVLZuHc) | 9:52 | Kubernetes: зачем нужен | — |
| 88 | [System Design: Why Is Docker Important?](https://www.youtube.com/watch?v=QEzbZKtLi-g) | 4:02 | Docker: зачем нужен | — |

### B11 — Производительность и стоимость

`topics/11-performance-and-cost.md` · 7 видео · 40 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 3 | [Latency Numbers Programmer Should Know: Crash Course System Design #1](https://www.youtube.com/watch?v=FqR5vESuKe0) | 6:22 | Числа задержек и бюджет latency | B00 |
| 5 | [10 Key Data Structures We Use Every Day](https://www.youtube.com/watch?v=ouipSd_5ivQ) | 8:43 | Структуры данных в инфраструктуре (bloom filter, skip list, LSM) | B03 |
| 37 | [Top 7 Ways to 10x Your API Performance](https://www.youtube.com/watch?v=zvWKqUiovAM) | 6:05 | Оптимизация производительности API | — |
| 69 | [Concurrency Vs Parallelism!](https://www.youtube.com/watch?v=RlM9AfWf1WU) | 4:13 | Конкурентность vs параллелизм | — |
| 73 | [Linux Performance Tools!](https://www.youtube.com/watch?v=iJ_eIsA5E1U) | 6:41 | Инструменты профилирования Linux | B10 |
| 82 | [Big-O Notation in 3 Minutes](https://www.youtube.com/watch?v=x2CRZaN2xgM) | 3:04 | Big-O | — |
| 89 | [How the Garbage Collector Works in Java, Python, and Go!](https://www.youtube.com/watch?v=3Kqal7QaCCM) | 5:09 | Сборка мусора (JVM / Python / Go) | — |

### B12 — Кейсы: разборы реальных систем

`topics/12-case-studies.md` · 6 видео · 32 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 28 | [Amazon Prime Video Ditches AWS Serverless, Saves 90%](https://www.youtube.com/watch?v=JTp0TY_2hXM) | 4:15 | Prime Video: serverless → монолит | B07, B11 |
| 31 | [How Discord Stores TRILLIONS of Messages](https://www.youtube.com/watch?v=O3PwuzCvAjI) | 7:11 | Discord: хранение триллионов сообщений | B03 |
| 32 | [Uncovering Stack Overflow's Shocking Architecture](https://www.youtube.com/watch?v=fKc050dvNIE) | 4:09 | Stack Overflow: монолит на масштабе | B07 |
| 34 | [Demystifying the Unusual Evolution of the Netflix API Architecture](https://www.youtube.com/watch?v=Uu32ggF-DWg) | 4:12 | Netflix: эволюция API-архитектуры | B07 |
| 54 | [How Disney Hotstar Captures One Billion Emojis!](https://www.youtube.com/watch?v=UN1kW5AHid4) | 4:35 | Disney+ Hotstar: миллиард эмодзи | B05 |
| 95 | [Trillions of Web Pages: Where Does Google Store Them?](https://www.youtube.com/watch?v=nBvDtj-p6VM) | 8:36 | Google: хранение триллионов страниц | B03 |

### BXX — Вне ядра system design

`приложение «Смежное»` · 13 видео · 1 ч 2 мин

| # | Видео | Длит. | Топик карточки | Также относится к |
|--:|---|--:|---|---|
| 7 | [The Most Beloved Burger for Developers](https://www.youtube.com/watch?v=7swoLEqABhQ) | 3:25 | Развлекательное | — |
| 35 | [1 Year Of YouTube \| Best System Design Series](https://www.youtube.com/watch?v=q2MWdzhMq6A) | 1:03 | Канальное / анонс | — |
| 39 | [Git MERGE vs REBASE: Everything You Need to Know](https://www.youtube.com/watch?v=0chZFIZLR_0) | 4:34 | Git: merge vs rebase | B10 |
| 42 | [Software Engineer Promo is SUPER easy - DO THIS](https://www.youtube.com/watch?v=OTfYFl3rzjg) | 4:14 | Карьера | — |
| 45 | [Python Vs C++ Vs Java!](https://www.youtube.com/watch?v=hnlz0YYCpBU) | 4:41 | Сравнение языков | — |
| 47 | [How Git Works: Explained in 4 Minutes](https://www.youtube.com/watch?v=e9lnsKot_SQ) | 4:18 | Как устроен Git | B10 |
| 49 | [How Does Linux Boot Process Work?](https://www.youtube.com/watch?v=XpFsMB6FoOs) | 4:44 | Загрузка Linux | — |
| 53 | [Linux File System Explained!](https://www.youtube.com/watch?v=bbmWOjuFmgA) | 5:16 | Файловая система Linux | — |
| 55 | [Top 6 Tools to Turn Code into Beautiful Diagrams](https://www.youtube.com/watch?v=jCd6XfWLZsg) | 3:24 | Инструменты диаграмм | B00 |
| 62 | [Top 9 Must-Read Blogs for Engineers](https://www.youtube.com/watch?v=UuT61kf292A) | 5:55 | Ресурсы для чтения | B00 |
| 70 | [Linux Crash Course - Understanding File Permissions](https://www.youtube.com/watch?v=4N4Q576i3zA) | 4:32 | Права доступа в Linux | — |
| 72 | [25 Computer Papers You Should Read!](https://www.youtube.com/watch?v=_kynGl5hr9U) | 9:11 | Статьи-первоисточники | B00 |
| 103 | [How the JVM Actually Works](https://www.youtube.com/watch?v=bF28LFPjFsI) | 6:43 | Как работает JVM | — |

## Дубли и пересечения

Темы, раскрытые в нескольких видео — при сборке карточек берём наиболее полное, остальные идут как дополнительные ссылки.

| Тема | Видео | Что делаем |
|---|---|---|
| Kafka | 21, 41, 59, 67, 77, 84, 99 | Одна карточка «Kafka», внутри разделы: модель, производительность, сценарии, сравнение с RabbitMQ/Pulsar |
| Redis | 10, 25, 100 | Одна карточка «Redis», разделы: модель данных, однопоточность, сценарии |
| HTTP-версии | 24, 75 | Одна карточка, #75 как расширенная версия |
| Стили API | 29, 91 | #91 — короткий пересказ #29, оставляем как ссылку |
| Kubernetes | 12, 78 | Одна карточка |
| Docker | 43, 88 | Одна карточка |
| Обзоры концепций | 85, 96, 97 | Не карточки — источник для чек-листа в `01-roadmap.md` |
| Trade-offs | 92, 93 | Источник для раздела `00-workflow.md` → W10 |

## Требует проверки

Классификация сделана по названиям. Эти видео стоит открыть перед финальной раскладкой — название не даёт понять содержание:

| # | Видео | Гипотеза |
|--:|---|---|
| 5 | 10 Key Data Structures We Use Every Day | Структуры данных в инфраструктуре (bloom filter, skip list, LSM-дерево) → B03/B11, а не базовый CS |
| 7 | The Most Beloved Burger for Developers | Похоже на развлекательное; если про слои стека — переедет в B00 |
| 55 | Top 6 Tools to Turn Code into Beautiful Diagrams | Инструменты документирования → приложение, либо B00 (артефакты дизайна) |
| 65 | KISS, SOLID, CAP, BASE | Смесь принципов кода и распределённых систем; может разойтись на две карточки |
| 80 | Everything You NEED to KNOW About Web Applications | Обзорное; либо вводная карточка B01, либо часть roadmap |

## Вне ядра system design

13 видео (1 ч 2 мин) — про инструменты разработчика, ОС, языки и карьеру: 7, 35, 39, 42, 45, 47, 49, 53, 55, 62, 70, 72, 103.
Они не выбрасываются: 62 и 72 (блоги и статьи-первоисточники) уходят в `95-sources.md`, остальные — в приложение «Смежное», отдельным списком без карточек.
