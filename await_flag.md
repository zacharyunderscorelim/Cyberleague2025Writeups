In the source code file:

>Proxyserver.scala

we see this code:

```
val getData = {
  val isValid = isAllowed & url.startsWith("http://flagserver")
  val response: Response[String] = quickRequest
    .get(uri"$url")
    .send()
  isAllowed = isValid && response.isSuccess
  response.body
}
```
Meaning that for us to access the webpage, ```isAllowed``` must be ```true``` and ```url``` starts with "http://flagserver"

The dockerfile for flagserver exposes port 8081
hence my url should be something like: http://35.187.242.102:10011/proxy?url=http://flagserver:8081/flag&secret=WHATEVER_MATCHES_THE_HASHES
but wait:
```
var isAllowed = true

val secretChecks = secrets zip SECRETS map { inputs =>
  Future {
    isAllowed = isAllowed & BCrypt.checkpw(inputs._1, inputs._2)
  }
}

```
isAllowed already starts as true
the code uses a concurrent bCrypt check for the different hashes, checking the hashes in different threads within Future{}
This line:

```isAllowed = isAllowed & BCrypt.checkpw(inputs._1, inputs._2)```

has a race condition. Since Futures execute concurrently, multiple threads may read or write isAllowed at the same time. Before the hash check in the Future even completes, sometimes, a thread might already read isAllowed as true, since it was set as that before.

Hence, sometimes, our link will work no matter what our parameter secret is.

cyberleague{r4c3_y0u_t0_th3_fl4g_-_sl0w34t_w1n5}