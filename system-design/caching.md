# Caching
Caching is simply the process of making copies of data. Typically data is copied to a location where it can be accessed faster. On single computers, RAM data is copied to the CPU cache. On browsers, static data is copied to disk, significantly faster than transferring it across a network. On distributed systems, database/disk data is copied to RAM. It is important that copies of data do not become out of sync.

## Caching from the Client's Perspective
When a client attempts to load data, it first checks the memory cache, then the disk cache, and finally makes a network request if not found in either cache. When a cached file is found, this is known as a **cache hit**. When a cached file is not found, this is known as a **cache miss**.

## Cache Ratio
$\frac{\text{no. of cache hits}}{\text{no. of cache hits} + \text{no. of misses}}$
The higher the ratio, the better our cache is performing.

## Caching from the Server's Perspective
Thinking about a Twitter server, how should the server determine which tweets to cache and which to retrieve from the disk? Below are some strategies.

## Caching Strategies 
### Write-Around
A newly created resource is first written to disk. Only when a retrieval for that resource occurs does it get written to the cache. You are writing around the cache, first going to the disk.

### Write-Through
A newly created resource is written to both the disk and the cache. This might be inefficient since some resources will be very infrequently accessed but will still land in the cache.

### Write-Back
A newly created resource will be written to the cache only. This can be risky since the cache is not persistent storage, and if the server crashes, this data will be lost.

## Eviction Policies
**FIFO**: first in, first out. Similar to a queue.

**LRU**: least recently used. If an item has not been accessed for a long time, it is less likely to be accessed in the future as well. Fitting for something like Twitter.

![LRU Cache](./images/lru-cache.avif)

**LFU**: least frequently used. It's implemented using key-value pairs, where the key represents the item and the value represents the frequency of its usage. When the cache space runs out, the item with the smallest frequency is evicted.

## CDNs
A **CDN**, or content delivery network, is a group of cache servers that are located around the world so they can cache content close to end users. Without these, end users would have to request resources from the **origin server**, even if it was across the globe. CDNs speed up content delivery and reduce load on the origin server. The downside of a CDN is that we can usually only put static content on them. We can't have application code on the CDN servers. Again, this is similar to caching. There are modern edge servers that can do this, but they are still new.

![CDN](./images/cdn.avif)

### Push CDNs
- Content is proactively pushed to all CDN servers from origin
- Best for static, infrequently changing content
- Higher storage costs but faster delivery (guaranteed cache hits)
- Requires manual content management and updates
- Ideal for: Global video content, static assets

![Push CDN](./images/push-cdn.avif)

### Pull CDNs
- Content is fetched from origin only when requested
- Best for dynamic, frequently changing content
- Lower storage costs but potential initial latency
- Automatic content management via cache misses/hits
- Content can vary by region based on local demand
- Ideal for: Social media platforms like Twitter

![Pull CDN](./images/pull-cdn.avif)

Key Difference: Push CDNs prioritize speed and guaranteed availability at the cost of storage and maintenance, while Pull CDNs optimize for storage efficiency and automatic content distribution at the cost of potential initial latency.