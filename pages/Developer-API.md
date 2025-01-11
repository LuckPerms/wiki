### Intro

LuckPerms has a complete developer API, which allows other plugins on the server to read and modify LuckPerms data, and easily integrate LuckPerms deeply into existing plugins and systems.

### Versioning

The API uses [Semantic Versioning](https://semver.org/), meaning whenever a non-backwards compatible change is made, the major version will increment. You can rest assured knowing your integration will not break between versions, providing the major version remains the same.

The current API release is `5.4`.

* The API package in LuckPerms is `net.luckperms.api`.
* JavaDocs are available either in [a standard JavaDoc layout](https://javadoc.io/doc/net.luckperms/api/latest/), or within the API [source code](https://github.com/LuckPerms/LuckPerms/tree/master/api/src/main/java/net/luckperms/api).

#### Changelogs

* Version `2.x` represented the initial release of the API. 
* Version `3.x` (19th Feb 17) introduced a number of backwards incompatible changes. [[changelog](https://gist.github.com/lucko/fdf6ae4b2d9e466d8103dd9c68e5db9e)]
* Version `4.x` (7th Nov 17) introduced a number of backwards incompatible changes. [[changelog](https://gist.github.com/lucko/34c5c3c52ad80f8541395a096a937e91)]
* Version `5.x` was a complete rewrite of the API. Bridging tools are provided to maintain compatibility with older versions.

## Quick start guide

* [Adding LuckPerms to your project](#adding-luckperms-to-your-project)
  * [Maven](#maven)
  * [Gradle](#gradle)
  * [Manual](#manual)
* [Obtaining an instance of the API](#obtaining-an-instance-of-the-api)
  * [Using the Bukkit ServicesManager](#using-the-bukkit-servicesmanager)
  * [Using the Sponge ServicesManager](#using-the-sponge-servicesmanager)
  * [Using the singleton](#using-the-singleton-static-access)
* [Useful information](#useful-information)
  * [Thread safety](#thread-safety)
  * [Immutability](#immutability)
  * [Blocking operations](#blocking-operations)
  * [Using CompletableFutures](#using-completablefutures)
  * [Asynchronous events & callbacks](#asynchronous-events--callbacks)

___

### Adding LuckPerms to your project

The API artifact is published to the [Maven Central](http://central.sonatype.org/) repository.

#### Maven

If you're using Maven, simply add this to the `dependencies` section of your POM.

````xml
<dependencies>
    <dependency>
        <groupId>net.luckperms</groupId>
        <artifactId>api</artifactId>
        <version>5.4</version>
        <scope>provided</scope>
    </dependency>
</dependencies>
````

#### Gradle

If you're using Gradle, you need to add these lines to your build script.

##### Groovy DSL:
```gradle
repositories {
    mavenCentral()
}

dependencies {
    compileOnly 'net.luckperms:api:5.4'
}
```

##### Kotlin DSL:
```gradle
repositories {
    mavenCentral()
}

dependencies {
    compileOnly("net.luckperms:api:5.4")
}
```

#### Manual

If you want to manually add the API dependency to your classpath, you can obtain the jar by:

1. Navigating to [`https://repo1.maven.org/maven2/net/luckperms/api/`](https://repo1.maven.org/maven2/net/luckperms/api/)
2. Selecting the version you wish to use
3. Downloading the jar titled `api-x.x.jar`

___

### Obtaining an instance of the API

The root API interface is `LuckPerms`. You need to obtain an instance of this interface in order to do anything.

It can be obtained in a number of ways.

#### Using the Bukkit ServicesManager

When the plugin is enabled, an instance of `LuckPerms` will be provided in the Bukkit ServicesManager. (obviously you need to be writing your plugin for Bukkit!)

```java
RegisteredServiceProvider<LuckPerms> provider = Bukkit.getServicesManager().getRegistration(LuckPerms.class);
if (provider != null) {
    LuckPerms api = provider.getProvider();
    
}
```

#### Using the Sponge ServicesManager

When the plugin is enabled, an instance of `LuckPerms` will be provided in the Sponge ServicesManager. (obviously you need to be writing your plugin for Sponge!)

```java
Optional<ProviderRegistration<LuckPerms>> provider = Sponge.getServiceManager().getRegistration(LuckPerms.class);
if (provider.isPresent()) {
    LuckPerms api = provider.get().getProvider();
    
}
```

#### Using the singleton (static access)

When the plugin is enabled, an instance of `LuckPerms` can be obtained statically from the `LuckPermsProvider` class. (this will work on all platforms)

**Note:** this method will throw an `IllegalStateException` if the API is not loaded.

```java
LuckPerms api = LuckPermsProvider.get();
```

___

### Useful information

Now you've added the API classes to your project, and obtained an instance of the `LuckPerms`, you're almost ready to start using the API. However, before you go any further, please make sure you read and understand the information below.

#### Thread safety

* All LuckPerms internals are thread-safe. You can safely interact with the API from async scheduler tasks (or just generally from other threads)
* This also extends to the permission querying methods in Bukkit/Bungee/Sponge. These can be safely called async when LuckPerms is being used as the permissions plugin.

#### Immutability

* In cases where methods return classes from the Java collections framework, assume that the returned methods are always immutable, unless indicated otherwise. (in the JavaDocs)
* This means that you cannot make changes to any returned collections, and that the collections are only an accurate representation of the underlying data at the time of the method call.

#### Blocking operations

* Some methods are not "main thread friendly", meaning that if they are called from the main Minecraft Server thread, the server will lag.
* This is because many methods conduct I/O with either the file system or the network. 
* In most cases, these methods return [CompletableFutures](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html).
* Futures can be an initially complex paradigm for some users - however, it is crucial that you have at least a basic understanding of how they work before attempting to use them.
* As a general rule, it is advised that if it's convenient to do so, you conduct as much work with the API as possible within async scheduler tasks. Some methods don't return futures, but may still involve a number of relatively complex computations.


#### Using CompletableFutures

This is a super quick guide. If you'd like more comprehensive info, see the [CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html) or [CompletionStage](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletionStage.html) JavaDoc pages.

For the purposes of explaining, take the following method in the `ActionLogger` class.

```java
CompletableFuture<ActionLog> getLog();
```

After calling the method, we get a `CompletableFuture<ActionLog>` - the object we actually want is the `ActionLog`. The `CompletableFuture` represents the result of some computation (in this case the computation to obtain the ActionLog), and provides us with methods to obtain the `ActionLog` object.

If the context of our method call is already asynchronous (if we're calling the method from an async scheduler task), then we can do-away with the future entirely.

```java
/*
  Calling this method "requests" an ActionLog from the API.
  
  However, it's unlikely that the log will be available immediately...
  We need to wait for it to be supplied.
*/
CompletableFuture<ActionLog> logFuture = actionLogger.getLog();

/*
  Since we're already on an async thread, it doesn't matter how long we
  have to wait for the elusive Log to show up.
  
  The #join method will block - and wait until the Log has been supplied,
  and then return it.
  
  If for whatever reason the process to obtain a ActionLog threw an exception,
  this method will rethrow an the same exception wrapped in a CompletionException
*/
ActionLog log = logFuture.join();
```

An alternative to using `#join` is to register a callback with the CompletableFuture, to be executed once the `Log` is supplied.

If we need to use the instance on the main server thread, then a special executor can be passed to the callback is executed on the server thread.

```java
// Create an executor that will run our callback on the server thread.
Executor executor = runnable -> Bukkit.getScheduler().runTask(plugin, runnable);

// Register a callback with the future.
logFuture.whenCompleteAsync(new BiConsumer<ActionLog, Throwable>() { // can be reduced to a lambda, I've left it as an anonymous class for clarity
    @Override
    public void accept(ActionLog log, Throwable exception) {
        if (exception != null) {
            // There was some error whilst getting the log.
            return;
        }

        // Use the log for something...
    }
}, executor);
```

If you don't care about errors, this can be simplified further.

```java
logFuture.thenAcceptAsync(log -> { /* Use the log for something */ }, executor);
```

The CompletableFuture class can initially be very confusing to use (it's still a relatively new API in Java!), however it is a great way to encapsulate async computations, and in the case of Minecraft, ensures that users don't accidentally block the server thread waiting on lengthy I/O calls.

#### Asynchronous events & callbacks

* The vast majority of LuckPerms' work is done in async tasks away from the server thread.
* With that in mind, it would be silly to call LuckPerms events synchronously - meaning that, without exception, all events listeners are called asynchronously.

Please keep in mind that many parts of Bukkit, Sponge and the Minecraft server in general are not thread-safe, and should only be interacted with from the server thread. If you need to use Bukkit or Sponge methods from within LuckPerms event listeners or callbacks, you need to perform your action using the scheduler.
