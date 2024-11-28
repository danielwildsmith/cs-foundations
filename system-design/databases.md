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