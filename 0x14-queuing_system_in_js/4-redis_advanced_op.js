const redis = require('redis');
const { restore } = require('sinon');
const client = redis.createClient();

client.on("error", function(error) {
  console.error(`Redis client not connected to the server: ${error}`);
});

client.on('connect', function() {
  console.log('Redis client connected to the server');
  client.hset(['HolbertonSchools', 'Portland', 50], redis.print);
  client.hset(['HolbertonSchools', 'Seattle', 80], redis.print);
  client.hset(['HolbertonSchools', 'New York', 20], redis.print);
  client.hset(['HolbertonSchools', 'Bogota', 20], redis.print);
  client.hset(['HolbertonSchools', 'Cali', 40], redis.print);
  client.hset(['HolbertonSchools', 'Paris', 2], redis.print);
  client.hgetall('HolbertonSchools', function(err, res) {
    console.log(res);
  })
});
