# Databases

## SQL / Relational Database Management Systems (RDBMS)
RDBMSs provide a way to structure data within disk (persistent storage) so that reading from and writing to it is efficient, using tables.  Each row contains information about a single primary key. A primary key uniquely identifies each record, where a record is a row.

They are implemented using B+ Trees, which are optimal for reducing disk I/O operations. 

![B+ Trees](./images/b-plus-trees.avif)

### Foreign Keys
Consider the following two tables that are created here:

```
CREATE TABLE People (
    PhoneNumber int PRIMARY KEY,
    Name varchar(100)
);
```

```
CREATE TABLE Homes (
    PhoneNumber int,
    Address varchar(255),
    FOREIGN KEY (PhoneNumber) REFERENCES People(PhoneNumber)
);
```

We can ensure that a phone number must exist within People before it can be inserted into Homes. This is a **foreign key** constraint. With this, each record in Homes is associated with a record in People.

### Joins
We can also retrieve information across tables through these key relations by using joins.

```
SELECT People.name, Homes.address
FROM People
JOIN Homes ON People.phone = Homes.phone;
```

### Trade-offs
All **transactions**, units consisting of a sequence of one or more SQL operations, within a RDBMS must follow ACID: Atomicity, Consistency, Isolation, and Durability. Only after all parts of the transaction are completed is the changed data committed to the database.

**Durability**: in the event of a crash, data is not lost - it is persistent

**Atomicity**: all the changes within a transaction are performed, or none of them are. Avoids inconsistent state.

![Atomicity](./images/atomicity.avif)

**Isolation**: a transaction is invisible to other transactions, so that intermediate states of a transaction don't affect other ones.

