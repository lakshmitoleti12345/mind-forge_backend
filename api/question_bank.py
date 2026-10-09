# Comprehensive Technical Interview Question Bank for MindForge
# Contains 30 Questions per domain: Python, SQL, JavaScript, React, Django REST API

QUESTION_BANK = {
    "Python Mastery": [
        {
            "front": "What is the Global Interpreter Lock (GIL) in Python and how does it impact multi-threading?",
            "back": "The GIL is a mutex that prevents multiple native threads from executing Python bytecodes at the same time in CPython. This means multi-threading in Python cannot achieve true CPU parallelization for CPU-bound tasks.",
            "explanation": "For CPU-bound tasks, use Python's `multiprocessing` module instead of `threading` to bypass the GIL.",
            "tags": "Python,Concurrency,GIL"
        },
        {
            "front": "What are Python Decorators and how do they work?",
            "back": "Decorators are functions that take another function as an argument, extend its behavior without modifying it, and return a new function.",
            "explanation": "Example:\n@my_decorator\ndef greet(): print('Hello')\nIs equivalent to: greet = my_decorator(greet)",
            "tags": "Python,Decorators,Functional"
        },
        {
            "front": "What is the difference between `list.sort()` and `sorted()` in Python?",
            "back": "`list.sort()` modifies the original list in-place and returns `None`.\n`sorted(iterable)` creates and returns a new sorted list from any iterable.",
            "explanation": "`list.sort()` is more memory efficient when modifying an existing list.",
            "tags": "Python,DataStructures"
        },
        {
            "front": "What are Python Generators and how does the `yield` keyword work?",
            "back": "Generators are functions that return an iterator using the `yield` keyword. Instead of returning all values at once, they yield values one at a time, saving memory.",
            "explanation": "Generators maintain their local execution state between `next()` calls.",
            "tags": "Python,Generators,Memory"
        },
        {
            "front": "What is the difference between `is` and `==` in Python?",
            "back": "`==` checks for value equality (do objects have equal values?).\n`is` checks for object identity (do variables point to the exact same memory address?).",
            "explanation": "Example: `a = [1, 2]; b = [1, 2]`. `a == b` is True, but `a is b` is False.",
            "tags": "Python,Basics,Memory"
        },
        {
            "front": "What is Context Management in Python and how do you implement a `with` statement?",
            "back": "Context managers handle resource allocation and cleanup (e.g. opening files or database connections). Implemented using `__enter__` and `__exit__` dunder methods or `@contextmanager`.",
            "explanation": "Ensures resources are closed safely even if exceptions occur.",
            "tags": "Python,ContextManager"
        },
        {
            "front": "What are `*args` and `**kwargs` in Python function definitions?",
            "back": "`*args` passes a variable number of non-keyword positional arguments as a tuple.\n`**kwargs` passes variable keyword arguments as a dictionary.",
            "explanation": "Example: `def fn(*args, **kwargs): print(args, kwargs)`",
            "tags": "Python,Functions"
        },
        {
            "front": "What is the difference between shallow copy and deep copy in Python?",
            "back": "Shallow copy (`copy.copy()`) creates a new object but references nested objects.\nDeep copy (`copy.deepcopy()`) recursively duplicates all nested objects.",
            "explanation": "Modifying nested elements in a shallow copy affects the original object.",
            "tags": "Python,Memory,Copy"
        },
        {
            "front": "How does Python handle Memory Management and Garbage Collection?",
            "back": "Python uses reference counting as its primary memory management mechanism. When a reference count reaches zero, memory is freed. It also uses a cyclic garbage collector to detect circular references.",
            "explanation": "Module `gc` exposes cyclic garbage collector controls.",
            "tags": "Python,Memory,GarbageCollection"
        },
        {
            "front": "What are Python `dataclasses` and why use them?",
            "back": "Introduced in Python 3.7, `@dataclass` automatically generates dunder methods like `__init__`, `__repr__`, `__eq__` for data-holding classes.",
            "explanation": "Example:\n@dataclass\nclass User:\n    name: str\n    age: int",
            "tags": "Python,OOP,DataClass"
        },
        {
            "front": "What is the difference between `__str__` and `__repr__` in Python?",
            "back": "`__str__` returns a readable, user-friendly string representation.\n`__repr__` returns an unambiguous string representation meant for developers and debugging.",
            "explanation": "Ideally `eval(repr(obj))` should reconstruct the original object.",
            "tags": "Python,OOP,Dunder"
        },
        {
            "front": "What is Python's MRO (Method Resolution Order)?",
            "back": "MRO defines the order in which Python searches for attributes and methods in multiple inheritance hierarchies. Uses C3 Linearization algorithm.",
            "explanation": "View MRO of a class via `ClassName.__mro__` or `ClassName.mro()`.",
            "tags": "Python,OOP,Inheritance"
        },
        {
            "front": "What are List Comprehensions vs Generator Expressions in Python?",
            "back": "List comprehension `[x for x in data]` creates the entire list in memory immediately.\nGenerator expression `(x for x in data)` evaluates lazily on-demand.",
            "explanation": "Generator expressions consume significantly less RAM for large datasets.",
            "tags": "Python,Memory,Performance"
        },
        {
            "front": "What is `asyncio` and how do `async` / `await` keywords work in Python?",
            "back": "`asyncio` provides asynchronous I/O event loop execution. `async def` defines a coroutine, and `await` pauses execution until a non-blocking asynchronous task completes.",
            "explanation": "Allows single-threaded handling of thousands of concurrent I/O operations.",
            "tags": "Python,Async,Concurrency"
        },
        {
            "front": "What is the difference between `@staticmethod` and `@classmethod`?",
            "back": "`@classmethod` receives the class (`cls`) as first argument and can modify class state.\n`@staticmethod` receives no automatic implicit first argument and behaves like a regular function attached to a class namespace.",
            "explanation": "Classmethods are often used as alternative constructor factory methods.",
            "tags": "Python,OOP,Decorators"
        },
        {
            "front": "What are `slots` (`__slots__`) in Python classes?",
            "back": "`__slots__` explicitly declares data members and prevents the creation of `__dict__`, reducing RAM overhead and speeding up attribute access.",
            "explanation": "Example: `class Point: __slots__ = ('x', 'y')`",
            "tags": "Python,Performance,Memory"
        },
        {
            "front": "What is the difference between `any()` and `all()` built-in functions?",
            "back": "`any(iterable)` returns True if AT LEAST ONE element is truthy.\n`all(iterable)` returns True ONLY if ALL elements are truthy.",
            "explanation": "Both use short-circuit evaluation.",
            "tags": "Python,Builtins"
        },
        {
            "front": "How do Python Exceptions work and what is the role of `else` and `finally` blocks?",
            "back": "`try`: Code to test for errors.\n`except`: Runs if exception occurs.\n`else`: Runs ONLY if NO exception occurs.\n`finally`: Runs ALWAYS regardless of errors.",
            "explanation": "Use `finally` for guaranteed cleanup operations like closing files.",
            "tags": "Python,Exceptions"
        },
        {
            "front": "What are Python Type Hints and how do static type checkers like `mypy` use them?",
            "back": "Type hints (`def add(a: int, b: int) -> int`) provide optional static typing documentation for IDE autocompletion and static analysis without altering runtime execution.",
            "explanation": "Enforced by tools like `mypy` or `pyright` during CI/CD builds.",
            "tags": "Python,TypeHints"
        },
        {
            "front": "What is `functools.lru_cache` in Python?",
            "back": "A decorator that wraps a function with a Least Recently Used (LRU) memoization cache to store recent function call results.",
            "explanation": "Greatly speeds up recursive functions like Fibonacci calculations.",
            "tags": "Python,Performance,Caching"
        },
        {
            "front": "What are Lambda Functions in Python?",
            "back": "Anonymous inline single-expression functions defined with `lambda arguments: expression`.",
            "explanation": "Example: `square = lambda x: x ** 2`",
            "tags": "Python,Functional"
        },
        {
            "front": "What is the difference between `__init__` and `__new__` in Python?",
            "back": "`__new__` is the actual instance creator method (returns the new instance).\n`__init__` is the instance initializer method (populates object attributes).",
            "explanation": "`__new__` is used when overriding immutable objects or implementing Singletons.",
            "tags": "Python,OOP,Advanced"
        },
        {
            "front": "What is Monkey Patching in Python?",
            "back": "Dynamic runtime modification of a class or module without editing source code.",
            "explanation": "Often used in testing to mock network API calls or DB connections.",
            "tags": "Python,Testing,Metaprogramming"
        },
        {
            "front": "What is the difference between mutable and immutable data types in Python?",
            "back": "Mutable types (`list`, `dict`, `set`) can be changed in-place.\nImmutable types (`int`, `str`, `tuple`, `frozenset`) cannot be modified after creation.",
            "explanation": "Only immutable types can be used as dictionary keys!",
            "tags": "Python,DataTypes"
        },
        {
            "front": "What is `zip()` and how does `zip(*iterables)` work?",
            "back": "`zip()` pairs elements from multiple iterables index-by-index. `zip(*zipped)` unzips a zipped sequence back into separate tuples.",
            "explanation": "Example: `list(zip([1,2], ['a','b']))` -> `[(1, 'a'), (2, 'b')]`",
            "tags": "Python,Iterators"
        },
        {
            "front": "What is the purpose of `__name__ == '__main__'` in Python scripts?",
            "back": "Checks if the Python script is being executed directly from CLI or imported as a module.",
            "explanation": "Prevents script execution code from running when imported into another file.",
            "tags": "Python,Modules"
        },
        {
            "front": "What is `collections.defaultdict` in Python?",
            "back": "A subclass of `dict` that returns a default value for non-existent keys instead of raising a `KeyError`.",
            "explanation": "Example: `counts = defaultdict(int)` automatically initializes missing keys to 0.",
            "tags": "Python,Collections"
        },
        {
            "front": "What is `itertools` module used for?",
            "back": "Provides fast, memory-efficient tools for creating iterators, combinations, permutations, and infinite cycles.",
            "explanation": "Functions include `permutations`, `combinations`, `chain`, `cycle`.",
            "tags": "Python,Iterators"
        },
        {
            "front": "What is global variable scope vs `nonlocal` keyword in Python?",
            "back": "`global` allows modifying variables defined at top-level module scope.\n`nonlocal` allows modifying variables in enclosing outer function scopes (closures).",
            "explanation": "Used in nested functions to mutate outer scope variables.",
            "tags": "Python,Scope"
        },
        {
            "front": "How do Python dataclass `field(default_factory=...)` work?",
            "back": "Prevents the mutable default argument bug by dynamically producing fresh instances (like `list` or `dict`) for every new object.",
            "explanation": "Example: `items: list = field(default_factory=list)`",
            "tags": "Python,DataClass,BestPractices"
        }
    ],

    "SQL & Database Mastery": [
        {
            "front": "What is the difference between INNER JOIN, LEFT JOIN, RIGHT JOIN, and FULL OUTER JOIN?",
            "back": "INNER JOIN: Matches records in both tables.\nLEFT JOIN: All left table records + matching right table records.\nRIGHT JOIN: All right table records + matching left table records.\nFULL OUTER JOIN: All records when there is a match in left or right table.",
            "explanation": "NULLs are populated for missing matches in outer joins.",
            "tags": "SQL,Joins,Databases"
        },
        {
            "front": "What are ACID properties in Relational Database Management Systems (RDBMS)?",
            "back": "Atomicity: All-or-nothing transaction execution.\nConsistency: Maintains valid DB constraint rules.\nIsolation: Concurrent transactions don't interfere.\nDurability: Committed data persists permanently.",
            "explanation": "Ensures reliable financial and transaction processing.",
            "tags": "SQL,Transactions,ACID"
        },
        {
            "front": "What is the difference between `WHERE` and `HAVING` clauses in SQL?",
            "back": "`WHERE` filters individual rows BEFORE aggregate grouping.\n`HAVING` filters aggregated group results AFTER `GROUP BY` execution.",
            "explanation": "Example: `SELECT dept, COUNT(*) FROM emp GROUP BY dept HAVING COUNT(*) > 5`",
            "tags": "SQL,Filtering,GroupBy"
        },
        {
            "front": "What is Database Indexing and how does a B-Tree index speed up queries?",
            "back": "Indexing creates a lookup data structure (typically B-Tree) that allows binary-like search operations ($O(\\log N)$ time) instead of full table scans ($O(N)$ time).",
            "explanation": "Tradeoff: Speeds up `SELECT`, but slows down `INSERT`/`UPDATE` due to index maintenance.",
            "tags": "SQL,Indexing,Performance"
        },
        {
            "front": "What is Database Normalization (1NF, 2NF, 3NF)?",
            "back": "1NF: Atomic values, no repeating groups.\n2NF: 1NF + no partial dependency on composite primary keys.\n3NF: 2NF + no transitive dependencies (non-key column depending on non-key column).",
            "explanation": "Normalization eliminates data redundancy and update anomalies.",
            "tags": "SQL,Normalization,DatabaseDesign"
        },
        {
            "front": "What is the difference between `TRUNCATE`, `DELETE`, and `DROP` in SQL?",
            "back": "`DELETE`: DML command, deletes rows one-by-one, supports `WHERE`, can be rolled back.\n`TRUNCATE`: DDL command, empties whole table quickly, resets identity auto-increment.\n`DROP`: DDL command, deletes entire table structure and data permanently.",
            "explanation": "`TRUNCATE` is faster than `DELETE` because it deallocates data pages directly.",
            "tags": "SQL,DDL,DML"
        },
        {
            "front": "What are Window Functions in SQL and how do `ROW_NUMBER()`, `RANK()`, and `DENSE_RANK()` differ?",
            "back": "Window functions perform calculations across related table rows without collapsing them into a single row (`OVER (PARTITION BY ... ORDER BY ...)`).\nROW_NUMBER: 1, 2, 3, 4\nRANK: 1, 2, 2, 4 (skips after ties)\nDENSE_RANK: 1, 2, 2, 3 (no gaps after ties)",
            "explanation": "Crucial for top-N analysis per group queries.",
            "tags": "SQL,WindowFunctions,Analytics"
        },
        {
            "front": "What is a CTE (Common Table Expression) and `WITH` clause in SQL?",
            "back": "A temporary named result set defined using `WITH` that exists only within the execution scope of a single SQL query.",
            "explanation": "Improves query readability and enables recursive queries.",
            "tags": "SQL,CTE,Queries"
        },
        {
            "front": "What is the N+1 Query Problem in ORMs and SQL?",
            "back": "Occurs when an application executes 1 initial SQL query to fetch N parent records, and then executes N additional queries to fetch child data for each parent.",
            "explanation": "Solvable using SQL JOINs or eager loading (`select_related`/`prefetch_related`).",
            "tags": "SQL,ORM,Performance"
        },
        {
            "front": "What is a Database Deadlock and how can it be prevented?",
            "back": "A condition where two or more transactions block each other indefinitely by holding locks on resources that the other transaction needs.",
            "explanation": "Prevented by acquiring locks in a consistent order and setting transaction lock timeouts.",
            "tags": "SQL,Transactions,Deadlock"
        },
        {
            "front": "What is the difference between a Primary Key and a Unique Key?",
            "back": "Primary Key: Uniquely identifies a record, CANNOT contain NULLs, only 1 per table.\nUnique Key: Ensures uniqueness, CAN contain NULL values, multiple allowed per table.",
            "explanation": "Primary keys automatically create clustered indexes in most RDBMS.",
            "tags": "SQL,Keys,Constraints"
        },
        {
            "front": "What is a Composite Key in SQL?",
            "back": "A primary key or unique constraint consisting of TWO OR MORE columns combined.",
            "explanation": "Example: `PRIMARY KEY (student_id, course_id)` in an enrollment table.",
            "tags": "SQL,Keys"
        },
        {
            "front": "What is Foreign Key Referential Integrity?",
            "back": "A constraint ensuring that child table foreign key values MUST exist in parent table primary key columns.",
            "explanation": "Configured with actions like `ON DELETE CASCADE` or `ON DELETE SET NULL`.",
            "tags": "SQL,Constraints,ReferentialIntegrity"
        },
        {
            "front": "What is a Database View vs Materialized View?",
            "back": "View: Virtual table stored as a saved query; runs dynamically on every read.\nMaterialized View: Physical copy of query results saved to disk; requires manual/scheduled refresh.",
            "explanation": "Materialized views drastically speed up complex analytical aggregation queries.",
            "tags": "SQL,Views,Performance"
        },
        {
            "front": "What is the SQL `COALESCE()` function?",
            "back": "Returns the FIRST non-NULL value from a list of expressions.",
            "explanation": "Example: `SELECT COALESCE(phone, mobile, 'No Contact') FROM users`",
            "tags": "SQL,Functions,Nulls"
        },
        {
            "front": "What is Database Sharding vs Partitioning?",
            "back": "Partitioning: Splitting a large table across separate files/disks on a SINGLE database server.\nSharding: Horizontal partitioning across MULTIPLE separate database server instances.",
            "explanation": "Sharding is used to scale databases to terabytes/petabytes of traffic.",
            "tags": "SQL,Scaling,Sharding"
        },
        {
            "front": "What is the difference between `UNION` and `UNION ALL`?",
            "back": "`UNION` combines query result sets and REMOVES duplicate rows (slower).\n`UNION ALL` combines result sets INCLUDING duplicates (faster).",
            "explanation": "Use `UNION ALL` unless duplicate removal is strictly required.",
            "tags": "SQL,Sets"
        },
        {
            "front": "What are Isolation Levels in SQL Transactions?",
            "back": "1. Read Uncommitted (allows Dirty Reads)\n2. Read Committed (prevents Dirty Reads)\n3. Repeatable Read (prevents Non-Repeatable Reads)\n4. Serializable (highest isolation, prevents Phantom Reads).",
            "explanation": "Higher isolation levels reduce concurrency throughput.",
            "tags": "SQL,Transactions,Isolation"
        },
        {
            "front": "What is a Dirty Read in SQL Transactions?",
            "back": "Occurs when Transaction A reads data that Transaction B modified but HAS NOT YET COMMITTED. If Transaction B rolls back, Transaction A read invalid data.",
            "explanation": "Prevented using 'Read Committed' isolation level or higher.",
            "tags": "SQL,Transactions"
        },
        {
            "front": "What is the SQL `EXPLAIN` or `EXPLAIN ANALYZE` command?",
            "back": "Displays the database query execution plan, showing table scans, index usage, join algorithms, and estimated query execution cost.",
            "explanation": "Indispensable tool for diagnosing slow SQL queries.",
            "tags": "SQL,Performance,Explain"
        },
        {
            "front": "What is the difference between OLTP and OLAP systems?",
            "back": "OLTP (Online Transaction Processing): Fast, short operational transactions (e.g. e-commerce orders).\nOLAP (Online Analytical Processing): Complex aggregation queries across historical data warehouses.",
            "explanation": "OLTP uses row-store DBs (PostgreSQL/MySQL); OLAP uses column-store DBs (Snowflake/ClickHouse).",
            "tags": "SQL,Architecture,DataWarehouse"
        },
        {
            "front": "What is Database Connection Pooling?",
            "back": "A cache of open database connections maintained by an application server to avoid the expensive TCP overhead of opening/closing DB connections per HTTP request.",
            "explanation": "Tools like `PgBouncer` or `HikariCP` handle connection pooling.",
            "tags": "SQL,Performance,ConnectionPool"
        },
        {
            "front": "What is `GROUP BY` and `AGGREGATE` functions (`COUNT`, `SUM`, `AVG`, `MAX`, `MIN`)?",
            "back": "`GROUP BY` collapses rows with identical column values into summary groups, allowing mathematical aggregate functions to run per group.",
            "explanation": "Every non-aggregated column in the `SELECT` list must be included in `GROUP BY`.",
            "tags": "SQL,Aggregation"
        },
        {
            "front": "What is an Upsert (`INSERT ... ON CONFLICT / ON DUPLICATE KEY UPDATE`) in SQL?",
            "back": "An atomic operation that inserts a new record, or updates existing column values if a primary key or unique constraint conflict occurs.",
            "explanation": "Prevents race conditions when inserting/updating records concurrently.",
            "tags": "SQL,Upsert,Transactions"
        },
        {
            "front": "What is a Database Trigger?",
            "back": "A stored procedural routine that automatically executes in response to specified `INSERT`, `UPDATE`, or `DELETE` events on a table.",
            "explanation": "Used for automated auditing and complex data validation rules.",
            "tags": "SQL,Triggers,Automation"
        },
        {
            "front": "What is a Correlated Subquery?",
            "back": "A subquery that references columns from the outer query, re-evaluating once for every row processed by the outer query.",
            "explanation": "Can cause poor performance compared to JOINs if datasets are large.",
            "tags": "SQL,Subqueries"
        },
        {
            "front": "What is the `EXISTS` vs `IN` operator in SQL?",
            "back": "`EXISTS` tests for row existence and short-circuits as soon as a single match is found (efficient for subqueries).\n`IN` evaluates all subquery values into a list.",
            "explanation": "`EXISTS` handles `NULL` values safely compared to `IN`.",
            "tags": "SQL,Subqueries,Performance"
        },
        {
            "front": "What is Database Database Backup: Hot vs Cold Backup?",
            "back": "Cold Backup: Performed while database is completely shut down.\nHot Backup: Performed while database is online and actively receiving read/write traffic.",
            "explanation": "Hot backups rely on Write-Ahead Logs (WAL).",
            "tags": "SQL,Backups,DevOps"
        },
        {
            "front": "What is Write-Ahead Logging (WAL)?",
            "back": "A transaction logging mechanism where database changes are written to a append-only log file on disk BEFORE committing changes to data storage files.",
            "explanation": "Ensures durability and atomicity during unexpected server crashes.",
            "tags": "SQL,WAL,Architecture"
        },
        {
            "front": "What is SQLite database locking model?",
            "back": "SQLite uses file-level locking. Multiple readers can read concurrently, but a write operation locks the ENTIRE database file exclusively.",
            "explanation": "WAL mode (`PRAGMA journal_mode=WAL`) allows concurrent reads while writing!",
            "tags": "SQLite,Locking,Performance"
        }
    ],

    "JavaScript Mastery": [
        {
            "front": "What is a JavaScript Closure and why is it useful?",
            "back": "A closure is a function bundled with references to its surrounding lexical environment. It allows an inner function to access variables from an outer function even after the outer function has returned.",
            "explanation": "Used for data privacy, currying, and stateful event listeners.",
            "tags": "JavaScript,Closures,Scope"
        },
        {
            "front": "What is the JavaScript Event Loop?",
            "back": "The event loop continuously monitors the Call Stack and Task Queues. When the Call Stack is empty, it processes all Microtasks (Promises) before executing the next Macrotask (setTimeout).",
            "explanation": "Allows single-threaded JavaScript to perform non-blocking I/O operations.",
            "tags": "JavaScript,Async,EventLoop"
        },
        {
            "front": "What is the difference between `var`, `let`, and `const` in JavaScript?",
            "back": "`var`: Function-scoped, hoisted with `undefined`, can be re-declared.\n`let`: Block-scoped, hoisted in Temporal Dead Zone (TDZ), reassignable.\n`const`: Block-scoped, hoisted in TDZ, CANNOT be reassigned.",
            "explanation": "Always prefer `const`, and use `let` when variables must mutate.",
            "tags": "JavaScript,Variables,ES6"
        },
        {
            "front": "What is Prototype Inheritance in JavaScript?",
            "back": "Every JavaScript object has a private prototype property (`[[Prototype]]`) linking to another object. When accessing a property, JS searches up the prototype chain until found or `null` is reached.",
            "explanation": "`Object.getPrototypeOf(obj)` returns an object's prototype.",
            "tags": "JavaScript,Prototypes,OOP"
        },
        {
            "front": "What is the difference between `==` and `===` in JavaScript?",
            "back": "`==` checks for loose equality after applying implicit type coercion.\n`===` checks for strict equality without type coercion (values and types must match).",
            "explanation": "Example: `5 == '5'` is True, but `5 === '5'` is False.",
            "tags": "JavaScript,Coercion,Basics"
        },
        {
            "front": "What are Promises in JavaScript and what are their 3 states?",
            "back": "A Promise represents the eventual completion or failure of an asynchronous operation.\n3 States:\n1. Pending\n2. Fulfilled (`.then()`)\n3. Rejected (`.catch()`)",
            "explanation": "Avoid nested callbacks ('callback hell') using Promises or `async/await`.",
            "tags": "JavaScript,Promises,Async"
        },
        {
            "front": "What is `async` / `await` in JavaScript?",
            "back": "Syntactic sugar built on top of Promises. `async` functions return a Promise, and `await` pauses execution until the Promise resolves or rejects.",
            "explanation": "Allows writing asynchronous code that looks synchronous.",
            "tags": "JavaScript,Async,ES8"
        },
        {
            "front": "What is Hoisting in JavaScript?",
            "back": "JavaScript's default behavior of moving variable and function declarations to the top of their containing scope during compilation phase.",
            "explanation": "Function declarations are fully hoisted; `let` & `const` enter the Temporal Dead Zone.",
            "tags": "JavaScript,Hoisting,Scope"
        },
        {
            "front": "What is the Temporal Dead Zone (TDZ)?",
            "back": "The period between entering a block scope and the actual variable initialization line for `let` and `const` variables.",
            "explanation": "Accessing a `let` variable in its TDZ throws a `ReferenceError`.",
            "tags": "JavaScript,TDZ,Scope"
        },
        {
            "front": "What is `this` binding in JavaScript and how does Arrow Functions affect it?",
            "back": "Regular functions bind `this` dynamically based on how they are called.\nArrow functions DO NOT have their own `this`; they capture `this` lexically from the enclosing scope.",
            "explanation": "Use arrow functions inside callbacks to retain outer scope `this`.",
            "tags": "JavaScript,This,ArrowFunctions"
        },
        {
            "front": "What is the difference between `call()`, `apply()`, and `bind()`?",
            "back": "`call(thisArg, arg1, arg2)`: Invokes function immediately with explicit `this` and arguments list.\n`apply(thisArg, [args])`: Invokes function immediately with arguments array.\n`bind(thisArg)`: Returns a NEW function with bound `this` for later invocation.",
            "explanation": "Used to explicitly set function execution context.",
            "tags": "JavaScript,This,Functions"
        },
        {
            "front": "What is Debouncing vs Throttling in JavaScript?",
            "back": "Debouncing: Delays function execution until a specified idle time passes without new events (e.g. search input autocompletion).\nThrottling: Limits function execution to once every N milliseconds (e.g. window scroll listeners).",
            "explanation": "Prevents performance bottlenecks during high-frequency browser events.",
            "tags": "JavaScript,Performance,Events"
        },
        {
            "front": "What is Event Delegation in JavaScript?",
            "back": "Attaching a single event listener to a parent DOM container instead of adding listeners to multiple child elements, leveraging Event Bubbling.",
            "explanation": "Improves memory usage and automatically handles dynamically added child nodes.",
            "tags": "JavaScript,DOM,EventDelegation"
        },
        {
            "front": "What is Event Bubbling vs Event Capturing?",
            "back": "Capturing Phase: Event trickles DOWN from Window to target element.\nBubbling Phase: Event bubbles UP from target element back to Window.",
            "explanation": "Use `event.stopPropagation()` to halt bubbling.",
            "tags": "JavaScript,DOM,Events"
        },
        {
            "front": "What is Deep Cloning in JavaScript (`structuredClone` vs `JSON.parse(JSON.stringify())`)?",
            "back": "`structuredClone()` is the native JS API for deep cloning objects including Dates, Maps, Sets, and Arrays.\n`JSON.parse(JSON.stringify())` fails on Functions, undefined, and Date objects.",
            "explanation": "Always use `structuredClone()` in modern JS engines.",
            "tags": "JavaScript,Objects,Cloning"
        },
        {
            "front": "What are ES6 Modules (`import` / `export`) vs CommonJS (`require` / `module.exports`)?",
            "back": "ES6 Modules: Static, asynchronous loading, standard in modern browsers & bundlers.\nCommonJS: Dynamic, synchronous loading, historical Node.js standard.",
            "explanation": "ES6 modules enable tree-shaking dead code elimination.",
            "tags": "JavaScript,Modules,ES6"
        },
        {
            "front": "What are Map and Set in ES6 JavaScript?",
            "back": "`Map`: Key-value collection where keys can be ANY type (objects, functions, primitives).\n`Set`: Collection of UNIQUE values.",
            "explanation": "`Set` is ideal for deduplicating arrays: `[...new Set(array)]`",
            "tags": "JavaScript,DataStructures,ES6"
        },
        {
            "front": "What is `WeakMap` and `WeakSet` in JavaScript?",
            "back": "Collections holding WEAK references to objects. Items in WeakMap/WeakSet do not prevent garbage collection if no other references exist.",
            "explanation": "Keys MUST be objects; WeakMaps are not iterable.",
            "tags": "JavaScript,Memory,GarbageCollection"
        },
        {
            "front": "What is Symbol data type in JavaScript?",
            "back": "A unique, immutable primitive data type used to create hidden, collision-free object property keys.",
            "explanation": "Example: `const id = Symbol('id')`",
            "tags": "JavaScript,Primitives,Symbols"
        },
        {
            "front": "What is Object.freeze() vs Object.seal()?",
            "back": "`Object.freeze()`: Prevents adding, deleting, or modifying existing property values (completely immutable).\n`Object.seal()`: Prevents adding or deleting properties, but ALLOWS modifying existing values.",
            "explanation": "Neither performs deep immutability on nested objects.",
            "tags": "JavaScript,Objects,Immutability"
        },
        {
            "front": "What is Optional Chaining (`?.`) and Nullish Coalescing (`??`) in JavaScript?",
            "back": "`?.`: Safely accesses nested object properties without throwing error if nullish.\n`??`: Returns right-hand operand ONLY if left-hand operand is `null` or `undefined` (unlike `||` which checks for falsy).",
            "explanation": "Example: `const name = user?.profile?.name ?? 'Guest'`",
            "tags": "JavaScript,ES2020,Syntax"
        },
        {
            "front": "What is Array Destructuring and Object Destructuring?",
            "back": "Syntax allowing unpacking of values from arrays or properties from objects into distinct variables.",
            "explanation": "Example: `const [a, b] = arr; const { name, age } = user;`",
            "tags": "JavaScript,Destructuring,ES6"
        },
        {
            "front": "What is `Promise.all()` vs `Promise.allSettled()`?",
            "back": "`Promise.all()`: Fails fast immediately if ANY Promise rejects.\n`Promise.allSettled()`: Waits for ALL Promises to settle (fulfilled or rejected) and returns array of outcome objects.",
            "explanation": "Use `allSettled` when you need results from all tasks regardless of individual failures.",
            "tags": "JavaScript,Promises,Async"
        },
        {
            "front": "What is `Promise.race()` vs `Promise.any()`?",
            "back": "`Promise.race()`: Settles as soon as the FIRST Promise settles (either resolve OR reject).\n`Promise.any()`: Resolves as soon as the FIRST Promise FULFILLS (ignores rejections unless ALL fail).",
            "explanation": "`Promise.any()` returns an `AggregateError` if all promises reject.",
            "tags": "JavaScript,Promises,Async"
        },
        {
            "front": "What is `use strict` directive in JavaScript?",
            "back": "Enforces strict parsing and error handling rules in JS code (e.g. prevents undeclared global variables, throws errors on read-only assignments).",
            "explanation": "ES6 modules automatically run in strict mode.",
            "tags": "JavaScript,StrictMode"
        },
        {
            "front": "What is Generator Function in JavaScript (`function*` and `yield`)?",
            "back": "A function that can be paused and resumed using the `yield` keyword, returning a Generator iterator object.",
            "explanation": "Used in Redux-Saga for managing async side-effects.",
            "tags": "JavaScript,Generators,Async"
        },
        {
            "front": "What is `Proxy` and `Reflect` API in JavaScript?",
            "back": "`Proxy`: Metaprogramming wrapper that intercepts and customizes basic object operations (get, set, delete).\n`Reflect`: Built-in object providing default target operations.",
            "explanation": "Vue 3 reactivity system is built entirely on JavaScript Proxies!",
            "tags": "JavaScript,Proxy,Metaprogramming"
        },
        {
            "front": "What is the difference between `forEach` and `map` in JavaScript?",
            "back": "`forEach`: Executes a callback for each array item, returns `undefined`, mutates or performs side-effects.\n`map`: Executes callback for each item and returns a NEW array with transformed values.",
            "explanation": "`map` is functional and chainable.",
            "tags": "JavaScript,Arrays,Functional"
        },
        {
            "front": "What is Currying in Functional JavaScript?",
            "back": "A technique of transforming a function with multiple arguments into a sequence of functions that each take a single argument.",
            "explanation": "Example: `f(a, b, c)` becomes `f(a)(b)(c)`",
            "tags": "JavaScript,Functional,Currying"
        },
        {
            "front": "What is `MutationObserver` in Web APIs?",
            "back": "A built-in browser API that monitors DOM trees for changes (attribute modifications, node insertion/deletion) asynchronously.",
            "explanation": "Replaced deprecated DOM Mutation Events for high performance.",
            "tags": "JavaScript,DOM,MutationObserver"
        }
    ],

    "React 19 Core": [
        {
            "front": "What is the Virtual DOM in React and how does Diffing work?",
            "back": "Virtual DOM is an in-memory lightweight JS representation of the real DOM. When state changes, React renders a new VDOM tree, diffs it against the old tree using a $O(N)$ heuristic algorithm (Reconciliation), and updates only changed real DOM nodes.",
            "explanation": "Minimizes expensive direct browser DOM reflows and repaints.",
            "tags": "React,VirtualDOM,Reconciliation"
        },
        {
            "front": "What are React Hooks and what are the two main rules of Hooks?",
            "back": "Hooks allow function components to use state and lifecycle features.\nRules:\n1. Call Hooks ONLY at the top level (not inside loops, conditions, or nested functions).\n2. Call Hooks ONLY from React function components or custom Hooks.",
            "explanation": "Ensures React preserves Hook state across multiple component renders.",
            "tags": "React,Hooks,Rules"
        },
        {
            "front": "What is `useEffect` Hook and how does the cleanup function work?",
            "back": "Manages side effects (fetching data, subscriptions, DOM mutations). Returning a function from `useEffect` acts as a cleanup cleanup step before the component unmounts or before re-running the effect.",
            "explanation": "Example: `useEffect(() => { const timer = setInterval(...); return () => clearInterval(timer); }, [])`",
            "tags": "React,Hooks,useEffect"
        },
        {
            "front": "What is the difference between `useMemo` and `useCallback` in React?",
            "back": "`useMemo`: Caches the calculated RESULT of a complex function execution.\n`useCallback`: Caches a FUNCTION INSTANCE to prevent child component re-renders.",
            "explanation": "Syntax: `useMemo(() => compute(), [deps])` vs `useCallback(() => fn(), [deps])`",
            "tags": "React,Hooks,Performance"
        },
        {
            "front": "What is `useRef` Hook and how is it different from `useState`?",
            "back": "`useRef` returns a mutable ref object (`.current`) that persists across renders. Crucially, updating a `ref` DOES NOT trigger a component re-render (unlike `useState`).",
            "explanation": "Used for DOM element access, timers, and previous state tracking.",
            "tags": "React,Hooks,useRef"
        },
        {
            "front": "What is React Context API and when should you use it?",
            "back": "Provides a way to pass data through the component tree without manually passing props down at every level (Prop Drilling).",
            "explanation": "Ideal for global state like themes, user authentication, and locale settings.",
            "tags": "React,Context,State"
        },
        {
            "front": "What is Prop Drilling and how can you avoid it?",
            "back": "Prop Drilling is passing props down through multiple layers of intermediate components that don't need the data themselves.",
            "explanation": "Avoided using React Context API, Redux/Zustand, or Component Composition.",
            "tags": "React,Props,Architecture"
        },
        {
            "front": "What is the difference between Controlled and Uncontrolled Components in React?",
            "back": "Controlled: Form input values are controlled entirely by React state (`value` & `onChange`).\nUncontrolled: Form data is handled directly by the DOM (`useRef`).",
            "explanation": "Controlled components enable real-time validation and instant state sync.",
            "tags": "React,Forms"
        },
        {
            "front": "What are React Keys and why are they required in Lists?",
            "back": "Keys give elements a stable identity so React's reconciliation engine can track which items were added, changed, or removed during list re-renders.",
            "explanation": "Avoid using array indices as keys if items can be re-ordered or deleted!",
            "tags": "React,Keys,Reconciliation"
        },
        {
            "front": "What is `React.memo` and when should you use it?",
            "back": "A higher-order component (HOC) that memoizes a function component, skipping re-renders if props have not changed (shallow equality comparison).",
            "explanation": "Use for expensive child components that render frequently with unchanged props.",
            "tags": "React,Performance,Memo"
        },
        {
            "front": "What is React 19 Server Components (RSC) vs Client Components?",
            "back": "Server Components execute strictly on the server during request time, shipping 0KB JavaScript to the client bundle.\nClient Components (`'use client'`) render on client with interactive state and event listeners.",
            "explanation": "Server components reduce bundle size and enable direct DB access.",
            "tags": "React19,RSC,ServerComponents"
        },
        {
            "front": "What is `useActionState` and `useFormStatus` in React 19?",
            "back": "`useActionState`: Simplifies form submission state management with async Server Actions.\n`useFormStatus`: Provides status information (like `pending`) of a parent `<form>`.",
            "explanation": "Eliminates boilerplate `isLoading` and `error` state management.",
            "tags": "React19,Actions,Forms"
        },
        {
            "front": "What is React StrictMode and why does it double-render in development?",
            "back": "A development tool that highlights potential problems (deprecated APIs, unexpected side-effects). In dev mode, it intentionally double-invokes render methods and effects to catch non-pure functions.",
            "explanation": "Does not affect production builds.",
            "tags": "React,StrictMode,DevTools"
        },
        {
            "front": "What are Error Boundaries in React?",
            "back": "Class components that catch JavaScript errors anywhere in their child component tree, log errors, and display a fallback UI instead of crashing the app.",
            "explanation": "Uses `componentDidCatch` or `getDerivedStateFromError`.",
            "tags": "React,ErrorHandling"
        },
        {
            "front": "What is Custom Hooks in React?",
            "back": "JavaScript functions starting with `use` that encapsulate reusable stateful logic combining standard React Hooks.",
            "explanation": "Example: `useFetch(url)`, `useLocalStorage(key)`.",
            "tags": "React,CustomHooks"
        },
        {
            "front": "What is Code Splitting and `React.lazy()` with `Suspense`?",
            "back": "`React.lazy()` enables dynamic importing of components as separate bundle chunks. `Suspense` displays a fallback UI (loader) while the chunk is downloading.",
            "explanation": "Example: `const Dashboard = React.lazy(() => import('./Dashboard'))`",
            "tags": "React,CodeSplitting,Performance"
        },
        {
            "front": "What is the difference between `useLayoutEffect` and `useEffect`?",
            "back": "`useEffect` runs asynchronously AFTER DOM painting (non-blocking).\n`useLayoutEffect` runs synchronously BEFORE browser DOM painting.",
            "explanation": "Use `useLayoutEffect` for DOM measurements to prevent visual flickers.",
            "tags": "React,Hooks,DOM"
        },
        {
            "front": "What is SyntheticEvent in React?",
            "back": "React's cross-browser wrapper around browser native events, ensuring uniform event property behavior across Chrome, Firefox, Safari, and Edge.",
            "explanation": "Delegates events to document root for performance.",
            "tags": "React,Events,SyntheticEvent"
        },
        {
            "front": "What is state immutability in React and why should you never mutate state directly?",
            "back": "React relies on shallow reference equality checks (`prevObj !== nextObj`) to determine if component re-rendering is needed. Direct state mutation (`state.items.push()`) breaks change detection.",
            "explanation": "Always create new object copies (`setState([...items, newItem])`).",
            "tags": "React,State,Immutability"
        },
        {
            "front": "What is `useTransition` Hook in React?",
            "back": "Allows marking state updates as non-urgent transitions, keeping the main thread responsive during expensive UI renders.",
            "explanation": "Returns `[isPending, startTransition]`.",
            "tags": "React,Hooks,Performance"
        },
        {
            "front": "What is `useDeferredValue` Hook in React?",
            "back": "Defers updating a secondary value until high-priority renders (like typing in a text input) finish processing.",
            "explanation": "Similar to debouncing, but built into React's scheduler.",
            "tags": "React,Hooks,Concurrent"
        },
        {
            "front": "What is React Portal (`createPortal`)?",
            "back": "Renders child components into a DOM node outside the parent component's DOM hierarchy.",
            "explanation": "Commonly used for Modals, Tooltips, and Popovers.",
            "tags": "React,Portals,DOM"
        },
        {
            "front": "What is the difference between Redux Toolkit and React Context API?",
            "back": "Context API: Simple, built-in, best for low-frequency updates (themes/auth). High frequency updates can trigger mass re-renders.\nRedux Toolkit: Centralized store with selective selector subscriptions and middleware ecosystem.",
            "explanation": "Use Redux Toolkit for complex global state with frequent updates.",
            "tags": "React,Redux,State"
        },
        {
            "front": "What is `useOptimistic` Hook in React 19?",
            "back": "Allows showing an optimistic updated UI state immediately while an asynchronous server request is still pending in the background.",
            "explanation": "Automatically rolls back if the server action fails.",
            "tags": "React19,OptimisticUI"
        },
        {
            "front": "What is Higher-Order Component (HOC) in React?",
            "back": "A pattern where a function takes a component as an argument and returns an enhanced new component (`const EnhancedComp = withAuth(BaseComp)`).",
            "explanation": "Largely replaced by custom React Hooks.",
            "tags": "React,HOC,Patterns"
        },
        {
            "front": "What is Render Props pattern in React?",
            "back": "A technique for sharing code between components using a prop whose value is a function returning React elements (`<DataProvider render={data => <h1>{data}</h1>} />`).",
            "explanation": "Alternative to HOCs before custom Hooks.",
            "tags": "React,Patterns"
        },
        {
            "front": "What is `useId` Hook in React?",
            "back": "Generates unique, stable accessibility IDs across client and server SSR renders.",
            "explanation": "Prevents SSR hydration mismatch errors for form labels and inputs.",
            "tags": "React,Accessibility,SSR"
        },
        {
            "front": "What is Hydration Mismatch in React SSR?",
            "back": "Occurs when the server-rendered HTML structure does not match the initial client-side React Virtual DOM render tree.",
            "explanation": "Causes React to throw console warnings and re-render the tree.",
            "tags": "React,SSR,Hydration"
        },
        {
            "front": "What is `useImperativeHandle` Hook in React?",
            "back": "Customizes the instance value exposed to parent components when using `ref` with `forwardRef`.",
            "explanation": "Limits parent component access to internal child methods.",
            "tags": "React,Hooks,Refs"
        },
        {
            "front": "What is Component Lifecycle in Class vs Functional Components?",
            "back": "Class: `componentDidMount`, `componentDidUpdate`, `componentWillUnmount`.\nFunctional: Handled via `useEffect` dependency array (`[]`, `[deps]`, return cleanup).",
            "explanation": "`useEffect` combines all 3 lifecycle stages cleanly.",
            "tags": "React,Lifecycle"
        }
    ],

    "Django REST Framework": [
        {
            "front": "What is MVT (Model-View-Template) Architecture in Django?",
            "back": "Model: Defines database data structures & ORM.\nView: Handles business logic and HTTP requests.\nTemplate: Manages user presentation layer (HTML).",
            "explanation": "In DRF, Views return JSON responses instead of HTML Templates.",
            "tags": "Django,MVT,Architecture"
        },
        {
            "front": "What is the difference between `select_related` and `prefetch_related` in Django ORM?",
            "back": "`select_related`: Performs SQL `JOIN` for single-valued relationships (ForeignKey, OneToOne).\n`prefetch_related`: Performs separate SQL query and joins in Python for multi-valued relationships (ManyToMany, reverse FK).",
            "explanation": "Essential for eliminating N+1 database queries!",
            "tags": "Django,ORM,Performance"
        },
        {
            "front": "What are Django REST Framework Serializers?",
            "back": "Serializers convert complex Django Model instances into Python datatypes (`dict`) that can easily be rendered into JSON/XML, and deserialize incoming JSON back into validated Django objects.",
            "explanation": "Provides built-in data validation rules.",
            "tags": "DRF,Serializers,APIs"
        },
        {
            "front": "What is `ModelViewSet` in Django REST Framework?",
            "back": "A class combining complete CRUD logic (`list`, `create`, `retrieve`, `update`, `destroy`) for a Django model in a single unified view class.",
            "explanation": "Automatically routes endpoints using DRF `DefaultRouter`.",
            "tags": "DRF,ViewSets,APIs"
        },
        {
            "front": "What is JWT Authentication (`djangorestframework-simplejwt`) and how does Token Refresh work?",
            "back": "JWT returns an Access Token (short-lived, e.g. 15 mins) and Refresh Token (long-lived, e.g. 7 days). Client passes Access Token in `Authorization: Bearer <token>`. When expired, Client exchanges Refresh Token for a new Access Token.",
            "explanation": "Stateless authentication suitable for mobile and decoupled SPA React apps.",
            "tags": "Django,Security,JWT"
        },
        {
            "front": "What are Django Middleware and how does request processing work?",
            "back": "Middleware are hooks that run globally during every Django Request/Response cycle. Process incoming requests before reaching the view and process outgoing responses before returning to client.",
            "explanation": "Examples: CorsMiddleware, CsrfViewMiddleware, AuthenticationMiddleware.",
            "tags": "Django,Middleware"
        },
        {
            "front": "What are Django Signals (`post_save`, `pre_save`) and when should you use them?",
            "back": "Signals allow decoupled applications to get notified when actions occur elsewhere (e.g. automatically creating a `UserProfile` whenever a new `User` is saved).",
            "explanation": "Sender triggers signal, Receiver function executes handling logic.",
            "tags": "Django,Signals"
        },
        {
            "front": "What is Django ORM `F()` expression?",
            "back": "An `F()` object represents the value of a database field directly in SQL without pulling it into Python memory.",
            "explanation": "Prevents race conditions when updating counters: `Product.objects.filter(id=1).update(views=F('views') + 1)`",
            "tags": "Django,ORM,FExpressions"
        },
        {
            "front": "What is Django ORM `Q()` expression?",
            "back": "Used to construct complex SQL queries combining `AND`, `OR` (`|`), and `NOT` (`~`) logic.",
            "explanation": "Example: `Book.objects.filter(Q(title__icontains='Python') | Q(tags__name='Django'))`",
            "tags": "Django,ORM,QExpressions"
        },
        {
            "front": "What is CORS (Cross-Origin Resource Sharing) in Django REST Framework?",
            "back": "A security mechanism using HTTP headers that allows or restricts web applications running on one domain (e.g. React at `localhost:5173`) from making API calls to Django running on another domain (`localhost:8000`).",
            "explanation": "Handled via `django-cors-headers` package.",
            "tags": "Django,CORS,Security"
        },
        {
            "front": "What is the difference between `APIView`, `GenericAPIView`, and `ModelViewSet` in DRF?",
            "back": "`APIView`: Lowest level DRF view, manual handler method implementation (`def get`, `def post`).\n`GenericAPIView`: Adds serializer and queryset helper logic.\n`ModelViewSet`: Complete high-level CRUD boilerplate elimination.",
            "explanation": "Choose based on degree of custom flexibility needed.",
            "tags": "DRF,Views"
        },
        {
            "front": "What is Django Database Migration (`makemigrations` vs `migrate`)?",
            "back": "`makemigrations`: Inspects `models.py` changes and creates new SQL migration files.\n`migrate`: Executes migration files against the database to update database schema.",
            "explanation": "Maintains version-controlled schema synchronization.",
            "tags": "Django,Migrations,Databases"
        },
        {
            "front": "What is `transaction.atomic()` in Django?",
            "back": "A context manager or decorator ensuring that a block of database queries runs inside an atomic SQL transaction. If an exception occurs, ALL queries roll back automatically.",
            "explanation": "Crucial for financial transfers or multi-model orders.",
            "tags": "Django,Transactions,ACID"
        },
        {
            "front": "What are Custom Permission Classes in DRF (`BasePermission`)?",
            "back": "Classes implementing `has_permission(request, view)` or `has_object_permission(request, view, obj)` to enforce authorization rules.",
            "explanation": "Example: `IsOwnerOrReadOnly` or `IsAdminUser`.",
            "tags": "DRF,Permissions,Security"
        },
        {
            "front": "What is Django Custom User Model (`AbstractUser` vs `AbstractBaseUser`)?",
            "back": "`AbstractUser`: Extends standard Django User fields (first_name, email) while allowing extra fields.\n`AbstractBaseUser`: Provides total control over user model fields (requires building auth methods).",
            "explanation": "Always define a custom user model at project start!",
            "tags": "Django,Auth,UserModel"
        },
        {
            "front": "What is Django REST Framework Throttle Classes?",
            "back": "Rate-limiting middleware restricting how many HTTP requests a client can make within a specified timeframe (`UserRateThrottle`, `AnonRateThrottle`).",
            "explanation": "Prevents API abuse and Denial of Service (DoS) attacks.",
            "tags": "DRF,Throttling,Security"
        },
        {
            "front": "What is Celery with Redis/RabbitMQ in Django?",
            "back": "An asynchronous task queue used to run long-running tasks (sending emails, image processing, generating PDF reports) in background worker processes without blocking HTTP request execution.",
            "explanation": "Redis acts as the message broker queue.",
            "tags": "Django,Celery,Async"
        },
        {
            "front": "What is `SerializerMethodField` in DRF?",
            "back": "A read-only field whose value is calculated dynamically by invoking a method on the serializer class (`get_<field_name>`).",
            "explanation": "Example: `is_due = serializers.SerializerMethodField(); def get_is_due(self, obj): return ...`",
            "tags": "DRF,Serializers"
        },
        {
            "front": "What is the difference between `save()` and `create()` in DRF Serializers?",
            "back": "`create(validated_data)`: Defines how to instantiate and return a NEW model instance.\n`update(instance, validated_data)`: Defines how to modify an existing instance.\n`save()`: Invokes either `create()` or `update()` depending on whether instance was passed.",
            "explanation": "Override to handle nested serializer creation.",
            "tags": "DRF,Serializers"
        },
        {
            "front": "What is Django Database Connection Pooling & `CONN_MAX_AGE`?",
            "back": "Settings controlling database connection re-use. Setting `CONN_MAX_AGE` to integer seconds reuses database connections across multiple HTTP requests instead of opening new TCP connections per request.",
            "explanation": "Significantly improves API request response latency.",
            "tags": "Django,Performance,Database"
        },
        {
            "front": "What is `db_index=True` in Django Models?",
            "back": "Directs Django migration generator to create a database index on that specific column.",
            "explanation": "Use on columns frequently filtered in `filter()` or `order_by()`.",
            "tags": "Django,Indexes,Performance"
        },
        {
            "front": "What is `unique_together` vs `UniqueConstraint` in Django Models?",
            "back": "`unique_together`: Legacy tuple configuration for composite unique keys.\n`UniqueConstraint`: Modern replacement allowing functional constraints and conditional index filtering (`condition=Q(...)`).",
            "explanation": "Always use `UniqueConstraint` in modern Django.",
            "tags": "Django,Models,Constraints"
        },
        {
            "front": "What is Django Manager (`objects`) and how do you write a Custom Manager?",
            "back": "The interface through which Django database query operations are provided to models. Custom managers extend `models.Manager` to encapsulate reusable QuerySet filter methods.",
            "explanation": "Example: `Book.objects.published()`",
            "tags": "Django,ORM,Managers"
        },
        {
            "front": "What is `@action` decorator in DRF ViewSets?",
            "back": "Adds custom extra endpoints to a `ModelViewSet` that don't fit standard CRUD routes.",
            "explanation": "Example: `@action(detail=True, methods=['post']) def publish(self, request, pk=None):`",
            "tags": "DRF,ViewSets,Routing"
        },
        {
            "front": "What is Django `bulk_create()` and `bulk_update()`?",
            "back": "`bulk_create(list)`: Inserts a list of model instances in a SINGLE batch SQL query.\n`bulk_update(list, fields)`: Updates specified columns for a list of instances in one query.",
            "explanation": "Dramatically speeds up inserting thousands of objects.",
            "tags": "Django,ORM,Performance"
        },
        {
            "front": "What is Django `values()` and `values_list()`?",
            "back": "`values()`: Returns a QuerySet yielding dictionaries instead of model instances.\n`values_list()`: Returns tuples of specified field values.",
            "explanation": "Consumes less memory by skipping full Django model instantiation.",
            "tags": "Django,ORM,Optimization"
        },
        {
            "front": "What is Django CSRF (Cross-Site Request Forgery) protection?",
            "back": "Ensures that POST/PUT/DELETE requests originate from the user's browser app rather than a malicious external site by validating a secret CSRF token.",
            "explanation": "DRF Token/JWT APIs are exempt when using HTTP headers.",
            "tags": "Django,Security,CSRF"
        },
        {
            "front": "What is Django Cache Framework (`django.core.cache`)?",
            "back": "Allows caching views, template fragments, or database query results in memory (Redis/Memcached).",
            "explanation": "Functions include `cache.get(key)`, `cache.set(key, value, timeout)`.",
            "tags": "Django,Caching,Performance"
        },
        {
            "front": "What is `django-filter` package in DRF?",
            "back": "Provides declarative query param filtering for ViewSets (`filterset_fields = ['category', 'status']`).",
            "explanation": "Enables automatic URL search filtering.",
            "tags": "DRF,Filtering,APIs"
        },
        {
            "front": "What is Django SQLite to PostgreSQL production migration strategy?",
            "back": "SQLite is file-backed and ideal for local dev; production requires PostgreSQL for concurrent multi-process connection handling, row-level locking, and JSONB fields.",
            "explanation": "Configured via `DATABASES['default']` settings using `dj-database-url`.",
            "tags": "Django,PostgreSQL,Production"
        }
    ]
}
