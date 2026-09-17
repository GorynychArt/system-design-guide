# Глоссарий

Термины, используемые в документе, с русским и английским написанием. Определение — одна фраза; подробности по ссылке на карточку.

Отсортировано по русскому термину; аббревиатуры, не имеющие устоявшегося перевода, — в конце.

| Термин | English | Что это | Подробно |
|---|---|---|---|
| Агрегат | Aggregate | Группа объектов, изменяемая как одно целое; единица согласованности и транзакционная граница. | [ARCH-03](topics/07-architecture-styles.md#internal-architecture) |
| Анти-коррупционный слой | Anti-corruption layer | Прослойка, переводящая чужую модель в свою, чтобы внешние понятия не протекали внутрь контекста. | [ARCH-02](topics/07-architecture-styles.md#boundaries) |
| Аренда | Lease | Блокировка с ограниченным сроком действия; истекает сама, если держатель исчез. | [DIST-07](topics/06-distributed-systems.md#distributed-locks) |
| Бюджет задержки | Latency budget | Разложение целевого времени ответа по участкам пути запроса. | [PERF-01](topics/11-performance-and-cost.md#latency-numbers) |
| Бюджет ошибок | Error budget | Разрешённая доля неуспеха как ресурс: пока есть — можно рисковать выкатками. | [OPS-09](topics/10-delivery-and-ops.md#slo) |
| Векторные часы | Vector clock | Счётчики по репликам, позволяющие отличить причинную связь от параллельности. | [DIST-10](topics/06-distributed-systems.md#conflicts) |
| Вероятностный счётчик | HyperLogLog | Приблизительный подсчёт уникальных значений за фиксированную память. | [CASE-11](topics/12-case-studies.md#top-k) |
| Взаимный TLS | mTLS | Обе стороны предъявляют сертификаты; идентичность сервиса вместо доверия по адресу. | [SEC-09](topics/09-security.md#transport-security) |
| Витрина | Data mart | Производная структура данных, подготовленная под конкретные запросы. | [DATA-15](topics/03-storage-and-data.md#oltp-olap) |
| Время события / время обработки | Event time / processing time | Когда событие произошло против того, когда его обработали; определяет корректность окон. | [MSG-11](topics/05-async-and-messaging.md#pipeline) |
| Выкатка канареечная | Canary release | Малая доля трафика на новую версию с наблюдением перед расширением. | [OPS-02](topics/10-delivery-and-ops.md#deploy) |
| Гарантии сессии | Session guarantees | Read-your-writes, monotonic reads — практический минимум согласованности для интерфейса. | [DIST-03](topics/06-distributed-systems.md#consistency-models) |
| Геохэш | Geohash | Кодирование координат в сортируемую строку; общий префикс означает соседство. | [DATA-14](topics/03-storage-and-data.md#geo) |
| Гистограмма | Histogram | Распределение значений по корзинам; единственный корректный способ агрегировать перцентили. | [PERF-02](topics/11-performance-and-cost.md#percentiles) |
| Деградация управляемая | Graceful degradation | Заранее описанные режимы работы с отключением менее ценных функций. | [REL-04](topics/08-reliability.md#degradation) |
| Дедупликация | Deduplication | Отбрасывание повторной обработки по устойчивому идентификатору. | [MSG-06](topics/05-async-and-messaging.md#delivery-guarantees) |
| Джиттер | Jitter | Случайный разброс задержки повторов, разводящий клиентов во времени. | [REL-01](topics/08-reliability.md#timeouts-retries) |
| Дырявое ведро | Leaky bucket | Алгоритм ограничения частоты со сглаживанием потока. | [EDGE-06](topics/02-traffic-and-edge.md#rate-limiting) |
| Идемпотентность | Idempotency | Повторное выполнение операции не создаёт второй эффект. | [NET-16](topics/01-network-and-api.md#idempotency) |
| Инвертированный индекс | Inverted index | Отображение «терм → документы»; основа полнотекстового поиска. | [DATA-13](topics/03-storage-and-data.md#search) |
| Кворум | Quorum | Число узлов, которое должно ответить; при R + W > N множества пересекаются. | [DIST-04](topics/06-distributed-systems.md#quorum) |
| Консенсус | Consensus | Согласование единого решения группой узлов, переживающее отказ меньшинства. | [DIST-05](topics/06-distributed-systems.md#consensus) |
| Контекст ограниченный | Bounded context | Область, внутри которой термины имеют одно значение; граница модели и обычно сервиса. | [ARCH-02](topics/07-architecture-styles.md#boundaries) |
| Кэш-промах | Cache miss | Запрос, не найденный в кэше; массовые промахи опаснее отсутствия кэша. | [CACHE-04](topics/04-caching.md#cache-pathologies) |
| Лавина запросов | Cache stampede | Одновременный поход множества запросов в источник после истечения популярного ключа. | [CACHE-04](topics/04-caching.md#cache-pathologies) |
| Лаг репликации | Replication lag | Отставание реплики от источника; причина «данные не обновились». | [DATA-09](topics/03-storage-and-data.md#replication) |
| Линеаризуемость | Linearizability | Поведение как у единственной копии данных; сильнейшая и дорогая гарантия. | [DIST-03](topics/06-distributed-systems.md#consistency-models) |
| Логические часы | Lamport clock | Счётчик событий, задающий согласованный порядок без опоры на физическое время. | [DIST-10](topics/06-distributed-systems.md#conflicts) |
| Машина состояний | State machine | Явное описание состояний и разрешённых переходов вместо условий по коду. | [ARCH-03](topics/07-architecture-styles.md#internal-architecture) |
| Модульный монолит | Modular monolith | Единая выкатка при явных внутренних границах, проверяемых сборкой. | [ARCH-01](topics/07-architecture-styles.md#monolith-microservices) |
| Мультитенантность | Multi-tenancy | Обслуживание нескольких изолированных арендаторов одной системой. | [DATA-18](topics/03-storage-and-data.md#multitenancy) |
| Наблюдаемость | Observability | Способность ответить на незаданный заранее вопрос о поведении системы. | [OPS-07](topics/10-delivery-and-ops.md#observability) |
| Насыщение | Saturation | Объём работы, ожидающей в очереди; предсказывает деградацию лучше утилизации. | [PERF-07](topics/11-performance-and-cost.md#queueing) |
| Обнаружение сервисов | Service discovery | Механизм ответа на вопрос «по какому адресу сейчас живёт сервис». | [EDGE-08](topics/02-traffic-and-edge.md#discovery) |
| Обратное давление | Backpressure | Механизм, заставляющий источник замедлиться, когда приёмник не справляется. | [MSG-09](topics/05-async-and-messaging.md#backpressure) |
| Ограждающий маркер | Fencing token | Растущий номер, позволяющий ресурсу отвергнуть операцию устаревшего держателя блокировки. | [DIST-07](topics/06-distributed-systems.md#distributed-locks) |
| Оптимистическая блокировка | Optimistic locking | Проверка версии при записи вместо удержания блокировки. | [DATA-08](topics/03-storage-and-data.md#isolation) |
| Оркестрация | Orchestration | Явный координатор процесса, хранящий его состояние. | [ARCH-04](topics/07-architecture-styles.md#event-driven) |
| Ответ устаревший | Stale response | Отдача неактуальных данных ради скорости или доступности. | [NET-06](topics/01-network-and-api.md#http-caching) |
| Отсев выбросов | Outlier detection | Временное исключение экземпляра, отвечающего медленно или ошибками. | [EDGE-01](topics/02-traffic-and-edge.md#load-balancing) |
| Партиция | Partition | Часть топика или таблицы; единица порядка и параллелизма. | [MSG-04](topics/05-async-and-messaging.md#kafka) |
| Перцентиль | Percentile | Значение, ниже которого лежит заданная доля измерений; p99 важнее среднего. | [PERF-02](topics/11-performance-and-cost.md#percentiles) |
| Порты и адаптеры | Ports and adapters | Организация сервиса, при которой зависимости направлены к предметной области. | [ARCH-03](topics/07-architecture-styles.md#internal-architecture) |
| Предохранитель | Circuit breaker | Автомат, прекращающий вызовы к деградировавшей зависимости. | [REL-02](topics/08-reliability.md#circuit-breaker) |
| Проекция | Projection / read model | Производная модель чтения, построенная из событий или источника истины. | [ARCH-06](topics/07-architecture-styles.md#cqrs) |
| Радиус поражения | Blast radius | Доля пользователей и функций, затронутых одним отказом. | [REL-07](topics/08-reliability.md#cells) |
| Разделение чтения и записи | CQRS | Две модели вместо одной: под инварианты записи и под запросы чтения. | [ARCH-06](topics/07-architecture-styles.md#cqrs) |
| Реестр схем | Schema registry | Хранилище схем событий с проверкой совместимости версий. | [NET-18](topics/01-network-and-api.md#contracts) |
| Резерв с TTL | Reservation | Временное удержание дефицитного ресурса до подтверждения. | [CASE-08](topics/12-case-studies.md#booking) |
| Репликация | Replication | Копии данных на нескольких узлах ради доступности и масштаба чтения. | [DATA-09](topics/03-storage-and-data.md#replication) |
| Сага | Saga | Последовательность локальных транзакций с компенсациями вместо распределённой транзакции. | [DIST-08](topics/06-distributed-systems.md#distributed-transactions) |
| Сброс нагрузки | Load shedding | Осознанный отказ части запросов при перегрузке ради сохранения остальных. | [REL-03](topics/08-reliability.md#load-shedding) |
| Сверка | Reconciliation | Периодическое сравнение источника и производных копий для поиска расхождений. | [DATA-16](topics/03-storage-and-data.md#data-integrity) |
| Сегментация трафика | Traffic splitting | Направление доли запросов на другую версию на границе. | [EDGE-04](topics/02-traffic-and-edge.md#ingress) |
| Сервисная сетка | Service mesh | Инфраструктурный слой из прокси, снимающий с сервисов сетевые заботы. | [ARCH-10](topics/07-architecture-styles.md#mesh) |
| Согласованное хэширование | Consistent hashing | Распределение ключей, при котором изменение состава узлов двигает малую долю данных. | [DATA-11](topics/03-storage-and-data.md#consistent-hashing) |
| Согласованность отложенная | Eventual consistency | Копии сойдутся при отсутствии новых записей; о промежутке ничего не обещано. | [DIST-03](topics/06-distributed-systems.md#consistency-models) |
| Список пропусков | Skip list | Структура упорядоченного множества; используется в Redis. | [PERF-03](topics/11-performance-and-cost.md#big-o) |
| Статическая стабильность | Static stability | Способность пережить отказ, не совершая новых действий. | [REL-06](topics/08-reliability.md#fault-tolerance-overview) |
| Строка исходящего шлюза | Egress proxy | Единая точка исходящих обращений с белым списком адресов. | [EDGE-02](topics/02-traffic-and-edge.md#proxy) |
| Токенное ведро | Token bucket | Алгоритм ограничения частоты, допускающий всплеск в пределах накопленного. | [EDGE-06](topics/02-traffic-and-edge.md#rate-limiting) |
| Транзакционный ящик | Transactional outbox | Запись события в ту же транзакцию, что и изменение данных; публикация отдельным процессом. | [MSG-07](topics/05-async-and-messaging.md#outbox) |
| Трассировка | Distributed tracing | Путь одного запроса через все сервисы с временем каждого участка. | [OPS-07](topics/10-delivery-and-ops.md#observability) |
| Тёмный запуск | Dark launch | Исполнение нового кода на реальном трафике без показа результата. | [OPS-02](topics/10-delivery-and-ops.md#deploy) |
| Ужимание и расширение | Expand / contract | Схема безопасной миграции: добавить совместимое, перевести, удалить старое. | [DATA-17](topics/03-storage-and-data.md#migrations) |
| Уровень изоляции | Isolation level | Степень защиты транзакции от эффектов параллельных транзакций. | [DATA-08](topics/03-storage-and-data.md#isolation) |
| Утилизация | Utilization | Доля времени, в течение которой ресурс занят; не заменяет насыщение. | [PERF-07](topics/11-performance-and-cost.md#queueing) |
| Фильтр Блума | Bloom filter | Вероятностная структура, отвечающая «точно нет» или «возможно да». | [PERF-03](topics/11-performance-and-cost.md#big-o) |
| Фича-флаг | Feature flag | Переключатель поведения без выката кода. | [REL-04](topics/08-reliability.md#degradation) |
| Хвост распределения | Tail latency | Медленные запросы, определяющие пользовательский опыт при параллельных вызовах. | [PERF-02](topics/11-performance-and-cost.md#percentiles) |
| Хореография | Choreography | Сервисы реагируют на события друг друга без общего координатора. | [ARCH-04](topics/07-architecture-styles.md#event-driven) |
| Целевой уровень обслуживания | SLO | Числовая цель по показателю качества за окно времени. | [OPS-09](topics/10-delivery-and-ops.md#slo) |
| Цепочка поставок | Supply chain | Зависимости, образы и конвейер сборки как путь кода в прод. | [SEC-10](topics/09-security.md#supply-chain) |
| Шардирование | Sharding | Разрезание данных на части, живущие на разных узлах. | [DATA-10](topics/03-storage-and-data.md#sharding) |
| Штормовые повторы | Retry storm | Синхронизированные повторы, превращающие деградацию в отказ. | [REL-01](topics/08-reliability.md#timeouts-retries) |
| Эмбеддинг | Embedding | Числовой вектор, представляющий смысл объекта; основа поиска по близости. | [DATA-02](topics/03-storage-and-data.md#specialized-stores) |
| Эфемерное окружение | Ephemeral environment | Стенд, создаваемый из кода под задачу и удаляемый после. | [OPS-03](topics/10-delivery-and-ops.md#envs) |
| Ядовитое сообщение | Poison message | Сообщение, обработка которого падает всегда и блокирует поток. | [MSG-08](topics/05-async-and-messaging.md#consumer-retries) |
| Ячеистая архитектура | Cell-based architecture | Разделение системы на независимые экземпляры, каждый обслуживает часть пользователей. | [REL-07](topics/08-reliability.md#cells) |
| 2PC | Two-phase commit | Атомарная фиксация через координатора; блокирует участников при его отказе. | [DIST-08](topics/06-distributed-systems.md#distributed-transactions) |
| ACID | ACID | Атомарность, согласованность, изоляция, долговечность; C обеспечивается приложением. | [DATA-07](topics/03-storage-and-data.md#acid) |
| BFF | Backend for frontend | Сервис-агрегатор под конкретный тип клиента. | [ARCH-10](topics/07-architecture-styles.md#mesh) |
| CAP / PACELC | CAP / PACELC | При разрыве — согласованность или доступность; без разрыва — согласованность или задержка. | [DIST-02](topics/06-distributed-systems.md#cap) |
| CDC | Change data capture | Поток изменений, читаемый из журнала транзакций БД. | [MSG-07](topics/05-async-and-messaging.md#outbox) |
| CDN | Content delivery network | Сеть точек присутствия, отдающая контент из ближайшей к пользователю. | [EDGE-05](topics/02-traffic-and-edge.md#cdn) |
| DLQ | Dead letter queue | Очередь сообщений, исчерпавших попытки обработки. | [MSG-08](topics/05-async-and-messaging.md#consumer-retries) |
| Event sourcing | Event sourcing | Источник истины — последовательность событий; состояние является их свёрткой. | [ARCH-07](topics/07-architecture-styles.md#event-sourcing) |
| LSM-дерево | LSM tree | Структура хранения с дешёвой последовательной записью и слиянием уровней. | [DATA-05](topics/03-storage-and-data.md#indexes) |
| MVCC | MVCC | Многоверсионность: читатели не блокируют писателей. | [DATA-08](topics/03-storage-and-data.md#isolation) |
| RPO / RTO | RPO / RTO | Допустимая потеря данных и допустимое время восстановления. | [REL-09](topics/08-reliability.md#backup-dr) |
| SSE | Server-sent events | Односторонний поток событий от сервера поверх обычного HTTP. | [NET-12](topics/01-network-and-api.md#realtime) |
| Strangler fig | Strangler fig | Постепенное замещение старой системы новой через фасад на входе. | [ARCH-13](topics/07-architecture-styles.md#strangler) |
| STRIDE | STRIDE | Схема перебора угроз: подмена, изменение, отказ от авторства, раскрытие, отказ в обслуживании, повышение привилегий. | [SEC-11](topics/09-security.md#threat-modeling) |
| TCC | Try-Confirm-Cancel | Распределённая операция через резервирование ресурса с последующим подтверждением. | [DIST-08](topics/06-distributed-systems.md#distributed-transactions) |
| WAF | Web application firewall | Фильтр запросов по сигнатурам и правилам на периметре. | [EDGE-07](topics/02-traffic-and-edge.md#perimeter) |

---

Всего терминов: **95**. Числа и матрицы выбора — в [`90-cheatsheets.md`](90-cheatsheets.md); типовые ошибки — в [`91-antipatterns.md`](91-antipatterns.md); полный реестр тем — в [`01-roadmap.md`](01-roadmap.md).