**Consistency**: refers to the adherence to predefined rules and constraints that maintain the validity of the data throughout the execution of multiple transactions (e.g. account balance can't be negative).

## NoSQL
Not only SQL. This encapsulates all non-relational databases, created to make horizontally scaling databases easier. With SQL databases, it is difficult to know how to split up the data and maintain consistency due to the complex relations. Vertical scaling is possible with SQL databases, but this has its limitations. There are several different types of NoSQL databases:

### Key-Value Databases
Just like a hashmap, the database stores a collection of key-value pairs and the key serves as a unique identifier. The keys and values can range from simple objects to complex objects. They are schemaless, meaning different keys and values can have completely different structures. Redis is an example.

### Document Databases
Document Databases store data as "documents". These "documents" are JSON-like. This structure is beneficial because individual fields in a document can be added/removed independently of others. An example is MongoDB.

### Wide-Column Databases
A wide-column database stores data in columns rather than rows. Each column corresponds to a specific attribute or field of the data. This structure not only enables high write throughput but also optimizes reads and aggregations over a particular subset of data, an operation that traditional row-based storage isn't designed for. Some examples are Cassandra and Google's BigTable. To illustrate this, consider the example below:

Row-Based:
```
Row 1: [Harry Potter, J.K. Rowling, Fantasy, $24.99, 1997]
Row 2: [1984, George Orwell, Fiction, $15.99, 1949]
Row 3: [The Hobbit, J.R.R. Tolkien, Fantasy, $19.99, 1937]
```

Column-Based:
```
Titles:     [Harry Potter, 1984, The Hobbit]
Authors:    [J.K. Rowling, George Orwell, J.R.R. Tolkien]
Genres:     [Fantasy, Fiction, Fantasy]
Prices:     [$24.99, $15.99, $19.99]
Years:      [1997, 1949, 1937]
```

If we want to know all the information about a book, like The Hobbit, row-based databases are very efficient. But if we only want to know the average price of all books, column-based databases are much more efficient, since we do not need to look at all the other data to get that information. 

### Graph Databases
A graph database uses a graph-like structure where each node refers to an entity. Nodes are connected to each other through edges, or relationships. Graph databases are very much useful when the data has complex relationship and interconnectedness. Consider Facebook, a platform that involves relationships between users, a good fit for a graph database.

![Graph DB](./images/graph-db.avif)

### Why we Need NoSQL Databases
The biggest issue with SQL databases is scale and the restrictions. Because there are no foreign key or join constraints, the data can be split and stored on different servers. NoSQL databases are designed with distributed architecture in mind. Not every single NoSQL database is ACID-compliant, but many are. In fact, MongoDB is an ACID-compliant database. The acronym for NoSQL databases typically though is **BASE**: Basically Available, Soft state, Eventual consistency. 

### Basically Available
"Basically Available" means the system guarantees availability of data even in the face of multiple failures. Instead of refusing operations when something goes wrong, a BASE system will still respond to requests, even if it can't give the most up-to-date data. Think of it like a restaurant that might be out of some ingredients but stays open to serve what it can, rather than closing entirely.

### Soft state
"Soft state" means the state of the system may change over time, even without any new input. This happens because the system is constantly working to update and synchronize data across different nodes. Imagine a group of friends sharing news - even without new information coming in, they might be in different states of awareness as they gradually tell each other what they know.

### Eventual Consistency
A mechanism that provides eventual consistency is the leader/follower architecture. The leader database can be written to and read from, while follower databases can only be read from. The follower databases get synced up with the leader, but it is possible that "stale" reads will occur, i.e. the follower database is not fully up-to-date. They *eventually* update with the new data of the leader: **eventual consistency**.

## Replication and Sharding
Two techniques commonly used together in a distributed system to achieve high availability and throughput.

### Replication
Replication involves creating a copy of the database called a replica to handle more requests. The replica(s) is hosted on a separate machine or server, and it is kept in sync with the original database. Replication is used to increase data availability, improve scalability, and increase data durability. The original database is the leader, while the replica(s) is a follower. Data flows from the leader to the follower, synchronously or aysnchronously. 

#### Synchronous Replication
Every write transaction on the leader is immediately replicated on the follower, ensuring consistency between the two replicas. However, this approach introduces latency, since the request will only be responded to once the leader has replicated its data to the followers. The benefit is that if the leader goes down, the mostly updated follower can take its place, providing high availability.

#### Asynchronous Replication
The leader database commits the transaction and sends replication data to the follower without waiting for the follower to acknowledge or apply the changes immediately. The requestor gets a response immediately and does not have to wait for the data to be replicated. This reduces latency, but it means that if a client makes a request to the follower before the leader has updated it, the data might be stale until the leader updates it. This is the trade-off made for increased availability.

#### Leader-Leader Replication
Leader-Leader replication is used when data needs to be served in different regions. Both leaders can be written to and read from, making it ideal for distributing data across different parts of the world. However, synchronization latency between the leaders can be a challenge, and measures like periodic updates are needed to keep them in sync.

### Sharding
Sharding is used when replication alone is insufficient to handle the high traffic volume on a single database. It involves dividing the database into smaller shards, each hosted on a separate machine or server. Each shard contains only a subset of the entire dataset, and they do not have a complete copy of the original database. But what decides how data gets partitioned? One approach is range-based, where data is split according to rangers. Consider an example of 100 rows and 4 shards, we could split it by doing ```1-25```, ```26-50```...

Determining how data is partitioned among shards is done using a shard key. The shard key is a chosen criterion or attribute that determines which shard each data belongs to. For example, in a relational database, the shard key might be based on sex, such as splitting data between male and female. Alternatively, it could be based on a first name/last name basis, such as dividing names from A-L and M-Z into separate shards. Consistent hashing could also be used to minimize rebalancing when nodes are added or removed from the system.

#### Challenge with Sharding
With relational databases and their ACID properties, ensuring related tables with related data end up in the same shard can be complex. Because of this, sharding is not built in. NoSQL databases are designed with this in mind, however, and are better suited for sharding due to their "eventual consistency" model.